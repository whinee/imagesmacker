import os

from alltheutils.utils import dnrp
from PIL import Image, ImageDraw

from imagesmacker.draw import Draw
from imagesmacker.fields import relative_field_formatting
from imagesmacker.models.coordinates import XYWH
from imagesmacker.models.draw import TextConfig
from imagesmacker.models.fields import (
    FieldsConfig,
    FieldsCoords,
    RelativeDataFieldFormat,
    RelativeFieldCell,
    RelativeRow,
    TextFieldAttributes,
)

data_field_fmt_rows = []
fields_text = {}
fields_config = {}

horizontal_anchors = ["l", "m", "r"]
vertical_anchors = ["t", "m", "b"]

image_size = image_width, image_height = [
    i * 5 for i in (297, 210)
]  # landscape A4 size x5
image = Image.new("RGB", image_size, color="black")

draw = ImageDraw.Draw(image)
smack_draw = Draw(image)

text = """The quick brown fox jumps over the lazy dog"""


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


for y_anchor in vertical_anchors:
    y_anchor_list = []
    for x_anchor in horizontal_anchors:
        text_anchor = x_anchor + y_anchor
        y_anchor_list.append(RelativeFieldCell(fr=1, name=text_anchor))
        fields_text[text_anchor] = text
        fields_config[text_anchor] = TextFieldAttributes(
            text_config=TextConfig(
                font_filepath=os.path.join(
                    dnrp(__file__, 2),
                    "assets/fonts/arial bold.ttf",
                ),
                font_size=50,
                anchor=text_anchor,  # type: ignore
                break_text=True,
            ),
        )
    data_field_fmt_rows.append(RelativeRow(fr=1, cells=y_anchor_list))

data_field_fmt = RelativeDataFieldFormat(rows=data_field_fmt_rows)

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
image.save(os.path.join(dnrp(__file__, 2), "docs/examples/text-anchors-multiline.png"))
