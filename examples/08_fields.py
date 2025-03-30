import os

from alltheutils.utils import parent_dir_nth_times
from PIL import Image, ImageDraw

from imagesmacker.draw import Draw
from imagesmacker.fields import relative_field_formatting
from imagesmacker.models.coordinates import XYWH
from imagesmacker.models.draw import TextConfig, TextStyle
from imagesmacker.models.fields import (
    FieldsConfig,
    FieldsCoords,
    RelativeDataFieldFormat,
    RelativeFieldCell,
    RelativeRow,
    TextFieldAttributes,
)

text = """The quick brown fox jumps over the lazy dog"""

horizontal_anchors = ["l", "m", "r"]
vertical_anchors = ["t", "m", "b"]

default_font = os.path.join(
    parent_dir_nth_times(__file__, 2),
    "assets/fonts/arial bold.ttf",
)

image_size = image_width, image_height = [1000, 1000]  # landscape A4 size x5
image = Image.new("RGB", image_size, color="black")

draw = ImageDraw.Draw(image)
smack_draw = Draw(image)

default_text_field_attr = TextFieldAttributes(
    text_config=TextConfig(
        font_filepath=default_font,
        font_size=50,
        anchor="mm",
        break_text=True,
        style=TextStyle(fill="#fff"),
    ),
)


def walk(
    fields_text: dict[str, str],
    fields_coords: FieldsCoords,
    fields_config: FieldsConfig,
) -> None:
    for field_name, field_text in fields_text.items():
        field_attributes: TextFieldAttributes = fields_config[field_name]  # type: ignore
        smack_draw.text(
            text=field_text,
            field_coords=fields_coords[field_name],
            field_attributes=field_attributes,
        )


fields_text = {
    "A": "A: 1x1",
    "B": "B: 2x1",
    "C": "C: 1x2",
    "D": "D: 2x2",
}

data_field_fmt = RelativeDataFieldFormat(rows=[
    RelativeRow(fr=1, cells=[
        RelativeFieldCell(fr=1, name="A"),
        RelativeFieldCell(fr=2, name="B"),
    ]),
    RelativeRow(fr=2, cells=[
        RelativeFieldCell(fr=1, name="C"),
        RelativeFieldCell(fr=2, name="D"),
    ]),
])

fields_config = {key: default_text_field_attr for key in fields_text.keys()}

fields_coords = relative_field_formatting(
    data_field_fmt,
    XYWH(0, 0, image_width, image_height),
)

walk(fields_text=fields_text, fields_coords=fields_coords, fields_config=fields_config)


def draw_boxes() -> None:
    for field_coords in fields_coords.values():
        draw.rectangle(field_coords.list(), outline="white", width=3)
        # x1, y1, x2, y2 = field_coords.list()
        # middle_x = round((x1 + x2) / 2)
        # middle_y = round((y1 + y2) / 2)
        # draw.line((middle_x, y1, middle_x, y2), fill="white", width=1)
        # draw.line((x1, middle_y, x2, middle_y), fill="white", width=1)


draw_boxes()
image.save(
    os.path.join(
        parent_dir_nth_times(__file__, 2),
        "docs/examples/fields.png",
    ),
)
