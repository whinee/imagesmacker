import abc
from collections.abc import Iterator
from typing import Literal, NamedTuple, TypeAlias, cast

from imagesmacker.models.draw import TextAnchor, validate_text_anchor


class XYNamedTuple(NamedTuple):
    x: int
    y: int


class WHNamedTuple(NamedTuple):
    w: int
    h: int


class XYXYNamedTuple(NamedTuple):
    x1: int
    y1: int
    x2: int
    y2: int


class XYWHNamedTuple(NamedTuple):
    x: int
    y: int
    w: int
    h: int


class Coordinates(metaclass=abc.ABCMeta):
    coords: NamedTuple

    def __iter__(self) -> Iterator[int]:
        return iter(self.coords)

    def __str__(self) -> str:
        return str(self.tuple())

    def __repr__(self) -> str:
        return repr(self.coords)

    def list(self) -> list[int]:
        return list(self.coords)

    def tuple(self) -> tuple[int, int]:
        return cast(tuple[int, int], tuple(self.coords))

    def dict(self) -> dict[str, int]:
        return self.coords._asdict()


class RectangleCoordinates(metaclass=abc.ABCMeta):
    """
    Rectangle Coordinates.

    You can have an `xyxy` or `xywh` mode coordinates and it can be read by any
    methods that knows how to read `RectangleCoordinates`.

    Args:
        metaclass (_type_, optional): _description_. Defaults to abc.ABCMeta.

    """

    coords: NamedTuple

    @abc.abstractmethod
    def xyxy(self) -> XYXYNamedTuple:
        pass

    @abc.abstractmethod
    def xywh(self) -> XYWHNamedTuple:
        pass

    def text_coordinates(  # noqa: C901
        self,
        anchor: TextAnchor = "mm",
    ) -> tuple[int, int]:
        """
        `RectangleCoordinates` is often used as.

        Args:
        - anchor (`TextAnchor`, optional): _description_. Defaults to `"mm"`.

        Returns:
        `tuple[int, int]`: _description_

        """
        validate_text_anchor(anchor)
        x1, y1, x2, y2 = self.xyxy()
        horizontal_anchor, vertical_anchor = anchor  # type: ignore

        match horizontal_anchor:
            case "l":
                x = x1
            case "m":
                x = round((x1 + x2) / 2)
            case "r":
                x = x2

        match vertical_anchor:
            case "t":
                y = y1
            case "m":
                y = round((y1 + y2) / 2)
            case "b":
                y = y2

        return (x, y)

    def __iter__(self) -> Iterator[int]:
        return iter(self.coords)

    def __str__(self) -> str:
        return str(self.tuple())

    def __repr__(self) -> str:
        return repr(self.coords)

    def list(self) -> list[int]:
        return list(self.coords)

    def tuple(self) -> tuple[int, int, int, int]:
        return cast(tuple[int, int, int, int], tuple(self.coords))

    def dict(self) -> dict[str, int]:
        return self.coords._asdict()


class XY(Coordinates):
    def __init__(self, x: int, y: int) -> None:
        if x < 0:
            raise ValueError("x must be greater than or equal to zero.")
        if y < 0:
            raise ValueError("y must be greater than or equal to zero.")
        self.coords = XYNamedTuple(x=x, y=y)

    def xy(self) -> XYNamedTuple:
        return cast(XYNamedTuple, self.coords)


class WH(Coordinates):
    def __init__(self, w: int, h: int) -> None:
        if w < 0:
            raise ValueError("w must be greater than or equal to zero.")
        if h < 0:
            raise ValueError("h must be greater than or equal to zero.")
        self.coords = WHNamedTuple(w=w, h=h)

    def wh(self) -> WHNamedTuple:
        return cast(WHNamedTuple, self.coords)


class XYXY(RectangleCoordinates):
    def __init__(self, x1: int, y1: int, x2: int, y2: int) -> None:
        if x1 >= x2:
            raise ValueError("x2 must be greater than x1.")
        if y1 >= y2:
            raise ValueError("y2 must be greater than y1.")
        if x1 < 0:
            raise ValueError("x1 must be greater than or equal to zero.")
        if y1 < 0:
            raise ValueError("y1 must be greater than or equal to zero.")
        self.coords = XYXYNamedTuple(x1=x1, y1=y1, x2=x2, y2=y2)

    def xyxy(self) -> XYXYNamedTuple:
        return cast(XYXYNamedTuple, self.coords)

    def xywh(self) -> XYWHNamedTuple:
        """
        Convert `XYXYNamedTuple` to `XYWHNamedTuple`.

        Returns:
        `XYWHNamedTuple`

        """

        x1, y1, x2, y2 = self.coords
        return XYWHNamedTuple(x=x1, y=y1, w=x2 - x1, h=y2 - y1)


class XYWH(RectangleCoordinates):
    def __init__(self, x: int, y: int, w: int, h: int) -> None:
        if not (w > 0):
            raise ValueError("width must be greater than zero.")
        if not (h > 0):
            raise ValueError("height must be greater than zero.")
        if x < 0:
            raise ValueError("x must be greater than or equal to zero.")
        if y < 0:
            raise ValueError("y must be greater than or equal to zero.")
        self.coords = XYWHNamedTuple(x=x, y=y, w=w, h=h)

    def xyxy(self) -> XYXYNamedTuple:
        """
        Convert `XYWHNamedTuple` to `XYXYNamedTuple`.

        Returns:
        `XYXYNamedTuple`

        """

        x, y, w, h = self.coords

        return XYXYNamedTuple(x1=x, y1=y, x2=x + w, y2=y + h)

    def xywh(self) -> XYWHNamedTuple:
        return cast(XYWHNamedTuple, self.coords)


coordinates_type_alias: TypeAlias = Literal["XY", "WH"]
rectangle_coordinates_type_alias: TypeAlias = Literal["XYXY", "XYWH"]
