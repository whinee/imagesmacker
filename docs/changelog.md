<h1 align="center" style="font-weight: bold">
    Changelog
</h1>

This software uses [Semantic Versioning v2.0.0](https://semver.org/spec/v2.0.0.html). This changelog is based on [keepachangelog.com v1.1.0](https://keepachangelog.com/en/1.1.0/).

**Types of Changes**

- `Added` for new features.
- `Changed` for changes in existing functionality.
- `Deprecated` for soon-to-be removed features.
- `Removed` for now removed features.
- `Fixed` for any bug fixes.
- `Security` in case of vulnerabilities.

## 4.0.0

### Added

- Utilities for handling angled text.
- Added parameter `min_font_size` to `imagesmacker.models.draw.TextConfig`
- Added parameter `direction` to models `imagesmacker.models.fields.RelativeRow` (now named `imagesmacker.models.fields.RelativeContainer`) and `imagesmacker.models.fields.RelativeDataFieldFormat`

### Changed

- Optimized text fitting algorithm to be binary search-like
- Changed `imagesmacker.models.draw.TextConfig`'s `font_size` parameter name to `max_font_size`
- Renamed `imagesmacker.models.fields.RelativeRow` to `imagesmacker.models.fields.RelativeContainer`

### Removed

- Removed useless dependencies.

## 3.0.1

I do not think there is anything wrong with the codebase right now!!!

### Fixed

- Fixed `imagesmacker.draw.Draw.text` to now be able to draw inverted multiline text by [FUCKING SWAPPING THESE TWO CHARACTERS (`=-` TO `-=`) IN LINE 214 MY GOD](https://github.com/whinee/imagesmacker/commit/0ea1b655fb59e1e61a0fc488560c867cfe2c3872#diff-cac509c2db6ab9619d324a7954ff1466e312219a0c4a7ee709462a97133b247a)

## 3.0.0

### Added

- Added parameters `error_correction`, `mask_pattern`, `background_color`, and `foreground_color` to `imagesmacker.models.draw.QRCodeConfig`.
- Added validation of coordinates in `imagesmacker.models.coordinates.XYXY` and `imagesmacker.models.coordinates.XYWH`.

### Changed

- Keys in parameter `options` in `imagesmacker.models.draw.Code128Config` to be top level keys.

## 2.1.5

### Fixed

- `imagesmacker.draw.Draw.text` and `imagesmacker.draw.Draw.barcode` to not draw `None` or empty strings

## 2.1.4

### Fixed

- Bumped `alltheutils` dependency version to `1.0.1`

## 2.1.3

### Fixed

- `alltheutils` dependency is now pinned

## 2.1.2

### Fixed

- Multiline text drawing; Broke inverted multiline text drawing instead

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