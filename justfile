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
