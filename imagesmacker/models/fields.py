from typing import TypeAlias

from pydantic import BaseModel

from imagesmacker.models.coordinates import XYXY
from imagesmacker.models.draw import TextConfig

FieldsCoords: TypeAlias = dict[str, XYXY]

class RelativeFieldCell(BaseModel):
    fr: float
    name: str


class RelativeRow(BaseModel):
    fr: float
    cells: list[RelativeFieldCell]


class RelativeDataFieldFormat(BaseModel):
    rows: list[RelativeRow]

class FieldAttributes(BaseModel):
    text_config: TextConfig

class Fields(BaseModel):
    fields: dict[str, FieldAttributes]