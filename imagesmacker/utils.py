from imagesmacker.models.coordinates import XYXY, RectangleCoordinates


def rect_coords_middle_point(
    coordinates: RectangleCoordinates,
) -> tuple[int, float]:
    x1, y1, x2, y2 = coordinates.xyxy()
    return (x2 - x1, y2 - y1)


def scale_and_center_rect(
    br_coords: RectangleCoordinates,
    sr_wh: tuple[int, int],
) -> XYXY:
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

    scale_w = br_w / sr_w
    scale_h = br_h / sr_h

    scale = min(scale_w, scale_h)

    scaled_sr_w = int(sr_w * scale)
    scaled_sr_h = int(sr_h * scale)

    new_x1 = br_x1 + (br_w - scaled_sr_w) // 2
    new_y1 = br_y1 + (br_h - scaled_sr_h) // 2
    new_x2 = new_x1 + scaled_sr_w
    new_y2 = new_y1 + scaled_sr_h

    return XYXY(new_x1, new_y1, new_x2, new_y2)
