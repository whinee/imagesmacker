from textwrap import wrap
from typing import Any, Union

from PIL import Image, ImageDraw
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.main import QRCode

from imagesmacker.fonts import FontSizeCalculator, font_loader
from imagesmacker.models.coordinates import RectangleCoordinates
from imagesmacker.models.draw import TextAnchor, TextConfig
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
    An abstraction of `ImageDraw.Draw` specifically for drawing multiline text
    and QR codes in images.
    """

    def __init__(self, image: Image.Image) -> None:
        self.image = image
        self.draw = ImageDraw.Draw(image)

    def text(
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

        # x1, field_y, x2, y2 = field_coords.xyxy()
        field_x, field_y, field_width, field_height = field_coords.xywh()

        # Fit the text in the given field
        print(fsc.get_text_bbox(font_size, text))

        # If the text is multiline or is allowed to be broken into multiple lines, then
        # we try to break it into multiple lines so that it can fit into the field
        if ("\n" in text) or text_config.break_text:
            font_size, text_lines_list, text_height = self.break_text(
                text,
                text_config,
                font_size,
                fsc,
                field_width,
                field_height,
            )
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

        anchor, draw, field_x, field_y = self.inverted_draw(
            text_config, anchor, field_x, field_y, field_width, field_height, text_height
        )

        # print(text_lines_list)

        draw_text_common_kwargs["font"] = font_loader(
            text_config.font_filepath,
            font_size,
        )
        draw_text_common_kwargs["anchor"] = anchor

        if ("\n" in text) or text_config.break_text:
            # text_height over length of text_lines_list
            tholtlt = text_height / len(text_lines_list)

            match anchor[1]:
                case "t":
                    vertical_additive: float = (
                        field_height - text_height if text_config.inverted else field_y
                    )
                case "m":
                    vertical_additive = (
                        (field_height - text_height) / 2
                        if text_config.inverted
                        else field_y + ((field_height - text_height) / 2)
                    )
                case "b":
                    vertical_additive = (
                        0
                        if text_config.inverted
                        else field_y + field_height - text_height
                    )

            text_x = field_coords.text_coordinates(anchor=anchor)[0]
            draw_text_common_kwargs["anchor"] = anchor[0] + "m"

            for t, ty in zip(
                text_lines_list,
                range(round(tholtlt / 2), text_height, round(tholtlt)),
                strict=True,
            ):
                text_width, text_height = fsc.get_text_bbox(text)
                draw.text(
                    text=t,
                    xy=(text_x, vertical_additive + ty),
                    **draw_text_common_kwargs,
                )
        else:
            draw.text(
                text=text,
                xy=field_coords.text_coordinates(anchor=anchor),  # type: ignore
                **draw_text_common_kwargs,
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
                field_width
                * max_char_length_in_tlt
                / (fsc.get_text_bbox(font_size, text)[0]),
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

    def inverted_draw(
        self,
        text_config: TextConfig,
        anchor: TextAnchor,
        field_x: int,
        field_y: int,
        field_width: int,
        field_height: int,
        text_height: int,
    ) -> tuple[TextAnchor, ImageDraw.Draw, int, int]:
        if text_config.inverted:
            hth = round(text_height / 2)  # halved text height
            lhth = text_height - hth  # large half of the text height
            field_height += text_height
            inverted_text_image = Image.new(
                "RGBA", (field_width, field_height), color=(0, 0, 0, 0),
            )
            draw = ImageDraw.Draw(inverted_text_image)

            horizontal_anchor, vertical_anchor = anchor

            match horizontal_anchor:
                case "l":
                    anchor = "r" + vertical_anchor # type: ignore
                    field_x = field_height
                case "m":
                    field_x = round(field_height / 2)
                case "r":
                    anchor = "l" + vertical_anchor # type: ignore
                    field_x = 0

            match vertical_anchor:
                case "a":
                    field_y = field_height - text_height - lhth
                case "m":
                    field_y = round(field_height / 2)
                case "d":
                    field_y = text_height + lhth
        else:
            draw = self.draw

        return anchor, draw, field_x, field_y
