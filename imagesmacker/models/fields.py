from typing import TypeAlias

from pydantic import BaseModel

from imagesmacker.models.coordinates import XYXY
from imagesmacker.models.draw import BarcodeConfig, TextConfig


class RelativeFieldCell(BaseModel):
    fr: float
    name: str


class RelativeRow(BaseModel):
    fr: float
    cells: list[RelativeFieldCell]


class RelativeDataFieldFormat(BaseModel):
    rows: list[RelativeRow]


class FieldAttributes(BaseModel):
    pass


class TextFieldAttributes(FieldAttributes):
    text_config: TextConfig


class BarcodeFieldAttributes(FieldAttributes):
    barcode_config: BarcodeConfig


FieldsCoords: TypeAlias = dict[str, XYXY]
FieldsConfig: TypeAlias = (
    dict[str, TextFieldAttributes] | dict[str, BarcodeFieldAttributes]
)
