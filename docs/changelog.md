## 2.1.1

### Changed

- `imagesmacker.draw.Barcode.code128` now tries to fill up the whole field

## 2.1.0

### Added

- Ability to change the text's color

### Changed

- Extra fields are now forbidden for models in `imagesmacker/models/draw.py` and `imagesmacker/models/fields.py`

## 2.0.0

### Added

- QR code and Code 128 barcode drawing

### Changed

- `imagesmacker.models.fields.FieldAttributes` to `imagesmacker.models.fields.TextFieldAttributes`; `imagesmacker.models.fields.FieldAttributes` is now a generic for FieldAttributes.

## 1.0.0

### Added

- Functional horizontal text drawing

## 0.0.0

Initial Release of the package