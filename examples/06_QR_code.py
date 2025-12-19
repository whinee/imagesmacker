from alltheutils.utils import parent_dir_nth_times
from PIL import Image

from imagesmacker.draw import Draw
from imagesmacker.models.coordinates import XYWH
from imagesmacker.models.draw import BarcodeConfig, FieldConfig, QRCodeConfig

data = """https://go.kde.org/endof10"""

image_size = image_width, image_height = (500, 500)
image = Image.new("RGB", image_size, color="#FCF9DE")

draw = Draw(image)

field_attributes = FieldConfig(
    barcode=BarcodeConfig(
        qr=QRCodeConfig(background_color="#FCF9DE"),
    ),
)

margin = 0
margin_x2 = margin * 2

draw.draw(
    data=data,
    type="barcode.qr",
    field_coords=XYWH(
        margin,
        margin,
        image_width - margin_x2,
        image_height - margin_x2,
    ),
    field_attributes=field_attributes,
)

image.save(f"{parent_dir_nth_times(__file__, 2)}/docs/examples/QR.png")
