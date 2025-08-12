<h1 id=""><a href="#">Module imagesmacker.fonts</a></h1>

[← Go back to `imagesmacker`](./index.md)

<h2 id="functions"><a href="#functions">Functions</a></h2>

<h3 id="functions-font_loader"><a href="#functions-font_loader"><pre>font_loader</pre></a></h3>

```python
(filepath: str, size: int = 10) → PIL.ImageFont.FreeTypeFont
```

<h2 id="classes"><a href="#classes">Classes</a></h2>

<h3 id="classes-fontsizecalculator"><a href="#classes-fontsizecalculator"><pre>FontSizeCalculator</pre></a></h3>

```python
(draw: PIL.ImageDraw.ImageDraw, font_path: str)
```

Initialize the FontSizeCalculator class.

Args:
- draw (`ImageDraw.ImageDraw`): The ImageDraw object to use for text measurement.
- font_path (`str`): The font path to use.
- kwargs (`dict[str, Any]`): Additional keyword arguments.

<h4 id="classes-fontsizecalculator-methods"><a href="#classes-fontsizecalculator-methods">Methods</a></h4>

<h5 id="classes-fontsizecalculator-methods-get_text_bbox"><a href="#classes-fontsizecalculator-methods-get_text_bbox"><pre>get_text_bbox</pre></a></h5>

```python
(self, size: int, text: str) → tuple[int, int]
```

Get the width and height of the text for a given font size.

Args:
- size (`int`): The font size to measure.
- text (`str`): The text string to measure.

Returns:
`list[int]`: A list containing the width and height of the text.

---

[← Go back to `imagesmacker`](./index.md)