# Constants

# Choose recipes
default:
    @ just -lu; printf '%s ' press Enter to continue; read; just --choose

[private]
nio:
    @ python -m no_implicit_optional imagesmacker; exit 0

[private]
ruff:
    @ python -m ruff check --fix imagesmacker; exit 0

# Set up development environment
[unix]
bootstrap:
    #!/usr/bin/env bash
    rm -rf poetry.lock
    poetry install --with dev

# Lint codebase
lint:
    @ just nio
    @ python -m black -q imagesmacker
    @ just ruff
