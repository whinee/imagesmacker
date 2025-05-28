<h1 id=""><a href="#">Module imagesmacker.draw</a></h1>

[← Go back to `imagesmacker`](./index.md)

<h2 id="functions"><a href="#functions">Functions</a></h2>

<h3 id="functions-check_if_type_in_field_attrs"><a href="#functions-check_if_type_in_field_attrs"><pre>check_if_type_in_field_attrs</pre></a></h3>

```python
(field_attributes: pydantic.main.BaseModel) → Callable[[str], pydantic.main.BaseModel]
```

<h2 id="classes"><a href="#classes">Classes</a></h2>

<h3 id="classes-barcode"><a href="#classes-barcode"><pre>Barcode</pre></a></h3>

<h4 id="classes-barcode-static-methods"><a href="#classes-barcode-static-methods">Static methods</a></h4>

<h5 id="classes-barcode-static-methods-code128"><a href="#classes-barcode-static-methods-code128"><pre>code128</pre></a></h5>

```python
(data: str, field_coords: imagesmacker.models.coordinates.RectangleCoordinates, field_attributes: imagesmacker.models.draw.Code128Config) → qrcode.image.pil.PilImage
```

<h5 id="classes-barcode-static-methods-qr"><a href="#classes-barcode-static-methods-qr"><pre>qr</pre></a></h5>

```python
(data: str, field_coords: imagesmacker.models.coordinates.RectangleCoordinates, field_attributes: imagesmacker.models.draw.QRCodeConfig) → qrcode.image.base.BaseImage
```

<h3 id="classes-draw"><a href="#classes-draw"><pre>Draw</pre></a></h3>

```python
(image: PIL.Image.Image)
```

An abstraction of `ImageDraw.Draw` specifically for drawing texts and barcodes in images.

<h4 id="classes-draw-methods"><a href="#classes-draw-methods">Methods</a></h4>

<h5 id="classes-draw-methods-barcode"><a href="#classes-draw-methods-barcode"><pre>barcode</pre></a></h5>

```python
(self, data: str, field_coords: imagesmacker.models.coordinates.RectangleCoordinates, field_attributes: type[imagesmacker.models.draw.BarcodeConfig]) → None
```

<h5 id="classes-draw-methods-break_text"><a href="#classes-draw-methods-break_text"><pre>break_text</pre></a></h5>

```python
(self, text: str, text_config: imagesmacker.models.draw.TextConfig, font_size: int, fsc: imagesmacker.fonts.FontSizeCalculator, field_width: int, field_height: int) → tuple[int, list[str], int]
```

<h5 id="classes-draw-methods-data"><a href="#classes-draw-methods-data"><pre>data</pre></a></h5>

```python
(self, type: str, data: str, field_coords: imagesmacker.models.coordinates.RectangleCoordinates, field_attributes: imagesmacker.models.draw.FieldConfig) → None
```

<h5 id="classes-draw-methods-text"><a href="#classes-draw-methods-text"><pre>text</pre></a></h5>

```python
(self, data: str, field_coords: imagesmacker.models.coordinates.RectangleCoordinates, field_attributes: imagesmacker.models.draw.TextConfig) → None
```

Try to fit the text within the field.

Args:
- text (`str`): Text to be drawn
- field_coords (`RectangleCoordinates`): _description_
- field_attributes (`FieldAttributes`): _description_

---

[← Go back to `imagesmacker`](./index.md)