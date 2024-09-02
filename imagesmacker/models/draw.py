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
    line_height: float | int = 1.2
    inverted: bool = False
    style: TextStyle = TextStyle()


def validate_text_anchor(anchor: str):
    if len(anchor) != 2:
        raise ValueError("The string must be exactly 2 characters long.")
    anchor_tuple: tuple[str, str] = tuple(anchor)  # type: ignore
    horizontal_anchor, vertical_anchor = anchor_tuple  # type: ignore[misc]
    if horizontal_anchor not in {"l", "m", "r"}:
        raise ValueError(
            "The horizontal anchor must be one of the following: 'l', 'm', or 'r'.",
        )
    if vertical_anchor not in {"t", "m", "b"}:
        raise ValueError(
            "The vertical anchor must be one of the following: 't', 'm', or 'b'.",
        )
