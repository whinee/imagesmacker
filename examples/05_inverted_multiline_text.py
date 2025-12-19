from alltheutils.utils import parent_dir_nth_times
from PIL import Image

from imagesmacker.draw import Draw
from imagesmacker.models.coordinates import XYWH
from imagesmacker.models.draw import FieldConfig, TextConfig, TextStyle

text = """Address: #19 Lo St., Breezy Hills,
Brgy. San Roque, Quezon City, Metro Manila"""

image_size = image_width, image_height = (500, 500)
image = Image.new("RGB", image_size, color="black")

draw = Draw(image)

field_attributes = FieldConfig(
    text=TextConfig(
        font=f"{parent_dir_nth_times(__file__, 2)}/assets/fonts/arial bold.ttf",
        max_font_size=100,
        anchor="mm",
        inverted=True,
        break_text=True,
        style=TextStyle(fill="#fff"),
    ),
)

margin = 25
margin_x2 = margin * 2

draw.draw(
    type="text",
    data=text,
    field_coords=XYWH(
        margin,
        margin,
        image_width - margin_x2,
        image_height - margin_x2,
    ),
    field_attributes=field_attributes,
)

image.save(
    f"{parent_dir_nth_times(__file__, 2)}/docs/examples/inverted-multiline-mm.png",
)
