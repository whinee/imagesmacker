import os

from alltheutils.utils import file_exists
from PIL import ImageDraw, ImageFont
from PIL.ImageFont import FreeTypeFont


def font_loader(
    filepath: str,
    size: int = 10,
) -> FreeTypeFont:
    filepath = os.path.abspath(filepath)
    return ImageFont.truetype(file_exists(filepath), size)


class FontSizeCalculator:
    def __init__(
        self,
        draw: ImageDraw.ImageDraw,
        font: str,
    ) -> None:
        """
        Initialize the FontSizeCalculator class.

        Args:
        - draw (`ImageDraw.ImageDraw`): The ImageDraw object to use for text measurement.
        - font (`str`): The font name or path to use.
        - kwargs (`dict[str, Any]`): Additional keyword arguments.
        """
        self.draw = draw
        self.font = font

    def get_text_bbox(self, size: int, text: str) -> tuple[int, int]:
        """
        Get the width and height of the text for a given font size.

        Args:
        - size (`int`): The font size to measure.
        - text (`str`): The text string to measure.

        Returns:
        `list[int]`: A list containing the width and height of the text.
        """
        x1, y1, x2, y2 = self.draw.multiline_textbbox(
            xy=(0, 0),
            text=text,
            font=font_loader(self.font, size),
        )
        return (x2 - x1, y2 - y1)
