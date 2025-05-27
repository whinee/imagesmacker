<h1 id=""><a href="#">Module imagesmacker.models.fields</a></h1>

[← Go back to `imagesmacker.models`](./index.md)

<h2 id="classes"><a href="#classes">Classes</a></h2>

<h3 id="classes-barcodefieldattributes"><a href="#classes-barcodefieldattributes"><pre>BarcodeFieldAttributes</pre></a></h3>

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

<h4 id="classes-barcodefieldattributes-ancestors-in-mro"><a href="#classes-barcodefieldattributes-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- imagesmacker.models.fields.FieldAttributes
- pydantic.main.BaseModel

<h4 id="classes-barcodefieldattributes-class-variables"><a href="#classes-barcodefieldattributes-class-variables">Class variables</a></h4>

<h5 id="classes-barcodefieldattributes-class-variables-barcode_config"><a href="#classes-barcodefieldattributes-class-variables-barcode_config"><pre>barcode_config</pre></a></h5>

```python
imagesmacker.models.draw.BarcodeConfig
```

<h5 id="classes-barcodefieldattributes-class-variables-model_config"><a href="#classes-barcodefieldattributes-class-variables-model_config"><pre>model_config</pre></a></h5>

<h3 id="classes-fieldattributes"><a href="#classes-fieldattributes"><pre>FieldAttributes</pre></a></h3>

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

<h4 id="classes-fieldattributes-ancestors-in-mro"><a href="#classes-fieldattributes-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- pydantic.main.BaseModel

<h4 id="classes-fieldattributes-descendants"><a href="#classes-fieldattributes-descendants">Descendants</a></h4>

- imagesmacker.models.fields.BarcodeFieldAttributes
- imagesmacker.models.fields.TextFieldAttributes

<h4 id="classes-fieldattributes-class-variables"><a href="#classes-fieldattributes-class-variables">Class variables</a></h4>

<h5 id="classes-fieldattributes-class-variables-model_config"><a href="#classes-fieldattributes-class-variables-model_config"><pre>model_config</pre></a></h5>

<h3 id="classes-relativecontainer"><a href="#classes-relativecontainer"><pre>RelativeContainer</pre></a></h3>

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

<h4 id="classes-relativecontainer-ancestors-in-mro"><a href="#classes-relativecontainer-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- pydantic.main.BaseModel

<h4 id="classes-relativecontainer-class-variables"><a href="#classes-relativecontainer-class-variables">Class variables</a></h4>

<h5 id="classes-relativecontainer-class-variables-cells"><a href="#classes-relativecontainer-class-variables-cells"><pre>cells</pre></a></h5>

```python
Sequence[imagesmacker.models.fields.RelativeContainer | imagesmacker.models.fields.RelativeFieldCell]
```

<h5 id="classes-relativecontainer-class-variables-direction"><a href="#classes-relativecontainer-class-variables-direction"><pre>direction</pre></a></h5>

```python
str | Literal['lr', 'rl', 'tb', 'bt']
```

<h5 id="classes-relativecontainer-class-variables-fr"><a href="#classes-relativecontainer-class-variables-fr"><pre>fr</pre></a></h5>

```python
float
```

<h5 id="classes-relativecontainer-class-variables-model_config"><a href="#classes-relativecontainer-class-variables-model_config"><pre>model_config</pre></a></h5>

<h3 id="classes-relativedatafieldformat"><a href="#classes-relativedatafieldformat"><pre>RelativeDataFieldFormat</pre></a></h3>

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

<h4 id="classes-relativedatafieldformat-ancestors-in-mro"><a href="#classes-relativedatafieldformat-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- pydantic.main.BaseModel

<h4 id="classes-relativedatafieldformat-class-variables"><a href="#classes-relativedatafieldformat-class-variables">Class variables</a></h4>

<h5 id="classes-relativedatafieldformat-class-variables-cells"><a href="#classes-relativedatafieldformat-class-variables-cells"><pre>cells</pre></a></h5>

```python
Sequence[imagesmacker.models.fields.RelativeContainer | imagesmacker.models.fields.RelativeFieldCell]
```

<h5 id="classes-relativedatafieldformat-class-variables-direction"><a href="#classes-relativedatafieldformat-class-variables-direction"><pre>direction</pre></a></h5>

```python
str | Literal['lr', 'rl', 'tb', 'bt']
```

<h5 id="classes-relativedatafieldformat-class-variables-model_config"><a href="#classes-relativedatafieldformat-class-variables-model_config"><pre>model_config</pre></a></h5>

<h3 id="classes-relativefieldcell"><a href="#classes-relativefieldcell"><pre>RelativeFieldCell</pre></a></h3>

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

<h4 id="classes-relativefieldcell-ancestors-in-mro"><a href="#classes-relativefieldcell-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- pydantic.main.BaseModel

<h4 id="classes-relativefieldcell-class-variables"><a href="#classes-relativefieldcell-class-variables">Class variables</a></h4>

<h5 id="classes-relativefieldcell-class-variables-fr"><a href="#classes-relativefieldcell-class-variables-fr"><pre>fr</pre></a></h5>

```python
float
```

<h5 id="classes-relativefieldcell-class-variables-model_config"><a href="#classes-relativefieldcell-class-variables-model_config"><pre>model_config</pre></a></h5>

<h5 id="classes-relativefieldcell-class-variables-name"><a href="#classes-relativefieldcell-class-variables-name"><pre>name</pre></a></h5>

```python
str
```

<h3 id="classes-textfieldattributes"><a href="#classes-textfieldattributes"><pre>TextFieldAttributes</pre></a></h3>

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

<h4 id="classes-textfieldattributes-ancestors-in-mro"><a href="#classes-textfieldattributes-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- imagesmacker.models.fields.FieldAttributes
- pydantic.main.BaseModel

<h4 id="classes-textfieldattributes-class-variables"><a href="#classes-textfieldattributes-class-variables">Class variables</a></h4>

<h5 id="classes-textfieldattributes-class-variables-model_config"><a href="#classes-textfieldattributes-class-variables-model_config"><pre>model_config</pre></a></h5>

<h5 id="classes-textfieldattributes-class-variables-text_config"><a href="#classes-textfieldattributes-class-variables-text_config"><pre>text_config</pre></a></h5>

```python
imagesmacker.models.draw.TextConfig
```

---

[← Go back to `imagesmacker.models`](./index.md)