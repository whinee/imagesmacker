# Constants

# Choose recipes
default:
    @ just -lu; printf '%s ' press Enter to continue; read; just --choose

[private]
black:
    @ python -m black -q imagesmacker; python -m black -q test; exit 0

[private]
nio:
    @ python -m no_implicit_optional imagesmacker; python -m no_implicit_optional test; exit 0

[private]
ruff:
    @ python -m ruff check --fix imagesmacker; python -m ruff check --fix test; exit 0

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
