# import multiprocessing.dummy as mp
# import os
# from typing import Any


# from imagesmacker.draw import Draw
from imagesmacker.models.coordinates import XYXY, RectangleCoordinates
from imagesmacker.models.fields import (
    FieldsCoords,
    RelativeDataFieldFormat,
)


def relative_field_formatting(
    data_field_format: RelativeDataFieldFormat,
    dimensions: RectangleCoordinates,
) -> FieldsCoords:
    """
    _summary_.

    Args:
        data_field_format (RelativeDataFieldFormat): _description_
        dimensions (Coordinates): Coordinate mode agnostic dimensions.

    Returns:
        dict[str, tuple[float, float, float, float]]: _description_
    """

    initial_field_x, field_y, field_width, field_height = dimensions.xywh()

    total_field_fractional_height: float = 0
    ls_cell_fractional_widths: list[float] = []

    for row in data_field_format.rows:
        total_row_fractional_width: float = 0

        row_fractional_height = row.fr
        row_cells = row.cells

        total_field_fractional_height += row_fractional_height

        for cell in row_cells:
            total_row_fractional_width += cell.fr

        ls_cell_fractional_widths.append(total_row_fractional_width)

    output: dict[str, XYXY] = {}

    for row, total_row_fractional_width in zip(
        data_field_format.rows,
        ls_cell_fractional_widths,
        strict=True,
    ):
        row_fractional_height = row.fr
        row_cells = row.cells

        row_height = round(
            field_height * (row_fractional_height / total_field_fractional_height),
        )

        field_x = initial_field_x

        for cell in row_cells:
            cell_fractional_width = cell.fr
            cell_width = round(
                field_width * (cell_fractional_width / total_row_fractional_width),
            )
            output[cell.name] = XYXY(
                field_x,
                field_y,
                field_x + cell_width,
                field_y + row_height,
            )
            field_x += cell_width
        field_y += row_height

    return output
