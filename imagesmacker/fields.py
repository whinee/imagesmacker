from collections import deque

from imagesmacker.models.coordinates import XYXY, RectangleCoordinates
from imagesmacker.models.fields import (
    FieldsCoords,
    RelativeContainer,
    RelativeDataFieldFormat,
    RelativeFieldCell,
    cells_type,
)


def relative_field_formatting(  # noqa: C901
    data_field_format: RelativeContainer | RelativeDataFieldFormat,
    dimensions: RectangleCoordinates,
) -> FieldsCoords:
    """
    Non-recursive version of relative layout formatter using a manual stack.

    Args:
        data_field_format (RelativeDataFieldFormat): Layout tree.
        dimensions (RectangleCoordinates): Bounding box to render in.

    Returns:
        FieldsCoords: Dict of field names to XYXY positions.

    """
    output: FieldsCoords = {}

    x, y, w, h = dimensions.xywh()

    # Stack of layout jobs
    # Each job is: (cells, x, y, w, h, direction)
    stack: deque[
        tuple[RelativeContainer | RelativeDataFieldFormat, float, float, float, float]
    ] = deque()
    stack.append((data_field_format, x, y, w, h))  # root layout

    container: RelativeContainer | RelativeDataFieldFormat
    cells: cells_type

    while stack:
        container, cur_x, cur_y, cur_w, cur_h = stack.pop()
        cells = container.cells
        direction = container.direction

        total_fr = sum(cell.fr for cell in cells)
        horizontal = direction in ("lr", "rl")
        reverse = direction in ("rl", "bt")

        offset = cur_x if horizontal else cur_y
        cells_iter = reversed(cells) if reverse else cells

        for cell in cells_iter:
            frac = cell.fr / total_fr
            size = cur_w * frac if horizontal else cur_h * frac

            if horizontal:
                cell_x = offset
                cell_y = cur_y
                cell_w = size
                cell_h = cur_h
            else:
                cell_x = cur_x
                cell_y = offset
                cell_w = cur_w
                cell_h = size

            if isinstance(cell, RelativeFieldCell):
                output[cell.name] = XYXY(
                    round(cell_x),
                    round(cell_y),
                    round(cell_x + cell_w),
                    round(cell_y + cell_h),
                )
            elif isinstance(cell, RelativeContainer):
                # Push nested job onto stack
                stack.append(
                    (
                        cell,
                        cell_x,
                        cell_y,
                        cell_w,
                        cell_h,
                    ),
                )

            offset += size

    return output
