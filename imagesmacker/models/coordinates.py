import abc
from collections.abc import Iterator
from itertools import combinations
from math import sqrt
from typing import Literal, NamedTuple, TypeAlias, cast

from imagesmacker.models.draw import Anchor, validate_text_anchor


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


class FourXYNamedTuple(NamedTuple):
    xy1: XYNamedTuple
    xy2: XYNamedTuple
    xy3: XYNamedTuple
    xy4: XYNamedTuple


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

    """

    coordinates: NamedTuple
    w: int
    h: int

    @abc.abstractmethod
    def xyxy(self) -> XYXYNamedTuple:
        pass

    @abc.abstractmethod
    def xywh(self) -> XYWHNamedTuple:
        pass

    def fourxy(self) -> FourXYNamedTuple:
        """
        Convert `XYWHNamedTuple` to `FourXYNamedTuple`.

        Returns:
        `FourXYNamedTuple`

        """
        
        x1, y1, x2, y2 = self.xyxy()
        xy1 = XYNamedTuple(x=x1, y=y1)
        xy2 = XYNamedTuple(x=x2, y=y1)
        xy3 = XYNamedTuple(x=x2, y=y2)
        xy4 = XYNamedTuple(x=x1, y=y2)
        return FourXYNamedTuple(xy1=xy1, xy2=xy2, xy3=xy3, xy4=xy4)

    def wh(self) -> WHNamedTuple:
        return WHNamedTuple(w=self.w, h=self.h)

    def anchor_coordinates(  # noqa: C901
        self,
        anchor: Anchor = "mm",
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
        return iter(self.coordinates)

    def __str__(self) -> str:
        return str(self.tuple())

    def __repr__(self) -> str:
        return repr(self.coordinates)

    def list(self) -> list[int]:
        return list(self.coordinates)

    def tuple(self) -> tuple:
        return tuple(self.coordinates)

    def dict(self) -> dict[str, int]:
        return self.coordinates._asdict()


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
        self.coordinates = XYXYNamedTuple(x1=x1, y1=y1, x2=x2, y2=y2)
        self.w = x2 - x1
        self.h = y2 - y1

    def xyxy(self) -> XYXYNamedTuple:
        return cast(XYXYNamedTuple, self.coordinates)

    def xywh(self) -> XYWHNamedTuple:
        """
        Convert `XYXYNamedTuple` to `XYWHNamedTuple`.

        Returns:
        `XYWHNamedTuple`

        """

        x1, y1, *_ = self.coordinates
        return XYWHNamedTuple(x=x1, y=y1, w=self.w, h=self.h)


    def fourxy(self) -> FourXYNamedTuple:
        """
        Convert `XYXYNamedTuple` to `FourXYNamedTuple`.

        Returns:
        `FourXYNamedTuple`

        """

        x1, y1, x2, y2 = self.xyxy()
        xy1 = XYNamedTuple(x=x1, y=y1)
        xy2 = XYNamedTuple(x=x2, y=y1)
        xy3 = XYNamedTuple(x=x2, y=y2)
        xy4 = XYNamedTuple(x=x1, y=y2)
        return FourXYNamedTuple(xy1=xy1, xy2=xy2, xy3=xy3, xy4=xy4)


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
        self.coordinates = XYWHNamedTuple(x=x, y=y, w=w, h=h)
        self.w = w
        self.h = h

    def xyxy(self) -> XYXYNamedTuple:
        """
        Convert `XYWHNamedTuple` to `XYXYNamedTuple`.

        Returns:
        `XYXYNamedTuple`

        """

        x, y, w, h = self.coordinates
        return XYXYNamedTuple(x1=x, y1=y, x2=x + w, y2=y + h)

    def xywh(self) -> XYWHNamedTuple:
        return cast(XYWHNamedTuple, self.coordinates)


def distances_squared(a: XYNamedTuple, b: XYNamedTuple) -> int:
    dx = b.x - a.x
    dy = b.y - a.y
    return dx*dx + dy*dy


class FourXY(RectangleCoordinates):
    coordinates: FourXYNamedTuple
    def __init__(
        self,
        xy1: XYNamedTuple,
        xy2: XYNamedTuple,
        xy3: XYNamedTuple,
        xy4: XYNamedTuple,
    ) -> None:
        points = [xy1, xy2, xy3, xy4]

        # 1. Distinct points
        if len({(p.x, p.y) for p in points}) != 4:
            raise ValueError("Points must be distinct.")

        # 2. All pairwise distances
        distances = sorted(distances_squared(a, b) for a, b in combinations(points, 2))

        # Rectangle has:
        # - 4 equal short edges
        # - 2 equal long diagonals
        if distances[0] == 0:
            raise ValueError("Degenerate rectangle.")

        if not (
            distances[0] == distances[1] == distances[2] == distances[3] and
            distances[4] == distances[5]
        ):
            raise ValueError("Points do not form a rectangle.")

        # 3. Derive width & height
        side = sqrt(distances[0])
        other = sqrt(distances[2])  # same bucket
        # diag = sqrt(distances[5])

        # width & height are the two side lengths
        self.w = int(side)
        self.h = int(other)

        self.coordinates = FourXYNamedTuple( # type: ignore
            xy1=xy1, xy2=xy2, xy3=xy3, xy4=xy4,
        )

    def _is_axis_aligned(self) -> bool:
        xs = {p.x for p in (self.coordinates.xy1, self.coordinates.xy2,
                            self.coordinates.xy3, self.coordinates.xy4)}
        ys = {p.y for p in (self.coordinates.xy1, self.coordinates.xy2,
                            self.coordinates.xy3, self.coordinates.xy4)}
        return len(xs) == 2 and len(ys) == 2

    def xyxy(self) -> XYXYNamedTuple:
        if not self._is_axis_aligned():
            raise ValueError("FourXY is not axis-aligned.")

        xs = [p.x for p in [self.coordinates.xy1, self.coordinates.xy2,
            self.coordinates.xy3, self.coordinates.xy4]]
        ys = [p.y for p in [self.coordinates.xy1, self.coordinates.xy2,
            self.coordinates.xy3, self.coordinates.xy4]]

        return XYXYNamedTuple(
            x1=min(xs),
            y1=min(ys),
            x2=max(xs),
            y2=max(ys),
        )

    def xywh(self) -> XYWHNamedTuple:
        """
        Convert `XYXYNamedTuple` to `XYWHNamedTuple`.

        Returns:
        `XYWHNamedTuple`

        """

        x1, y1, *_ = self.xyxy()
        return XYWHNamedTuple(x=x1, y=y1, w=self.w, h=self.h)

    def fourxy(self) -> FourXYNamedTuple:
        return self.coordinates


coordinates_type_alias: TypeAlias = Literal["XY", "WH"]
rectangle_coordinates_type_alias: TypeAlias = Literal["XYXY", "XYWH", "FourXY"]
