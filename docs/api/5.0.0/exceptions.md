<h1 id=""><a href="#">Module imagesmacker.exceptions</a></h1>

[← Go back to `imagesmacker`](./index.md)

<h2 id="classes"><a href="#classes">Classes</a></h2>

<h3 id="classes-drawdataerror"><a href="#classes-drawdataerror"><pre>DrawDataError</pre></a></h3>

```python
(*args, **kwargs)
```

Common base class for all exceptions

<h4 id="classes-drawdataerror-ancestors-in-mro"><a href="#classes-drawdataerror-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- builtins.BaseException

<h4 id="classes-drawdataerror-descendants"><a href="#classes-drawdataerror-descendants">Descendants</a></h4>

- imagesmacker.exceptions.DrawDataValidationError

<h3 id="classes-drawdatatypeinvalid"><a href="#classes-drawdatatypeinvalid"><pre>DrawDataTypeInvalid</pre></a></h3>

```python
(message: str, details: str | None = None)
```

Base class for all custom exceptions.

<h4 id="classes-drawdatatypeinvalid-ancestors-in-mro"><a href="#classes-drawdatatypeinvalid-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- imagesmacker.exceptions.DrawDataValidationError
- imagesmacker.exceptions.DrawDataError
- alltheutils.exceptions.ValidationError
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-drawdatatypenotinfieldattrs"><a href="#classes-drawdatatypenotinfieldattrs"><pre>DrawDataTypeNotInFieldAttrs</pre></a></h3>

```python
(message: str, details: str | None = None)
```

Base class for all custom exceptions.

<h4 id="classes-drawdatatypenotinfieldattrs-ancestors-in-mro"><a href="#classes-drawdatatypenotinfieldattrs-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- imagesmacker.exceptions.DrawDataValidationError
- imagesmacker.exceptions.DrawDataError
- alltheutils.exceptions.ValidationError
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-drawdatavalidationerror"><a href="#classes-drawdatavalidationerror"><pre>DrawDataValidationError</pre></a></h3>

```python
(*args, **kwargs)
```

Common base class for all exceptions

<h4 id="classes-drawdatavalidationerror-ancestors-in-mro"><a href="#classes-drawdatavalidationerror-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- imagesmacker.exceptions.DrawDataError
- alltheutils.exceptions.ValidationError
- builtins.BaseException

<h4 id="classes-drawdatavalidationerror-descendants"><a href="#classes-drawdatavalidationerror-descendants">Descendants</a></h4>

- imagesmacker.exceptions.DrawDataTypeInvalid
- imagesmacker.exceptions.DrawDataTypeNotInFieldAttrs

---

[← Go back to `imagesmacker`](./index.md)