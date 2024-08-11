from typing import Literal

from pydantic import BaseModel


class TextStyle(BaseModel):
    italics: bool = False

class TextConfig(BaseModel):
    font: str
    anchor: Literal['la', 'ma', 'ra', 'lm', 'mm', 'rm', 'ld', 'md', 'rd'] = "mm"
    multiline_vertical_anchor: Literal['a', 'm', 'd'] = 'm'
    font_size: float | int = 100
    break_text: bool = False
    line_height: float | int = 1
    inverted: bool = False
    style: TextStyle = TextStyle()