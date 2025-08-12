<h1 id=""><a href="#">Module imagesmacker.models.coordinates</a></h1>

[← Go back to `imagesmacker.models`](./index.md)

<h2 id="classes"><a href="#classes">Classes</a></h2>

<h3 id="classes-coordinates"><a href="#classes-coordinates"><pre>Coordinates</pre></a></h3>

<h4 id="classes-coordinates-descendants"><a href="#classes-coordinates-descendants">Descendants</a></h4>

- imagesmacker.models.coordinates.WH
- imagesmacker.models.coordinates.XY

<h4 id="classes-coordinates-class-variables"><a href="#classes-coordinates-class-variables">Class variables</a></h4>

<h5 id="classes-coordinates-class-variables-coords"><a href="#classes-coordinates-class-variables-coords"><pre>coords</pre></a></h5>

```python
<function NamedTuple at 0x7f9d6ec22d40>
```

<h4 id="classes-coordinates-methods"><a href="#classes-coordinates-methods">Methods</a></h4>

<h5 id="classes-coordinates-methods-dict"><a href="#classes-coordinates-methods-dict"><pre>dict</pre></a></h5>

```python
(self) → dict[str, int]
```

<h5 id="classes-coordinates-methods-list"><a href="#classes-coordinates-methods-list"><pre>list</pre></a></h5>

```python
(self) → list[int]
```

<h5 id="classes-coordinates-methods-tuple"><a href="#classes-coordinates-methods-tuple"><pre>tuple</pre></a></h5>

```python
(self) → tuple[int, int]
```

<h3 id="classes-rectanglecoordinates"><a href="#classes-rectanglecoordinates"><pre>RectangleCoordinates</pre></a></h3>

Rectangle Coordinates.

You can have an `xyxy` or `xywh` mode coordinates and it can be read by any
methods that knows how to read `RectangleCoordinates`.

Args:
    metaclass (_type_, optional): _description_. Defaults to abc.ABCMeta.

<h4 id="classes-rectanglecoordinates-descendants"><a href="#classes-rectanglecoordinates-descendants">Descendants</a></h4>

- imagesmacker.models.coordinates.XYWH
- imagesmacker.models.coordinates.XYXY

<h4 id="classes-rectanglecoordinates-class-variables"><a href="#classes-rectanglecoordinates-class-variables">Class variables</a></h4>

<h5 id="classes-rectanglecoordinates-class-variables-coords"><a href="#classes-rectanglecoordinates-class-variables-coords"><pre>coords</pre></a></h5>

```python
<function NamedTuple at 0x7f9d6ec22d40>
```

<h4 id="classes-rectanglecoordinates-methods"><a href="#classes-rectanglecoordinates-methods">Methods</a></h4>

<h5 id="classes-rectanglecoordinates-methods-dict"><a href="#classes-rectanglecoordinates-methods-dict"><pre>dict</pre></a></h5>

```python
(self) → dict[str, int]
```

<h5 id="classes-rectanglecoordinates-methods-list"><a href="#classes-rectanglecoordinates-methods-list"><pre>list</pre></a></h5>

```python
(self) → list[int]
```

<h5 id="classes-rectanglecoordinates-methods-text_coordinates"><a href="#classes-rectanglecoordinates-methods-text_coordinates"><pre>text_coordinates</pre></a></h5>

```python
(self, anchor: Literal['lt', 'mt', 'rt', 'lm', 'mm', 'rm', 'lb', 'mb', 'rb'] = 'mm') → tuple[int, int]
```

`RectangleCoordinates` is often used as.

Args:
- anchor (`TextAnchor`, optional): _description_. Defaults to `"mm"`.

Returns:
`tuple[int, int]`: _description_

<h5 id="classes-rectanglecoordinates-methods-tuple"><a href="#classes-rectanglecoordinates-methods-tuple"><pre>tuple</pre></a></h5>

```python
(self) → tuple[int, int, int, int]
```

<h5 id="classes-rectanglecoordinates-methods-xywh"><a href="#classes-rectanglecoordinates-methods-xywh"><pre>xywh</pre></a></h5>

```python
(self) → imagesmacker.models.coordinates.XYWHNamedTuple
```

<h5 id="classes-rectanglecoordinates-methods-xyxy"><a href="#classes-rectanglecoordinates-methods-xyxy"><pre>xyxy</pre></a></h5>

```python
(self) → imagesmacker.models.coordinates.XYXYNamedTuple
```

<h3 id="classes-wh"><a href="#classes-wh"><pre>WH</pre></a></h3>

```python
(w: int, h: int)
```

<h4 id="classes-wh-ancestors-in-mro"><a href="#classes-wh-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- imagesmacker.models.coordinates.Coordinates

<h4 id="classes-wh-methods"><a href="#classes-wh-methods">Methods</a></h4>

<h5 id="classes-wh-methods-wh"><a href="#classes-wh-methods-wh"><pre>wh</pre></a></h5>

```python
(self) → imagesmacker.models.coordinates.WHNamedTuple
```

<h3 id="classes-whnamedtuple"><a href="#classes-whnamedtuple"><pre>WHNamedTuple</pre></a></h3>

```python
(w: int, h: int)
```

WHNamedTuple(w, h)

<h4 id="classes-whnamedtuple-ancestors-in-mro"><a href="#classes-whnamedtuple-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- builtins.tuple

<h4 id="classes-whnamedtuple-instance-variables"><a href="#classes-whnamedtuple-instance-variables">Instance variables</a></h4>

<h5 id="classes-whnamedtuple-instance-variables-h"><a href="#classes-whnamedtuple-instance-variables-h"><pre>h</pre></a></h5>

```python
int
```

Alias for field number 1

<h5 id="classes-whnamedtuple-instance-variables-w"><a href="#classes-whnamedtuple-instance-variables-w"><pre>w</pre></a></h5>

```python
int
```

Alias for field number 0

<h3 id="classes-xy"><a href="#classes-xy"><pre>XY</pre></a></h3>

```python
(x: int, y: int)
```

<h4 id="classes-xy-ancestors-in-mro"><a href="#classes-xy-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- imagesmacker.models.coordinates.Coordinates

<h4 id="classes-xy-methods"><a href="#classes-xy-methods">Methods</a></h4>

<h5 id="classes-xy-methods-xy"><a href="#classes-xy-methods-xy"><pre>xy</pre></a></h5>

```python
(self) → imagesmacker.models.coordinates.XYNamedTuple
```

<h3 id="classes-xynamedtuple"><a href="#classes-xynamedtuple"><pre>XYNamedTuple</pre></a></h3>

```python
(x: int, y: int)
```

XYNamedTuple(x, y)

<h4 id="classes-xynamedtuple-ancestors-in-mro"><a href="#classes-xynamedtuple-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- builtins.tuple

<h4 id="classes-xynamedtuple-instance-variables"><a href="#classes-xynamedtuple-instance-variables">Instance variables</a></h4>

<h5 id="classes-xynamedtuple-instance-variables-x"><a href="#classes-xynamedtuple-instance-variables-x"><pre>x</pre></a></h5>

```python
int
```

Alias for field number 0

<h5 id="classes-xynamedtuple-instance-variables-y"><a href="#classes-xynamedtuple-instance-variables-y"><pre>y</pre></a></h5>

```python
int
```

Alias for field number 1

<h3 id="classes-xywh"><a href="#classes-xywh"><pre>XYWH</pre></a></h3>

```python
(x: int, y: int, w: int, h: int)
```

Rectangle Coordinates.

You can have an `xyxy` or `xywh` mode coordinates and it can be read by any
methods that knows how to read `RectangleCoordinates`.

Args:
    metaclass (_type_, optional): _description_. Defaults to abc.ABCMeta.

<h4 id="classes-xywh-ancestors-in-mro"><a href="#classes-xywh-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- imagesmacker.models.coordinates.RectangleCoordinates

<h4 id="classes-xywh-methods"><a href="#classes-xywh-methods">Methods</a></h4>

<h5 id="classes-xywh-methods-text_coordinates"><a href="#classes-xywh-methods-text_coordinates"><pre>text_coordinates</pre></a></h5>

```python
(self, anchor: Literal['lt', 'mt', 'rt', 'lm', 'mm', 'rm', 'lb', 'mb', 'rb'] = 'mm') → tuple[int, int]
```

`RectangleCoordinates` is often used as.

Args:
- anchor (`TextAnchor`, optional): _description_. Defaults to `"mm"`.

Returns:
`tuple[int, int]`: _description_

<h5 id="classes-xywh-methods-xywh"><a href="#classes-xywh-methods-xywh"><pre>xywh</pre></a></h5>

```python
(self) → imagesmacker.models.coordinates.XYWHNamedTuple
```

<h5 id="classes-xywh-methods-xyxy"><a href="#classes-xywh-methods-xyxy"><pre>xyxy</pre></a></h5>

```python
(self) → imagesmacker.models.coordinates.XYXYNamedTuple
```

Convert `XYWHNamedTuple` to `XYXYNamedTuple`.

Returns:
`XYXYNamedTuple`

<h3 id="classes-xywhnamedtuple"><a href="#classes-xywhnamedtuple"><pre>XYWHNamedTuple</pre></a></h3>

```python
(x: int, y: int, w: int, h: int)
```

XYWHNamedTuple(x, y, w, h)

<h4 id="classes-xywhnamedtuple-ancestors-in-mro"><a href="#classes-xywhnamedtuple-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- builtins.tuple

<h4 id="classes-xywhnamedtuple-instance-variables"><a href="#classes-xywhnamedtuple-instance-variables">Instance variables</a></h4>

<h5 id="classes-xywhnamedtuple-instance-variables-h"><a href="#classes-xywhnamedtuple-instance-variables-h"><pre>h</pre></a></h5>

```python
int
```

Alias for field number 3

<h5 id="classes-xywhnamedtuple-instance-variables-w"><a href="#classes-xywhnamedtuple-instance-variables-w"><pre>w</pre></a></h5>

```python
int
```

Alias for field number 2

<h5 id="classes-xywhnamedtuple-instance-variables-x"><a href="#classes-xywhnamedtuple-instance-variables-x"><pre>x</pre></a></h5>

```python
int
```

Alias for field number 0

<h5 id="classes-xywhnamedtuple-instance-variables-y"><a href="#classes-xywhnamedtuple-instance-variables-y"><pre>y</pre></a></h5>

```python
int
```

Alias for field number 1

<h3 id="classes-xyxy"><a href="#classes-xyxy"><pre>XYXY</pre></a></h3>

```python
(x1: int, y1: int, x2: int, y2: int)
```

Rectangle Coordinates.

You can have an `xyxy` or `xywh` mode coordinates and it can be read by any
methods that knows how to read `RectangleCoordinates`.

Args:
    metaclass (_type_, optional): _description_. Defaults to abc.ABCMeta.

<h4 id="classes-xyxy-ancestors-in-mro"><a href="#classes-xyxy-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- imagesmacker.models.coordinates.RectangleCoordinates

<h4 id="classes-xyxy-methods"><a href="#classes-xyxy-methods">Methods</a></h4>

<h5 id="classes-xyxy-methods-text_coordinates"><a href="#classes-xyxy-methods-text_coordinates"><pre>text_coordinates</pre></a></h5>

```python
(self, anchor: Literal['lt', 'mt', 'rt', 'lm', 'mm', 'rm', 'lb', 'mb', 'rb'] = 'mm') → tuple[int, int]
```

`RectangleCoordinates` is often used as.

Args:
- anchor (`TextAnchor`, optional): _description_. Defaults to `"mm"`.

Returns:
`tuple[int, int]`: _description_

<h5 id="classes-xyxy-methods-xywh"><a href="#classes-xyxy-methods-xywh"><pre>xywh</pre></a></h5>

```python
(self) → imagesmacker.models.coordinates.XYWHNamedTuple
```

Convert `XYXYNamedTuple` to `XYWHNamedTuple`.

Returns:
`XYWHNamedTuple`

<h5 id="classes-xyxy-methods-xyxy"><a href="#classes-xyxy-methods-xyxy"><pre>xyxy</pre></a></h5>

```python
(self) → imagesmacker.models.coordinates.XYXYNamedTuple
```

<h3 id="classes-xyxynamedtuple"><a href="#classes-xyxynamedtuple"><pre>XYXYNamedTuple</pre></a></h3>

```python
(x1: int, y1: int, x2: int, y2: int)
```

XYXYNamedTuple(x1, y1, x2, y2)

<h4 id="classes-xyxynamedtuple-ancestors-in-mro"><a href="#classes-xyxynamedtuple-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- builtins.tuple

<h4 id="classes-xyxynamedtuple-instance-variables"><a href="#classes-xyxynamedtuple-instance-variables">Instance variables</a></h4>

<h5 id="classes-xyxynamedtuple-instance-variables-x1"><a href="#classes-xyxynamedtuple-instance-variables-x1"><pre>x1</pre></a></h5>

```python
int
```

Alias for field number 0

<h5 id="classes-xyxynamedtuple-instance-variables-x2"><a href="#classes-xyxynamedtuple-instance-variables-x2"><pre>x2</pre></a></h5>

```python
int
```

Alias for field number 2

<h5 id="classes-xyxynamedtuple-instance-variables-y1"><a href="#classes-xyxynamedtuple-instance-variables-y1"><pre>y1</pre></a></h5>

```python
int
```

Alias for field number 1

<h5 id="classes-xyxynamedtuple-instance-variables-y2"><a href="#classes-xyxynamedtuple-instance-variables-y2"><pre>y2</pre></a></h5>

```python
int
```

Alias for field number 3

---

[← Go back to `imagesmacker.models`](./index.md)