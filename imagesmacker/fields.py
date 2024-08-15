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


# def draw_field(
#     draw: Draw,
#     field: str,
#     text: str,
#     *args: list[Any],
#     **kwargs: dict[str, Any],
# ) -> None:
#     if fa := FIELDS.get(field):
#         if (field == "qr") or fa.pop("qr", False):
#             draw.qr(data=text, **fa)
#         else:
#             draw.text(*args, text=text, **{**fa, **kwargs})  # type: ignore[arg-type, misc]


# def walk(data: RecursiveDict, tpl: Image, previous: list[str]) -> None:
#     op_folder = os.path.join(OUT_PATH, *previous)

#     ctpl = tpl.copy()
#     cdraw = Draw(ctpl)

#     ls = data.pop('_ls', [])
#     for k, v in data.items():
#         draw_field(cdraw, k, text=v)  # type: ignore

#     def inner(i: dict[str, str]) -> None:
#         name = i.pop("_name", list(i.values())[0])
#         for k, v in i.items():
#             draw_field(cdraw, k, text=v)
#         ctpl.save(os.path.join(op_folder, name + ".png"))

#     p = mp.Pool(10)
#     p.map(inner, ls)
#     p.close()
#     p.join()

# def walk(data: RecursiveDict, tpl: Image, previous: list[str]) -> None:
#     print(OUT_PATH, previous)
#     op_folder = os.path.join(OUT_PATH, *[i for i in previous if i is not None])
#     fields: RecursiveDict
#     if fields := data.get("fields"): # type: ignore[assignment]
#         for field, fv in fields.items(): # type: ignore[assignment]
#             for field_folder, ffv in fv.items(): # type: ignore[union-attrp]
#                 local_tpl = tpl.copy()
#                 draw = Draw(local_tpl)
#                 draw_field(draw, field, text=ffv.get("value", field_folder))  # type: ignore[arg-type, union-attr]
#                 walk(ffv, local_tpl, [*previous, field_folder])  # type: ignore[arg-type]
#     elif ls := data.get("ls"):
#         try:
#             os.makedirs(op_folder)
#         except FileExistsError:
#             pass

#         def inner(i: dict[str, str]) -> None:
#             ctpl = tpl.copy()
#             cdraw = Draw(ctpl)
#             name = i.pop("_name", list(i.values())[0])
#             for k, v in i.items():
#                 draw_field(cdraw, k, text=v)
#             ctpl.save(os.path.join(op_folder, name + ".png"))

#         p = mp.Pool(10)
#         p.map(inner, ls)
#         p.close()
#         p.join()


# def walk(data: RecursiveDict, tpl: Image, previous: list[str]) -> None:
#     op_folder = os.path.join(OUT_PATH, *[i for i in previous if i is not None])
#     local_tpl = tpl.copy()

#     if isinstance(data, dict):
#         for field, fv in data.items():  # type: ignore[assignment]
#             draw = Draw(local_tpl)
#             draw_field(draw, field, text=fv)  # type: ignore[arg-type, union-attr]
#         walk(data["_fields"] if "_fields" in data else data["_ls"], local_tpl, [*previous, data["_name"]])  # type: ignore[arg-type]
#     else:
#         try:
#             os.makedirs(op_folder)
#         except FileExistsError:
#             pass

#         def inner(i: dict[str, str]) -> None:
#             ctpl = tpl.copy()
#             cdraw = Draw(ctpl)
#             name = i.pop("_name", list(i.values())[0])
#             for k, v in i.items():
#                 draw_field(cdraw, k, text=v)
#             ctpl.save(os.path.join(op_folder, name + ".png"))

#         p = mp.Pool(10)
#         p.map(inner, data)
#         p.close()
#         p.join()
