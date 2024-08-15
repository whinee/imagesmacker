from typing import Literal, TypeAlias

from pydantic import BaseModel

TextAnchor: TypeAlias = Literal["lt", "mt", "rt", "lm", "mm", "rm", "lb", "mb", "rb"]


class TextStyle(BaseModel):
    italics: bool = False


class TextConfig(BaseModel):
    font_filepath: str
    font_size: int = 100
    # minimum_font_size: int = 20
    anchor: TextAnchor = "mm"
    # multiline_vertical_anchor: Literal["t", "m", "b"] = "m"
    break_text: bool = False
    line_height: float | int = 1
    inverted: bool = False
    style: TextStyle = TextStyle()
