<h1 id=""><a href="#">Module imagesmacker.fields</a></h1>

[← Go back to `imagesmacker`](./index.md)

<h2 id="functions"><a href="#functions">Functions</a></h2>

<h3 id="functions-relative_field_formatting"><a href="#functions-relative_field_formatting"><pre>relative_field_formatting</pre></a></h3>

```python
(data_field_format: imagesmacker.models.fields.RelativeContainer | imagesmacker.models.fields.RelativeDataFieldFormat, dimensions: imagesmacker.models.coordinates.RectangleCoordinates) → dict[str, imagesmacker.models.coordinates.XYXY]
```

Non-recursive version of relative layout formatter using a manual stack.

Args:
    data_field_format (RelativeDataFieldFormat): Layout tree.
    dimensions (RectangleCoordinates): Bounding box to render in.

Returns:
    FieldsCoords: Dict of field names to XYXY positions.

---

[← Go back to `imagesmacker`](./index.md)