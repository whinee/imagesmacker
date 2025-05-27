from collections.abc import Sequence
from typing import Literal, TypeAlias, Union

from pydantic import BaseModel, ConfigDict

from imagesmacker.models.coordinates import XYXY
from imagesmacker.models.draw import BarcodeConfig, TextConfig

cells_type = Sequence[Union["RelativeContainer", "RelativeFieldCell"]]
directions_type = Literal["lr", "rl", "tb", "bt"]


class RelativeFieldCell(BaseModel):
    model_config = ConfigDict(extra="forbid")
    fr: float
    name: str


class RelativeContainer(BaseModel):
    model_config = ConfigDict(extra="forbid")
    fr: float
    cells: cells_type
    direction: str | directions_type = "tb"


class RelativeDataFieldFormat(BaseModel):
    model_config = ConfigDict(extra="forbid")
    cells: cells_type
    direction: str | directions_type = "tb"


class FieldAttributes(BaseModel):
    model_config = ConfigDict(extra="forbid")


class TextFieldAttributes(FieldAttributes):
    model_config = ConfigDict(extra="forbid")
    text_config: TextConfig


class BarcodeFieldAttributes(FieldAttributes):
    model_config = ConfigDict(extra="forbid")
    barcode_config: BarcodeConfig


FieldsCoords: TypeAlias = dict[str, XYXY]
FieldsConfig: TypeAlias = (
    dict[str, TextFieldAttributes] | dict[str, BarcodeFieldAttributes]
)
