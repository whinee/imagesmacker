import os
from collections.abc import Callable
from typing import Any

from PIL import ImageDraw, ImageFont
from PIL.ImageFont import FreeTypeFont


def ttf(
    font: str,
    size: int = 10,
) -> FreeTypeFont:
    return ImageFont.truetype(os.path.join("assets/fonts", font) + ".ttf", size)


def font_size_fn(
    draw: ImageDraw.ImageDraw,
    font: str,
    xy: tuple[int, int],
    **kwargs: dict[str, Any],
) -> Callable[..., list[int]]:
    def inner(size: int, text: str) -> list[int]:
        x1, y1, x2, y2 = draw.multiline_textbbox(
            xy=xy,
            text=text,
            font=ttf(font, size),
            **kwargs,
        )
        return [x2 - x1, y2 - y1]

    return inner
