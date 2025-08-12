# Specifications

These are the specifications the library and library's API should adhere to.

## [Coordinates](coordinates.md)
- XY (point: `x, y`)
- XYXY (rectangle: `x1, y1, x2, y2`; top-left and bottom-right corner coordinates of the rectangle)
- XYWH (rectangle: `x, y, w, h`; top-left corner coordinates and width and height in pixels of the rectangle)
- XY4 (rotated rectangle: `(x1, y1), (x2, y2), (x3, y3), (x4, y4)`; coordinates of all corners of the rotated rectangle)
- Conversion from XYXY to XYWH, and vice versa.
## Text
### Orientation
- Horizontal
- Vertical
- Diagonal
### Styles
- Bold
- Italic
- Underline
- Outline/Stroke