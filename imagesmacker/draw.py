from textwrap import wrap
from typing import Any, Union

from PIL import Image, ImageDraw
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.main import QRCode

from imagesmacker.fonts import FontSizeCalculator, font_loader
from imagesmacker.models.coordinates import XYXY, RectangleCoordinates
from imagesmacker.models.draw import TextConfig
from imagesmacker.models.fields import FieldAttributes

RecursiveDict = dict[str, Union[str, list["RecursiveDict"], "RecursiveDict"]]


def qr(data: str, box_size: int = 20, border: int = 1, **kwargs) -> StyledPilImage:
    qr = QRCode(
        border=border,
        box_size=box_size,
    )
    qr.add_data(data)
    qr.make(fit=True)
    return qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
    )


class Draw:
    """
    An abstraction of `ImageDraw.Draw` specifically for drawing texts
    and QR codes in images.
    """

    def __init__(self, image: Image.Image) -> None:
        self.image = image
        self.draw = ImageDraw.Draw(image)

    def text(  # noqa: C901
        self,
        text: str,
        field_coords: RectangleCoordinates,
        field_attributes: FieldAttributes,
    ) -> None:
        """
        This method will try to fit the text within the field.

        Args:
        - text (`str`): Text to be drawn
        - field_coords (`RectangleCoordinates`): _description_
        - field_attributes (`FieldAttributes`): _description_
        """

        # Initialize variables
        draw_text_common_kwargs: dict[str, Any] = {}

        text_config = field_attributes.text_config

        font_size = text_config.font_size
        anchor = text_config.anchor

        fsc = FontSizeCalculator(self.draw, text_config.font_filepath)

        field_x1, field_y1, field_x2, field_y2 = field_coords.xyxy()
        field_x, field_y, field_width, field_height = field_coords.xywh()

        # If the text is multiline or is allowed to be broken into multiple lines, then
        # we try to break it into multiple lines so that it can fit into the field
        if ("\n" in text) or text_config.break_text:
            font_size, text_lines_list, text_height = self.break_text(
                text=text,
                text_config=text_config,
                font_size=font_size,
                fsc=fsc,
                field_width=field_width,
                field_height=field_height,
            )
        # Else, we just try to fit a single line of text in the field
        else:
            while True:
                text_width, text_height = fsc.get_text_bbox(font_size, text)
                # If `text_width` is greater than `field_width` or if `text_height` is
                # greater than `field_height`, then the `font_size` will be decremented
                # by 1, and the loop will continue until the condition is no longer
                # satisfied.
                if (text_width > field_width) or (text_height > field_height):
                    font_size -= 1
                else:
                    break

        # If the text needs to be inverted (ie. turned upside down), then, it needs to
        # undergo the following steps:
        if text_config.inverted:
            # I dont know why this code is here, so I just commented it out
            # # Get the half of the text height, then round that
            # halved_text_height = round(text_height / 2) # `hth` in short
            # # Subtract `hth` to the `text_height` to get the larger half of the text
            # # height. This is for pixel accuracy
            # larger_hth = text_height - halved_text_height
    
            # # field_height += text_height

            # Create a new image with the same width and height as the field to draw the
            # soon-to-be inverted text on
            inverted_text_image = Image.new(
                "RGBA",
                (field_width, field_height),
                color=(0, 0, 0, 0),
            )
            draw = ImageDraw.Draw(inverted_text_image)

            horizontal_anchor, vertical_anchor = anchor  # type: ignore

            # Reverse horizontal anchor
            match horizontal_anchor:
                case "l":
                    horizontal_anchor = "r"
                case "r":
                    horizontal_anchor = "l"

            # I DO NOT FUCKING UNDERSTAND WHY I NEED TO DO THIS
            # edit: I don't care anymore
            if not text_config.break_text:
                match vertical_anchor:
                    case "t":
                        vertical_anchor = "b"
                    case "b":
                        vertical_anchor = "t"

            anchor = horizontal_anchor + vertical_anchor
        else:
            draw = self.draw

        draw_text_common_kwargs["font"] = font_loader(
            text_config.font_filepath,
            font_size,
        )
        draw_text_common_kwargs["anchor"] = anchor

        # If the text is multiline or is allowed to be broken into multiple lines, then
        if ("\n" in text) or text_config.break_text:
            # text_height over length of text_lines_list
            tholtlt = text_height / len(text_lines_list)

            # there is a `vertical_additive` to place the multiline text exactly where
            # it is aligned to
            match anchor[1]:
                case "t":
                    vertical_additive = (
                        field_height - text_height if text_config.inverted else field_y
                    )
                case "m":
                    vertical_additive = round(
                        (field_height - text_height) / 2
                        if text_config.inverted
                        else field_y + ((field_height - text_height) / 2),
                    )
                case "b":
                    vertical_additive = (
                        0
                        if text_config.inverted
                        else field_y + field_height - text_height
                    )

            text_x = field_coords.text_coordinates(anchor=anchor)[0] - field_x # type: ignore
            draw_text_common_kwargs["anchor"] = anchor[0] + "m"

            for text_line, text_y in zip(
                text_lines_list,
                range(round(tholtlt / 2), text_height, round(tholtlt)),
                strict=True,
            ):
                text_xy = (text_x, vertical_additive + text_y)
                draw.text(
                    text=text_line,
                    xy=text_xy,
                    **draw_text_common_kwargs,
                )

                # WARNING: remove in production
                # text_width, text_height = fsc.get_text_bbox(font_size, text_line)
                # rect_coordinates = (
                #     text_xy[0] - (text_width / 2),
                #     text_xy[1] - (text_height / 2),
                #     text_xy[0] + (text_width / 2),
                #     text_xy[1] + (text_height / 2),
                # )
                # self.draw.rectangle(
                #     rect_coordinates,
                #     outline="white",
                #     width=1,
                # )
        else:
            draw_field_coords: RectangleCoordinates
            if text_config.inverted:
                draw_field_coords = XYXY(0, 0, field_x2 - field_x1, field_y2 - field_y1)
            else:
                draw_field_coords = field_coords

            draw.text(
                text=text,
                xy=draw_field_coords.text_coordinates(anchor=anchor), # type: ignore
                **draw_text_common_kwargs,
            )

        if text_config.inverted:
            inverted_text_image = inverted_text_image.rotate(180)
            self.image.paste(
                inverted_text_image,
                (field_x1, field_y1, field_x2, field_y2),
                inverted_text_image,
            )

    def break_text(
        self,
        text: str,
        text_config: TextConfig,
        font_size: int,
        fsc: FontSizeCalculator,
        field_width: int,
        field_height: int,
    ) -> tuple[int, list[str], int]:
        while True:
            # Initialize variables
            text_width = 0
            text_line_width_list = []
            text_line_height_list = []

            text_lines_list = text.splitlines()  # tlt
            # Count the number of characters in the longest line of the multiline text
            max_char_length_in_tlt = max(len(i) for i in text_lines_list)

            # We can deduce the number of characters that fit in the field width
            # by multiplying the field width by `max_char_length_in_tlt`, all over the
            # width of the text is when drawn on the image.
            # This uses the fact that `(a/(b/c)) = ((a * c)/b)` to simplify the equation
            characters_per_field_width = round(
                (field_width * max_char_length_in_tlt)
                / fsc.get_text_bbox(font_size, text)[0],
            )

            # Rewrite the `text_lines_list` to have the longest line of text be
            # the value of `characters_per_field_width`
            text_lines_list = [
                j for i in text_lines_list for j in wrap(i, characters_per_field_width)
            ]
            length_tlt = len(text_lines_list)

            # Measure the width and height of each line of text, then appened it
            # to the intialized lists earlier
            for text_line in text_lines_list:
                text_line_width, text_line_height = fsc.get_text_bbox(
                    font_size,
                    text_line,
                )
                text_line_width_list.append(text_line_width)
                text_line_height_list.append(text_line_height)

                # set `text_width` to be the width of the widest line of text
            text_width = max(text_line_width_list)

            text_height = round(
                length_tlt
                * text_config.line_height
                * (sum(text_line_height_list) / length_tlt),
            )

            # If `text_width` is greater than `field_width` or if `text_height` is
            # greater than `field_height`, then the `font_size` will be decremented
            # by 1, and the loop will continue until the condition is no longer
            # satisfied.
            if (text_width > field_width) or (text_height > field_height):
                font_size -= 1
            else:
                return (font_size, text_lines_list, text_height)
