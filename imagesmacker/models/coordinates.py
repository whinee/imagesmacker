import abc
from collections.abc import Iterator
from typing import NamedTuple, cast


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

    @abc.abstractmethod
    def xyxy(self) -> XYXYNamedTuple:
        pass

    @abc.abstractmethod
    def xywh(self) -> XYWHNamedTuple:
        pass

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


class XYXY(Coordinates):
    def __init__(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.coords = XYXYNamedTuple(x1=x1, y1=y1, x2=x2, y2=y2)

    def xyxy(self) -> XYXYNamedTuple:
        return cast(XYXYNamedTuple, self.coords)

    def xywh(self) -> XYWHNamedTuple:
        x1, y1, x2, y2 = self.coords
        return XYWHNamedTuple(x=x1, y=y1, w=x2 - x1, h=y2 - y1)


class XYWH(Coordinates):
    def __init__(self, x: int, y: int, w: int, h: int) -> None:
        self.coords = XYWHNamedTuple(x=x, y=y, w=w, h=h)

    def xyxy(self) -> XYXYNamedTuple:
        x, y, w, h = self.coords
        return XYXYNamedTuple(x1=x, y1=y, x2=x + w, y2=y + h)

    def xywh(self) -> XYWHNamedTuple:
        return cast(XYWHNamedTuple, self.coords)
