# Coordinates System

From the [pillow documentation](https://pillow.readthedocs.io/en/stable/handbook/concepts.html)

> The Python Imaging Library uses a Cartesian pixel coordinate system, with (0,0) in the upper left corner. Note that the coordinates refer to the implied pixel corners; the centre of a pixel addressed as (0, 0) actually lies at (0.5, 0.5).
>
> Coordinates are usually passed to the library as 2-tuples (x, y). Rectangles are represented as 4-tuples, (x1, y1, x2, y2), with the upper left corner given first.

## `RectangleCoordinates`

In the `imagesmacker` library, I have added a `RectangleCoordinates` class so that rectangles can have `xyxy` and `xywh` mode.
### modes

`xyxy`:
- `x1, y1`: top-left corner of the rectangle
- `x2, y2`: bottom-right corner of the rectangle

`xywh`:
- `x, y`: top-left corner of the rectangle
- `w, h`: width and height of the rectangle in pixels

## Example

`examples/01_coordinates.py`:

```python
from alltheutils.utils import parent_dir_nth_times
from PIL import Image, ImageDraw

from imagesmacker.models.coordinates import XYXY

image_size = (500, 500)
image = Image.new("RGB", image_size, color="black")
draw = ImageDraw.Draw(image)
rectangle_coords = XYXY(100, 100, 400, 400)

draw.rectangle(rectangle_coords.list(), fill="purple")

image.save(f"{parent_dir_nth_times(__file__, 2)}/docs/examples/coordinates-test.png")
```


### ``


