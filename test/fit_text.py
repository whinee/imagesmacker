import os

from alltheutils.utils import dnrp
from PIL import Image

from imagesmacker.draw import Draw
from imagesmacker.models.coordinates import XYWH
from imagesmacker.models.draw import TextConfig
from imagesmacker.models.fields import (
    FieldAttributes,
)


def example_one() -> None:
    image_size = image_width, image_height = (500, 500)
    image = Image.new("RGB", image_size, color="black")

    draw = Draw(image)

    text = """Cwoissant OwO"""

    field_attributes = FieldAttributes(
        text_config=TextConfig(
            font_filepath=os.path.join(
                dnrp(__file__, 2),
                "assets/fonts/arial bold.ttf",
            ),
            font_size=100,
            anchor="mm",  # type: ignore
        ),
    )

    draw.text(
        text=text,
        field_coords=XYWH(0, 0, image_width, image_height),
        field_attributes=field_attributes,
    )

    image.save(os.path.join(dnrp(__file__, 2), "docs/examples/fit-1.png"))


def main() -> None:
    example_one()


main()
