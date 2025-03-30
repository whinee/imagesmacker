# Constants

# Choose recipes
default:
    @ just -l

[private]
black:
    @ python -m black -q examples > /dev/null 2>&1
    @ python -m black -q imagesmacker > /dev/null 2>&1
    @ python -m black -q test > /dev/null 2>&1

[private]
nio:
    @ python -m no_implicit_optional examples
    @ python -m no_implicit_optional imagesmacker
    @ python -m no_implicit_optional test

[private]
ruff:
    @ python -m ruff check --fix --exit-zero examples
    @ python -m ruff check --fix --exit-zero imagesmacker
    @ python -m ruff check --fix --exit-zero test

# Set up development environment
[unix]
bootstrap:
    #!/usr/bin/env bash
    rm -rf poetry.lock
    poetry install --with dev

# Lint codebase
lint:
    @ just black
    @ just nio
    @ just ruff

test:
    python examples/01_coordinates.py
    python examples/02_text.py
    python examples/03_multiline_text.py
    python examples/04_inverted_text.py
    python examples/05_inverted_multiline_text.py
    python examples/06_QR_code.py
    python examples/07_Code128.py

    python test/text_anchors_inverted_multiline.py
    python test/text_anchors_multiline.py
    python test/text_anchors.py

version:
    @ poetry version

bump +args:
    @ poetry version {{args}}
    @ poetry version | awk '{print $2}' > dev/version