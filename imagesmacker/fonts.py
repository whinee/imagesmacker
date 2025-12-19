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
        img_draw: ImageDraw.ImageDraw,
        font_path: str,
    ) -> None:
        """
        Initialize the FontSizeCalculator class.

        Args:
        - draw (`ImageDraw.ImageDraw`): The ImageDraw object to use for text measurement.
        - font_path (`str`): The font path to use.
        - kwargs (`dict[str, Any]`): Additional keyword arguments.

        """
        self.img_draw = img_draw
        self.font_path = font_path

    def get_multiline_baseline_bbox(self, size: int, text: str) -> tuple[int, int]:
        """
        Returns a baseline-aware bounding box for multiline text.

        Baseline of the FIRST line is at y = 0.

        top = -ascent_of_first_line
        bottom = (sum of all line heights) + spacing*(n_lines-1) - ascent_of_first_line

        Args:
        - size (`int`): The font size to measure.
        - text (`str`): The text string to measure.

        Returns:
        `list[int]`: A list containing the width and height of the text.

        """

        font = font_loader(self.font_path, size)

        lines = text.split("\n")
        ascent, descent = font.getmetrics()

        # Width = max width of any line
        widths = [font.getsize(line)[0] for line in lines]

        # x1, y1, x2, y2 = self.img_draw.multiline_textbbox(
        #     xy=(0, 0),
        #     text=text,
        #     font=font_loader(self.font_path, size),
        # )

        max_width = max(widths)

        # Height per line = ascent + descent
        line_height = ascent + descent

        # Total height
        total_height = (line_height * len(lines)) + (spacing * (len(lines) - 1))

        return (max_width, total_height - ascent)
