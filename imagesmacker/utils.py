from imagesmacker.models.coordinates import RectangleCoordinates


def rect_coords_middle_point(
    coordinates: RectangleCoordinates,
) -> tuple[int, float]:
    x1, y1, x2, y2 = coordinates.xyxy()
    return (x2 - x1, y2 - y1)
