
from alltheutils.utils import half_round


def xywh2xyxy(
    anchor: str | tuple[str, str],
    x: int,
    y: int,
    w: int,
    h: int,
) -> tuple[int, int, int, int]:
    """
    Taking into consideration the given text anchor, convert [x, y, w, h] to [x1, y1, x2, y2].

    | `x-anchor` |    `x1` |    `x2` |
    |-----------:|--------:|--------:|
    | l (left)   |       x |   x + w |
    | m (middle) | x - w/2 | x + w/2 |
    | r (right)  |   x - w |       x |

    |           `y-anchor` |    `y1` |    `y2` |
    |---------------------:|--------:|--------:|
    | a (ascender/top)     |       y |   y + h |
    | m (middle)           | y - h/2 | y + h/2 |
    | d (descender/bottom) |   y - h |       y |

    Args:
    - anchor (`str`): text anchor
    - x (`int`): text's x-coordinate
    - y (`int`): text's y-coordinate
    - w (`int`): text's width
    - h (`int`): text's height

    Returns:
    `tuple[int, int, int, int]`: [x1, y1, x2, y2]
    """

    xa: str
    ya: str
    xa, ya = anchor  # type: ignore[misc]

    match xa:
        case "l":
            x1, x2 = x, x + w
        case "m":
            x1, x2 = x - half_round(w), x + half_round(w)
        case "r":
            x1, x2 = x - w, x

    match ya:
        case "a":
            y1, y2 = y, y + h
        case "m":
            y1, y2 = y - half_round(h), y + half_round(h)
        case "d":
            y1, y2 = y - h, y

    return x1, y1, x2, y2


def xyxy2xywh(
    anchor: str | tuple[str, str],
    x1: int,
    y1: int,
    x2: int,
    y2: int,
) -> tuple[int, int, int, int]:
    """
    Taking into consideration the given text anchor, convert [x1, y1, x2, y2] to [x, y, w, h] (text with x, y coordinate and dimensions of w, h).

    | `x-anchor` |           `x` |     `w` |
    |-----------:|--------------:|--------:|
    | l (left)   |            x1 | x2 - x1 |
    | m (middle) | (x1 + x2) / 2 | x2 - x1 |
    | r (right)  |            x2 | x2 - x1 |

    |           `y-anchor` |           `y` |     `h` |
    |---------------------:|--------------:|--------:|
    | a (ascender/top)     |            y1 | y2 - y1 |
    | m (middle)           | (y1 + y2) / 2 | y2 - y1 |
    | d (descender/bottom) |            y2 | y2 - y1 |

    Args:
    - anchor (`str`): text anchor
    - x1 (`int`): text's x-coordinate of left edge
    - y1 (`int`): text's y-coordinate of top edge
    - x2 (`int`): text's x-coordinate of right edge
    - y2 (`int`): text's y-coordinate of bottom edge

    Returns:
    `tuple[int, int, int, int]`: [x, y, w, h]
    """

    xa: str
    ya: str
    xa, ya = anchor  # type: ignore[misc]

    match xa:
        case "l":
            x = x1
        case "m":
            x = round((x1 + x2) * 0.5)
        case "r":
            x = x2

    match ya:
        case "a":
            y = y1
        case "m":
            y = round((y1 + y2) * 0.5)
        case "d":
            y = y2

    return x, y, x2 - x1, y2 - y1
