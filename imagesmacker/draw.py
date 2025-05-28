from collections.abc import Callable
from textwrap import wrap
from typing import Any

from barcode import Code128
from barcode.writer import ImageWriter as BarcodeImageWriter
from PIL import Image, ImageDraw
from pydantic import BaseModel
from qrcode.image.base import BaseImage
from qrcode.image.pil import PilImage
from qrcode.main import QRCode

from imagesmacker.exceptions import DrawDataTypeInvalid, DrawDataTypeNotInFieldAttrs
from imagesmacker.fonts import FontSizeCalculator, font_loader
from imagesmacker.models.coordinates import XYXY, RectangleCoordinates
from imagesmacker.models.draw import (
    BarcodeConfig,
    Code128Config,
    FieldConfig,
    QRCodeConfig,
    TextConfig,
)
from imagesmacker.utils import scale_and_center_rect


def check_if_type_in_field_attrs(
    field_attributes: BaseModel,
) -> Callable[[str], BaseModel]:
    def inner(type: str) -> BaseModel:
        original_type = type
        types = type.split(":")
        extracted_field_attributes = field_attributes
        for type_iter in types:
            extracted_field_attributes = getattr(extracted_field_attributes, type_iter, None)  # type: ignore
            if extracted_field_attributes is None:
                raise DrawDataTypeNotInFieldAttrs(original_type)
        return extracted_field_attributes  # type: ignore

    return inner


class Barcode:
    @staticmethod
    def code128(
        data: str,
        field_coords: RectangleCoordinates,
        field_attributes: Code128Config,
    ) -> PilImage:
        options_parameters = [
            "module_width",
            "module_height",
            "quiet_zone",
            "text_distance",
        ]
        options = {i: getattr(field_attributes, i) for i in options_parameters}
        barcode_class = Code128(data, writer=BarcodeImageWriter())

        bc_width, bc_height = barcode_class.render(
            writer_options=field_attributes.options,
            text="",
        ).size
        field_width, field_height = field_coords.xywh()[2:4]

        bc_aspect_ratio = bc_height / bc_width
        field_aspect_ratio = field_height / field_width
        bc_factor = options["module_height"] / bc_aspect_ratio

        options["module_height"] = field_aspect_ratio * bc_factor

        return barcode_class.render(writer_options=options, text="")

    @staticmethod
    def qr(
        data: str,
        field_coords: RectangleCoordinates,
        field_attributes: QRCodeConfig,
    ) -> BaseImage:
        qr = QRCode(
            border=field_attributes.border,
            box_size=field_attributes.box_size,
        )
        qr.add_data(data)
        qr.make(fit=True)
        return qr.make_image(
            back_color=field_attributes.background_color,
            fill_color=field_attributes.foreground_color,
            # image_factory=StyledPilImage,
            # module_drawer=RoundedModuleDrawer(),
        )


class Draw:
    """An abstraction of `ImageDraw.Draw` specifically for drawing texts and barcodes in images."""

    def __init__(self, image: Image.Image) -> None:
        self.image = image
        self.draw = ImageDraw.Draw(image)

    def text(  # noqa: C901
        self,
        data: str,
        field_coords: RectangleCoordinates,
        field_attributes: TextConfig,
    ) -> None:
        """
        Try to fit the text within the field.

        Args:
        - text (`str`): Text to be drawn
        - field_coords (`RectangleCoordinates`): _description_
        - field_attributes (`FieldAttributes`): _description_

        """

        text = data

        # If there is no text to draw, return immediately.
        if (text is None) or (str(text).strip() == ""):
            return

        text_config = field_attributes

        max_font_size = text_config.max_font_size
        anchor = text_config.anchor
        text_style = text_config.style

        font_size_calculator = FontSizeCalculator(self.draw, text_config.font)

        field_x1, field_y1, field_x2, field_y2 = field_coords.xyxy()
        field_x_coords, field_y, field_width, field_height = field_coords.xywh()

        # If the text is multiline or is allowed to be broken into multiple lines, then
        # we try to break it into multiple lines so that it can fit into the field
        if ("\n" in text) or text_config.break_text:
            max_font_size, text_lines_list, text_height = self.break_text(
                text=text,
                text_config=text_config,
                font_size=max_font_size,
                fsc=font_size_calculator,
                field_width=field_width,
                field_height=field_height,
            )
        # Else, we just try to fit a single line of text in the field
        else:
            while True:
                text_width, text_height = font_size_calculator.get_text_bbox(
                    max_font_size,
                    text,
                )

                if (text_width > field_width) or (text_height > field_height):
                    max_font_size = max_font_size // 2
                elif (field_width > text_width > (field_width * 0.9)) or (
                    field_height > text_height > (field_height * 0.9)
                ):
                    break
                else:
                    max_font_size = round(max_font_size * 1.5)

            while True:
                if (text_width < field_width) and (text_height < field_height):
                    max_font_size = max_font_size + 1
                else:
                    break

                text_width, text_height = font_size_calculator.get_text_bbox(
                    max_font_size,
                    text,
                )

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

        draw_text_common_kwargs: dict[str, Any] = {
            "font": font_loader(
                text_config.font,
                max_font_size,
            ),
            "anchor": anchor,
            "fill": text_style.fill,
        }

        # If the text is multiline or is allowed to be broken into multiple lines, then
        # we do the following:
        if ("\n" in text) or text_config.break_text:
            # We just approximate where to place the lines of text vertically.
            # That's why there are overlaps in glyphs when the line height is set at 1.
            # That's also why line height's default is set at `1.2`.
            # If we don't approximate this, then we can have non-overlapping glyphs,
            # but I have a deadline to meet, yknow?

            # text_height over length of text_lines_list
            text_height_over_text_lines_list = text_height / len(text_lines_list)

            # there is a `vertical_additive` to place the multiline text exactly where
            # it is aligned to
            match anchor[1]:
                case "t":
                    vertical_additive = (
                        field_height - text_height if text_config.inverted else field_y
                    )
                case "m":
                    vertical_additive = round(
                        (
                            (field_height - text_height) / 2
                            if text_config.inverted
                            else field_y + ((field_height - text_height) / 2)
                        ),
                    )
                case "b":
                    vertical_additive = (
                        0
                        if text_config.inverted
                        else field_y + field_height - text_height
                    )

            text_x_coords = field_coords.text_coordinates(anchor=anchor)[0]  # type: ignore

            if text_config.inverted:
                text_x_coords -= field_x_coords

            draw_text_common_kwargs["anchor"] = anchor[0] + "m"

            for text_line, text_y in zip(
                text_lines_list,
                range(
                    round(text_height_over_text_lines_list / 2),
                    text_height,
                    round(text_height_over_text_lines_list),
                ),
                strict=True,
            ):
                text_xy = (text_x_coords, vertical_additive + text_y)
                draw.text(
                    text=text_line,
                    xy=text_xy,
                    **draw_text_common_kwargs,
                )

                # # WARNING: remove in production
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

            # # WARNING: remove in production
            # self.draw.rectangle(
            #     field_coords.xyxy(),
            #     outline="red",
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
                xy=draw_field_coords.text_coordinates(anchor=anchor),  # type: ignore
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

            # If `text_width` is greater than `field_width`, or if `text_height` is
            # greater than `field_height`, then the `font_size` will be decremented
            # by 1, and the loop will continue until the condition is no longer
            # satisfied.
            if (text_width > field_width) or (text_height > field_height):
                font_size -= 1
            else:
                return (font_size, text_lines_list, text_height)

    def barcode(
        self,
        data: str,
        field_coords: RectangleCoordinates,
        field_attributes: type[BarcodeConfig],
    ) -> None:
        # If there is no text to draw, return immediately.
        if (data is None) or (str(data).strip() == ""):
            return

        match field_attributes:
            case Code128Config():
                data_type = "code128"
            case QRCodeConfig():
                data_type = "qr"
            case _:
                raise DrawDataTypeInvalid(type(field_attributes).__name__)

        barcode = getattr(Barcode, data_type)(
            data=data,
            field_coords=field_coords,
            field_attributes=field_attributes,
        )

        size: tuple[int, int] = barcode.size

        barcode_coords = scale_and_center_rect(field_coords, size)
        barcode_wh = barcode_coords.xywh()[2:4]

        self.image.paste(
            barcode.resize(barcode_wh, Image.Resampling.LANCZOS),
            barcode_coords.xyxy(),
        )

    def data(
        self,
        type: str,
        data: str,
        field_coords: RectangleCoordinates,
        field_attributes: FieldConfig,
    ) -> None:
        fn: Callable[..., None]
        extracted_field_attributes: Any

        original_type = type
        citifa = check_if_type_in_field_attrs(field_attributes)
        extracted_field_attributes = citifa(type)

        match type:
            case "text":
                fn = self.text
            case _:
                type, *subtypes = type.split(":")
                match type:
                    case "barcode":
                        fn = self.barcode
                    case _:
                        raise DrawDataTypeInvalid(original_type)

        fn(data, field_coords, extracted_field_attributes)
