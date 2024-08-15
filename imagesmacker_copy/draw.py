import os
from textwrap import wrap
from typing import Any, Optional, Union

from alltheutils.cfg import rcfg
from alltheutils.types import Kwargs
from alltheutils.utils import dnrp
from PIL import Image, ImageDraw
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.main import QRCode

from imagesmacker.fonts import font_loader, font_size_fn
from imagesmacker.utils import xywh2xyxy_text, xyxy2xywh_text

RecursiveDict = dict[str, Union[str, list["RecursiveDict"], "RecursiveDict"]]

CFG = rcfg(os.path.join(dnrp(__file__, 3), "cfg", "main.yml"))

FILES = CFG["files"]

FONTS_PATH = os.path.join(dnrp(__file__, 3), FILES["fonts"])
OUT_PATH = os.path.join(dnrp(__file__, 3), FILES["out"])


def qr(data: str, box_size: int = 20, border: int = 1, **kwargs) -> StyledPilImage:
    qr = QRCode(
        border=border,
        box_size=box_size,
    )
    qr.add_data(data)
    qr.make(fit=True)
    return qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
    )


class Draw:
    def __init__(self, img: Image.Image) -> None:
        self.img = img
        self.draw = ImageDraw.Draw(img)

    def text(
        self,
        type_coords_tuple: tuple[str, int, int, int, int],
        text: str,
        font: str,
        anchor: str = "mm",
        max_font_size: float | int = 100,
        breaktext: Optional[bool] = None,
        line_height: float | int = 1,
        inverted: bool = False,
        style: Optional[dict[str, Any]] = None,
        **kwargs: Any,
    ) -> None:
        """
        Text.

        Args:
            type_coords_tuple (tuple[str, int, int, int, int]): _description_
            text (str): _description_
            font (str): _description_
            anchor (str, optional): _description_. Defaults to "mm".
            max_font_size (float | int, optional): _description_. Defaults to 100.
            breaktext (Optional[bool], optional): _description_. Defaults to None.
            line_height (float | int, optional): _description_. Defaults to 1.
            inverted (bool, optional): _description_. Defaults to False.
            style (Optional[dict[str, Any]], optional): _description_. Defaults to None.

        Raises:
            Exception: _description_
            Exception: _description_
        """
        if breaktext is None:
            breaktext = False

        if not text:
            return

        xa: str
        ya: str
        mlva_ls: list[str]

        text = str(text).strip()
        coords_type, *coords = type_coords_tuple
        xa, ya, *mlva_ls = anchor  # type: ignore[misc] # multi line vertical anchor list
        slas: str = xa + ya  # type: ignore[misc] # single line anchor set

        if len(mlva_ls) > 1:
            raise Exception(
                "Anchor for multiline text should not exceed three characters.",
            )

        if coords_type == "xyxy":
            # left-most x-coordinate, highest y-coordinate, right-most x-coordinate, lowest y-coordinate
            x1, y1, x2, y2 = coords
            # field starting x-coordinate, field starting y-coordinate, field width, field height
            fx, fy, fw, fh = xyxy2xywh_text(slas, x1, y1, x2, y2)
        elif coords_type == "xywh":
            fx, fy, fw, fh = coords
            x1, y1, x2, y2 = xywh2xyxy_text(slas, fx, fy, fw, fh)

        tfs = font_size_fn(
            self.draw,
            font,
            (fx, fy),
        )  # true font size # type: ignore[arg-type]

        text_sls: str | list[str] = text  # text: string or list

        max_font_size = int(max_font_size)

        if ("\n" in text) or breaktext:
            if len(mlva_ls) == 0:
                mlva = "m"
            else:
                mlva = mlva_ls[0]
            while True:
                tw = 0
                tw_ls = []
                th_ls = []

                tt = text.splitlines()
                for i in tt:
                    tw += tfs(max_font_size, i)[0]
                ml = max(len(i) for i in tt)
                cpfw = round(fw / (tfs(max_font_size, text)[0] / ml))

                tt = [j for i in tt for j in wrap(i, cpfw)]
                ltt = len(tt)

                for i in tt:
                    twi, thi = tfs(max_font_size, i)
                    tw_ls.append(twi)
                    th_ls.append(thi)

                tw = max(tw_ls)
                th = round(ltt * line_height * (sum(th_ls) / ltt))
                if (tw > fw) or (th > fh):
                    max_font_size -= 1
                else:
                    text_sls = tt
                    break
        else:
            if len(mlva_ls) > 0:
                raise Exception(
                    "Anchor for single line text should not exceed two characters.",
                )
            tw, th = tfs(max_font_size, text)
            if (tw > fw) or (th > fh):
                while True:
                    max_font_size -= 1
                    tw, th = tfs(max_font_size, text)
                    if (tw <= fw) and (th <= fh):
                        break

        if inverted:
            hth = round(th / 2)  # halved text height
            lhth = th - hth  # large half of the text height
            fh += th
            it = Image.new("RGBA", (fw, fh), color=(0, 0, 0, 0))
            itd = ImageDraw.Draw(it)

            match xa:
                case "l":
                    slas = "r" + ya
                    fx = fw
                case "m":
                    fx = round(fw / 2)
                case "r":
                    slas = "l" + ya
                    fx = 0

            match ya:
                case "a":
                    fy = fh - th - lhth
                case "m":
                    fy: int = round(fh / 2)  # type: ignore[no-redef]
                case "d":
                    fy = th + lhth
        else:
            itd = self.draw

        text_kwargs = {
            "anchor": slas,
            "fill": kwargs.pop("fill"),
            "font": font_loader(font=font, size=max_font_size),  # type: ignore[arg-type, misc]
            **kwargs,
        }

        if isinstance(text_sls, list):
            tholtt = th / ltt

            match mlva:
                case "a":
                    vertical_additive: float = fh - th if inverted else y1
                case "m":
                    vertical_additive = (
                        (fh - th) / 2 if inverted else y1 + ((fh - th) / 2)
                    )
                case "d":
                    vertical_additive = 0 if inverted else y1 + fh - th

            for t, ty in zip(
                text_sls,
                range(round(tholtt / 2), th, round(tholtt)),
                strict=True,
            ):
                itd.text(text=t, xy=(fx, vertical_additive + ty), **text_kwargs)
        else:
            itd.text(text=text_sls, xy=(fx, fy), **text_kwargs)

        if inverted:
            it = it.rotate(180)
            self.img.paste(it, (x1, y1 - lhth, x2, y2 + hth), it)

    def qr(
        self,
        type_coords_tuple: tuple[str, int, int, int, int],
        data: str,
        **kwargs: Kwargs,
    ) -> None:
        coords_type, *coords = type_coords_tuple
        if coords_type == "xyxy":
            # left-most x-coordinate, highest y-coordinate, right-most x-coordinate, lowest y-coordinate
            x1, y1, x2, y2 = coords
        elif coords_type == "xywh":
            fx, fy, fw, fh = coords
            x1, y1, x2, y2 = xywh2xyxy_text("mm", fx, fy, fw, fh)

        w = x2 - x1
        h = y2 - y1

        if w > h:
            x1 = x2 - h
            x2 = x1 + h
            w = h
        else:
            y1 = y2 - w
            y2 = y1 + w
            h = w

        coords = [x1, y1, x2, y2]

        self.img.paste(
            qr(data, **kwargs).resize((w, h), Image.Resampling.LANCZOS), coords,
        )
