from collections.abc import Sequence
from typing import Literal, TypeAlias, Union

from pydantic import BaseModel, ConfigDict

from imagesmacker.models.coordinates import XYXY

cells_type: TypeAlias = Sequence[Union["RelativeContainer", "RelativeFieldCell"]]
directions_type: TypeAlias = Literal["lr", "rl", "tb", "bt"]
cell_variant_types: TypeAlias = Literal["text", "barcode.code128", "barcode.qr"]


class RelativeFieldCell(BaseModel):
    model_config = ConfigDict(extra="forbid")
    fr: float
    name: str
    variant: str | cell_variant_types = "text"


class RelativeContainer(BaseModel):
    model_config = ConfigDict(extra="forbid")
    fr: float
    cells: cells_type
    direction: str | directions_type = "tb"


class RelativeDataFieldFormat(BaseModel):
    model_config = ConfigDict(extra="forbid")
    cells: cells_type
    direction: str | directions_type = "tb"


FieldsCoords: TypeAlias = dict[str, XYXY]
