import math
from typing import Optional, overload

from imagesmacker.models.coordinates import WH, XY, XYXY, RectangleCoordinates


def rect_coords_middle_point(
    coordinates: RectangleCoordinates,
) -> tuple[int, int]:
    x1, y1, x2, y2 = coordinates.xyxy()
    return (x2 - x1, y2 - y1)


@overload
def scale_and_center_rect(
    br_coords: RectangleCoordinates,
    sr_wh: tuple[int, int],
) -> XYXY:
    pass


@overload
def scale_and_center_rect(
    br_coords: RectangleCoordinates,
    sr_wh: tuple[int, int],
    angle: float | int,
) -> tuple[tuple[XY, XY, XY, XY], WH]:
    pass


def scale_and_center_rect(
    br_coords: RectangleCoordinates,
    sr_wh: tuple[int, int],
    angle: Optional[float | int] = None,
) -> XYXY | tuple[tuple[XY, XY, XY, XY], WH]:
    """
    Given a big rectangle's xyxy and small rectangle's width and height, fit and center the small rectangle in the big rectangle, retaining the small rectangle's aspect ratio. Then, return the xyxy for the small rectangle to make that happen.

    Args:
    - br_xyxy (tuple[int, int, int, int]): Big rectangle's xyxy.
    - sr_wh (tuple[int, int]): Small rectangle's width and height.

    Returns:
        XYXY: Resulting xyxy.

    """
    br_x1, br_y1, br_x2, br_y2 = br_coords.xyxy()
    br_w = br_x2 - br_x1
    br_h = br_y2 - br_y1

    sr_w, sr_h = sr_wh

    # Scale factors based on the aspect ratio
    scale_w = br_w / sr_w
    scale_h = br_h / sr_h

    # Choose the smallest scaling factor to ensure the small rectangle fits
    scale = min(scale_w, scale_h)

    # Scaled width and height of the small rectangle
    scaled_w = int(round(sr_w * scale, 0))
    scaled_h = int(round(sr_h * scale, 0))

    # Compute the center of the big rectangle
    cx = (br_x1 + br_x2) // 2
    cy = (br_y1 + br_y2) // 2

    # Define the original rectangle corners (centered at origin)
    corners = [
        (-scaled_w // 2, -scaled_h // 2),
        (scaled_w // 2, -scaled_h // 2),
        (scaled_w // 2, scaled_h // 2),
        (-scaled_w // 2, scaled_h // 2),
    ]

    # If there's no rotation argument...
    if angle is None:
        # ...just center the rectangle...
        new_x1 = cx - scaled_w // 2
        new_y1 = cy - scaled_h // 2
        new_x2 = new_x1 + scaled_w
        new_y2 = new_y1 + scaled_h

        return XYXY(new_x1, new_y1, new_x2, new_y2)

    # ...else, apply the rotation matrix
    rotated_corners = []
    # Convert angle to radians
    theta = math.radians(angle)
    for x, y in corners:
        x_rotated = x * math.cos(theta) - y * math.sin(theta)
        y_rotated = x * math.sin(theta) + y * math.cos(theta)

        # Translate to the big rectangle's center
        x_final = cx + x_rotated
        y_final = cy + y_rotated

        # Round the final coordinates to the specified precision
        rotated_corners.append(XY(int(round(x_final, 0)), int(round(y_final, 0))))

    rotated_corners_tuple: tuple[XY, XY, XY, XY] = tuple(rotated_corners)  # type: ignore[assignment]

    return rotated_corners_tuple, WH(scaled_w, scaled_h)
