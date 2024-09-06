from typing import Any, Literal, Optional, TypeAlias

from PIL.ImageDraw import _Ink
from pydantic import BaseModel, ConfigDict

TextAnchor: TypeAlias = Literal["lt", "mt", "rt", "lm", "mm", "rm", "lb", "mb", "rb"]


class TextStyle(BaseModel):
    model_config = ConfigDict(extra="forbid")
    fill: _Ink = "#000"
    italics: bool = False  # not in use
    underline: bool = False  # not in use


class TextConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")
    font_filepath: str
    font_size: int = 100
    anchor: TextAnchor = "mm"
    break_text: bool = False
    line_height: float | int = 1.2
    inverted: bool = False
    style: TextStyle = TextStyle()


class BarcodeConfig(BaseModel):
    pass


class Code128Config(BarcodeConfig):
    model_config = ConfigDict(extra="forbid")
    options: Optional[dict[str, Any]] = None


class QRCodeConfig(BarcodeConfig):
    model_config = ConfigDict(extra="forbid")
    box_size: int = 20
    border: int = 1


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
