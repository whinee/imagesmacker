<h1 id=""><a href="#">Module imagesmacker.utils</a></h1>

[← Go back to `imagesmacker`](./index.md)

<h2 id="functions"><a href="#functions">Functions</a></h2>

<h3 id="functions-rect_coords_middle_point"><a href="#functions-rect_coords_middle_point"><pre>rect_coords_middle_point</pre></a></h3>

```python
(coordinates: imagesmacker.models.coordinates.RectangleCoordinates) → tuple[int, int]
```

<h3 id="functions-scale_and_center_rect"><a href="#functions-scale_and_center_rect"><pre>scale_and_center_rect</pre></a></h3>

```python
(br_coords: imagesmacker.models.coordinates.RectangleCoordinates, sr_wh: tuple[int, int], angle: float | int | None = None) → imagesmacker.models.coordinates.XYXY | tuple[tuple[imagesmacker.models.coordinates.XY, imagesmacker.models.coordinates.XY, imagesmacker.models.coordinates.XY, imagesmacker.models.coordinates.XY], imagesmacker.models.coordinates.WH]
```

Given a big rectangle's xyxy and small rectangle's width and height, fit and center the small rectangle in the big rectangle, retaining the small rectangle's aspect ratio. Then, return the xyxy for the small rectangle to make that happen.

Args:
- br_xyxy (tuple[int, int, int, int]): Big rectangle's xyxy.
- sr_wh (tuple[int, int]): Small rectangle's width and height.

Returns:
    XYXY: Resulting xyxy.

---

[← Go back to `imagesmacker`](./index.md)