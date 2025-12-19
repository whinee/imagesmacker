from alltheutils.utils import parent_dir_nth_times
from PIL import Image

from imagesmacker.draw import Draw
from imagesmacker.models.coordinates import XYWH
from imagesmacker.models.draw import FieldConfig, ImageConfig

data = "assets/images/cess/500x500-lyra-cropped.png"

image_size = image_width, image_height = (500, 500)
image = Image.new("RGB", image_size, color="black")

draw = Draw(image)

field_attributes = FieldConfig(
    image=ImageConfig(),
)

margin = 25
margin_x2 = margin * 2

draw.draw(
    type="image",
    data=data,
    field_coords=XYWH(
        margin,
        margin,
        image_width - margin_x2,
        image_height - margin_x2,
    ),
    field_attributes=field_attributes,
)

image.save(f"{parent_dir_nth_times(__file__, 2)}/docs/examples/image-placement.png")
