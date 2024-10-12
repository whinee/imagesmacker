from alltheutils.utils import dnrp
from PIL import Image

from imagesmacker.draw import Draw
from imagesmacker.models.coordinates import XYWH
from imagesmacker.models.draw import QRCodeConfig
from imagesmacker.models.fields import (
    BarcodeFieldAttributes,
)

data = """123456 jump!"""

image_size = image_width, image_height = (500, 500)
image = Image.new("RGB", image_size, color="black")

draw = Draw(image)

field_attributes = BarcodeFieldAttributes(
    barcode_config=QRCodeConfig(),
)

draw.barcode(
    data=data,
    type="QR",
    field_coords=XYWH(50, 50, image_width - 100, image_height - 100),
    field_attributes=field_attributes,
)

image.save(f"{dnrp(__file__, 2)}/docs/examples/QR.png")
