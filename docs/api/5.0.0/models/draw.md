<h1 id=""><a href="#">Module imagesmacker.models.draw</a></h1>

[← Go back to `imagesmacker.models`](./index.md)

<h2 id="functions"><a href="#functions">Functions</a></h2>

<h3 id="functions-validate_text_anchor"><a href="#functions-validate_text_anchor"><pre>validate_text_anchor</pre></a></h3>

```python
(anchor: str)
```

<h2 id="classes"><a href="#classes">Classes</a></h2>

<h3 id="classes-barcodeconfig"><a href="#classes-barcodeconfig"><pre>BarcodeConfig</pre></a></h3>

```python
(**data: Any)
```

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

<h4 id="classes-barcodeconfig-ancestors-in-mro"><a href="#classes-barcodeconfig-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- pydantic.main.BaseModel

<h4 id="classes-barcodeconfig-class-variables"><a href="#classes-barcodeconfig-class-variables">Class variables</a></h4>

<h5 id="classes-barcodeconfig-class-variables-code128"><a href="#classes-barcodeconfig-class-variables-code128"><pre>code128</pre></a></h5>

```python
imagesmacker.models.draw.Code128Config | None
```

<h5 id="classes-barcodeconfig-class-variables-model_config"><a href="#classes-barcodeconfig-class-variables-model_config"><pre>model_config</pre></a></h5>

<h5 id="classes-barcodeconfig-class-variables-qr"><a href="#classes-barcodeconfig-class-variables-qr"><pre>qr</pre></a></h5>

```python
imagesmacker.models.draw.QRCodeConfig | None
```

<h3 id="classes-code128config"><a href="#classes-code128config"><pre>Code128Config</pre></a></h3>

```python
(**data: Any)
```

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

<h4 id="classes-code128config-ancestors-in-mro"><a href="#classes-code128config-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- pydantic.main.BaseModel

<h4 id="classes-code128config-class-variables"><a href="#classes-code128config-class-variables">Class variables</a></h4>

<h5 id="classes-code128config-class-variables-model_config"><a href="#classes-code128config-class-variables-model_config"><pre>model_config</pre></a></h5>

<h5 id="classes-code128config-class-variables-module_height"><a href="#classes-code128config-class-variables-module_height"><pre>module_height</pre></a></h5>

```python
float
```

<h5 id="classes-code128config-class-variables-module_width"><a href="#classes-code128config-class-variables-module_width"><pre>module_width</pre></a></h5>

```python
float
```

<h5 id="classes-code128config-class-variables-options"><a href="#classes-code128config-class-variables-options"><pre>options</pre></a></h5>

```python
dict[str, typing.Any] | None
```

<h5 id="classes-code128config-class-variables-quiet_zone"><a href="#classes-code128config-class-variables-quiet_zone"><pre>quiet_zone</pre></a></h5>

```python
int
```

<h5 id="classes-code128config-class-variables-text_distance"><a href="#classes-code128config-class-variables-text_distance"><pre>text_distance</pre></a></h5>

```python
int
```

<h3 id="classes-fieldconfig"><a href="#classes-fieldconfig"><pre>FieldConfig</pre></a></h3>

```python
(**data: Any)
```

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

<h4 id="classes-fieldconfig-ancestors-in-mro"><a href="#classes-fieldconfig-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- pydantic.main.BaseModel

<h4 id="classes-fieldconfig-class-variables"><a href="#classes-fieldconfig-class-variables">Class variables</a></h4>

<h5 id="classes-fieldconfig-class-variables-barcode"><a href="#classes-fieldconfig-class-variables-barcode"><pre>barcode</pre></a></h5>

```python
imagesmacker.models.draw.BarcodeConfig | None
```

<h5 id="classes-fieldconfig-class-variables-model_config"><a href="#classes-fieldconfig-class-variables-model_config"><pre>model_config</pre></a></h5>

<h5 id="classes-fieldconfig-class-variables-text"><a href="#classes-fieldconfig-class-variables-text"><pre>text</pre></a></h5>

```python
imagesmacker.models.draw.TextConfig | None
```

<h3 id="classes-qrcodeconfig"><a href="#classes-qrcodeconfig"><pre>QRCodeConfig</pre></a></h3>

```python
(**data: Any)
```

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

<h4 id="classes-qrcodeconfig-ancestors-in-mro"><a href="#classes-qrcodeconfig-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- pydantic.main.BaseModel

<h4 id="classes-qrcodeconfig-class-variables"><a href="#classes-qrcodeconfig-class-variables">Class variables</a></h4>

<h5 id="classes-qrcodeconfig-class-variables-background_color"><a href="#classes-qrcodeconfig-class-variables-background_color"><pre>background_color</pre></a></h5>

```python
str | tuple[int, int, int]
```

<h5 id="classes-qrcodeconfig-class-variables-border"><a href="#classes-qrcodeconfig-class-variables-border"><pre>border</pre></a></h5>

```python
int
```

<h5 id="classes-qrcodeconfig-class-variables-box_size"><a href="#classes-qrcodeconfig-class-variables-box_size"><pre>box_size</pre></a></h5>

```python
int
```

<h5 id="classes-qrcodeconfig-class-variables-error_correction"><a href="#classes-qrcodeconfig-class-variables-error_correction"><pre>error_correction</pre></a></h5>

```python
int
```

<h5 id="classes-qrcodeconfig-class-variables-foreground_color"><a href="#classes-qrcodeconfig-class-variables-foreground_color"><pre>foreground_color</pre></a></h5>

```python
str | tuple[int, int, int]
```

<h5 id="classes-qrcodeconfig-class-variables-mask_pattern"><a href="#classes-qrcodeconfig-class-variables-mask_pattern"><pre>mask_pattern</pre></a></h5>

```python
int | None
```

<h5 id="classes-qrcodeconfig-class-variables-model_config"><a href="#classes-qrcodeconfig-class-variables-model_config"><pre>model_config</pre></a></h5>

<h3 id="classes-textconfig"><a href="#classes-textconfig"><pre>TextConfig</pre></a></h3>

```python
(**data: Any)
```

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

<h4 id="classes-textconfig-ancestors-in-mro"><a href="#classes-textconfig-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- pydantic.main.BaseModel

<h4 id="classes-textconfig-class-variables"><a href="#classes-textconfig-class-variables">Class variables</a></h4>

<h5 id="classes-textconfig-class-variables-anchor"><a href="#classes-textconfig-class-variables-anchor"><pre>anchor</pre></a></h5>

```python
Literal['lt', 'mt', 'rt', 'lm', 'mm', 'rm', 'lb', 'mb', 'rb']
```

<h5 id="classes-textconfig-class-variables-break_text"><a href="#classes-textconfig-class-variables-break_text"><pre>break_text</pre></a></h5>

```python
bool
```

<h5 id="classes-textconfig-class-variables-font"><a href="#classes-textconfig-class-variables-font"><pre>font</pre></a></h5>

```python
str
```

<h5 id="classes-textconfig-class-variables-inverted"><a href="#classes-textconfig-class-variables-inverted"><pre>inverted</pre></a></h5>

```python
bool
```

<h5 id="classes-textconfig-class-variables-line_height"><a href="#classes-textconfig-class-variables-line_height"><pre>line_height</pre></a></h5>

```python
float | int
```

<h5 id="classes-textconfig-class-variables-max_font_size"><a href="#classes-textconfig-class-variables-max_font_size"><pre>max_font_size</pre></a></h5>

```python
int
```

<h5 id="classes-textconfig-class-variables-min_font_size"><a href="#classes-textconfig-class-variables-min_font_size"><pre>min_font_size</pre></a></h5>

```python
int
```

<h5 id="classes-textconfig-class-variables-model_config"><a href="#classes-textconfig-class-variables-model_config"><pre>model_config</pre></a></h5>

<h5 id="classes-textconfig-class-variables-style"><a href="#classes-textconfig-class-variables-style"><pre>style</pre></a></h5>

```python
imagesmacker.models.draw.TextStyle
```

<h3 id="classes-textstyle"><a href="#classes-textstyle"><pre>TextStyle</pre></a></h3>

```python
(**data: Any)
```

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

<h4 id="classes-textstyle-ancestors-in-mro"><a href="#classes-textstyle-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- pydantic.main.BaseModel

<h4 id="classes-textstyle-class-variables"><a href="#classes-textstyle-class-variables">Class variables</a></h4>

<h5 id="classes-textstyle-class-variables-fill"><a href="#classes-textstyle-class-variables-fill"><pre>fill</pre></a></h5>

```python
float | tuple[int, ...] | str
```

<h5 id="classes-textstyle-class-variables-italics"><a href="#classes-textstyle-class-variables-italics"><pre>italics</pre></a></h5>

```python
bool
```

<h5 id="classes-textstyle-class-variables-model_config"><a href="#classes-textstyle-class-variables-model_config"><pre>model_config</pre></a></h5>

<h5 id="classes-textstyle-class-variables-underline"><a href="#classes-textstyle-class-variables-underline"><pre>underline</pre></a></h5>

```python
bool
```

---

[← Go back to `imagesmacker.models`](./index.md)