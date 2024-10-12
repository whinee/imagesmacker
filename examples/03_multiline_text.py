from alltheutils.utils import dnrp
from PIL import Image

from imagesmacker.draw import Draw
from imagesmacker.models.coordinates import XYWH
from imagesmacker.models.draw import TextConfig, TextStyle
from imagesmacker.models.fields import (
    TextFieldAttributes,
)

text = """Address: #19 Lo St., Breezy Hills,
Brgy. San Roque, Quezon City, Metro Manila"""

image_size = image_width, image_height = (500, 500)
image = Image.new("RGB", image_size, color="black")

draw = Draw(image)

field_attributes = TextFieldAttributes(
    text_config=TextConfig(
        font_filepath=f"{dnrp(__file__, 2)}/assets/fonts/arial bold.ttf",
        font_size=50,
        anchor="mm",
        style=TextStyle(fill="#fff"),
    ),
)

draw.text(
    text=text,
    field_coords=XYWH(50, 50, image_width - 100, image_height - 100),
    field_attributes=field_attributes,
)

image.save(f"{dnrp(__file__, 2)}/docs/examples/multiline-mm.png")
