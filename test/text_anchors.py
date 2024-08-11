from PIL import Image, ImageDraw
from rich.pretty import pprint

from imagesmacker.draw import Draw
from imagesmacker.fields import relative_field_formatting
from imagesmacker.models.coordinates import XYWH
from imagesmacker.models.draw import TextConfig
from imagesmacker.models.fields import (
    Fields,
    FieldAttributes,
    FieldsCoords,
    RelativeDataFieldFormat,
    RelativeFieldCell,
    RelativeRow,
)

data_field_fmt_rows = []
fields_text = {}
fields_dict = {}

horizontal_anchors = ['l', 'm', 'r']
vertical_anchors = ['a','m', 'd']

fields_text_config_default = TextConfig(font="arial bold", font_size=100)

image_size = image_width, image_height = (2100, 2970) # A4 size x10
image = Image.new("RGB", (1000, 1000), color="black")

draw = Draw(image)

def walk(
    fields: Fields,
    fields_coords: FieldsCoords,
    fields_text: dict[str, str],
) -> None:
    for field_text in fields_text:
        draw.text(field_text)

for y_anchor in vertical_anchors:
    y_anchor_list = []
    for x_anchor in horizontal_anchors:
        text_anchor = x_anchor + y_anchor
        y_anchor_list.append(RelativeFieldCell(fr=1, name=text_anchor))
        fields_text[text_anchor] = f"{text_anchor} example"
        fields_dict[text_anchor] = FieldAttributes(
            text_config=fields_text_config_default,
        )
    data_field_fmt_rows.append(RelativeRow(fr=1, cells=y_anchor_list))

data_field_fmt = RelativeDataFieldFormat(rows=data_field_fmt_rows)

pprint(data_field_fmt)
pprint(fields_text)

fields = Fields(
    fields=fields_dict,
)

fields_coords = relative_field_formatting(data_field_fmt, XYWH(0, 0, image_width, image_height))

pprint(fields_coords)

# walk(fields, fields_coords, fields_text)