from typing import TypeAlias

from pydantic import BaseModel, ConfigDict

from imagesmacker.models.coordinates import XYXY
from imagesmacker.models.draw import BarcodeConfig, TextConfig


class RelativeFieldCell(BaseModel):
    model_config = ConfigDict(extra="forbid")
    fr: float
    name: str


class RelativeRow(BaseModel):
    model_config = ConfigDict(extra="forbid")
    fr: float
    cells: list[RelativeFieldCell]


class RelativeDataFieldFormat(BaseModel):
    model_config = ConfigDict(extra="forbid")
    rows: list[RelativeRow]


class FieldAttributes(BaseModel):
    pass


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
