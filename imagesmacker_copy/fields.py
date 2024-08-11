import multiprocessing.dummy as mp
import os
from typing import Any

from PIL import Image

from imagesmacker.draw import Draw

def draw_field(
    draw: Draw,
    field: str,
    text: str,
    *args: list[Any],
    **kwargs: dict[str, Any],
) -> None:
    if fa := FIELDS.get(field):
        if (field == "qr") or fa.pop("qr", False):
            draw.qr(data=text, **fa)
        else:
            draw.text(*args, text=text, **{**fa, **kwargs})  # type: ignore[arg-type, misc]


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


def walk(data: RecursiveDict, tpl: Image, previous: list[str]) -> None:
    op_folder = os.path.join(OUT_PATH, *[i for i in previous if i is not None])
    local_tpl = tpl.copy()

    if isinstance(data, dict):
        for field, fv in data.items():  # type: ignore[assignment]
            draw = Draw(local_tpl)
            draw_field(draw, field, text=fv)  # type: ignore[arg-type, union-attr]
        walk(data["_fields"] if "_fields" in data else data["_ls"], local_tpl, [*previous, data["_name"]])  # type: ignore[arg-type]
    else:
        try:
            os.makedirs(op_folder)
        except FileExistsError:
            pass

        def inner(i: dict[str, str]) -> None:
            ctpl = tpl.copy()
            cdraw = Draw(ctpl)
            name = i.pop("_name", list(i.values())[0])
            for k, v in i.items():
                draw_field(cdraw, k, text=v)
            ctpl.save(os.path.join(op_folder, name + ".png"))

        p = mp.Pool(10)
        p.map(inner, data)
        p.close()
        p.join()
