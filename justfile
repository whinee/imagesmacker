# Constants
dev_docs := "dev/docs"
docs_api_root_dir := "docs/api"
docs_api_unreleased_dir := docs_api_root_dir + "/unreleased"

app_id := if os_family() == "windows" {
    `. .\\.venv\\Scripts\\Activate.ps1; python -c 'exec("""\ntry:\n from alltheutils import config\n print(config.read_conf_file("dev/values/constants/main.yaml")["app_name"])\nexcept ModuleNotFoundError:\n print("PLACEHOLDER")\n""")'`
} else {
    `source .venv/bin/activate && python -c 'exec("""\ntry:\n from alltheutils import config\n print(config.read_conf_file("dev/values/constants/main.yaml")["app_name"])\nexcept ModuleNotFoundError:\n print("PLACEHOLDER")\n""")'`
}

app_version := if os_family() == "windows" {
    `. .\\.venv\\Scripts\\Activate.ps1; python -c 'exec("""\ntry:\n from alltheutils import config\n print(config.read_conf_file("dev/values/programmatic_variables/main.dev.json")["version"])\nexcept ModuleNotFoundError:\n print("PLACEHOLDER")\n""")'`
} else {
    `source .venv/bin/activate && python -c 'exec("""\ntry:\n from alltheutils import config\n print(config.read_conf_file("dev/values/programmatic_variables/main.dev.json")["version"])\nexcept ModuleNotFoundError:\n print("PLACEHOLDER")\n""")'`
}

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
    rm -rf .venv
    rm -f uv.lock
    uv venv
    source .venv/bin/activate
    uv sync

# Set up development environment
[windows]
bootstrap:
    Remove-Item -Recurse -Force .venv
    Remove-Item -Force uv.lock
    uv venv
    . .\.venv\Scripts\Activate.ps1
    uv sync

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
    @ echo {{app_version}}

# Generate documentation
[unix]
docs:
    #!/usr/bin/env bash
    set -euo pipefail
    TMPDIR=$(mktemp -d)
    TARGET_DIR="{{docs_api_unreleased_dir}}"

    just lint

    pdoc --force --output-dir "$TMPDIR" --template-dir dev/tpl/pdoc3 {{app_id}} >/dev/null
    
    rm -rf "$TARGET_DIR"
    mkdir -p "$TARGET_DIR"
    cp -r "$TMPDIR/{{app_id}}"/* "$TARGET_DIR"
    rm -rf "$TMPDIR"

    mkdir -p "$TARGET_DIR/dev"
    cp -r "{{dev_docs}}"/* "$TARGET_DIR/dev"

    echo "Docs generated in $TARGET_DIR"

[unix]
[confirm('Are you sure you want to bump the version? [y/N]')]
bump *FLAGS:
    #!/usr/bin/env bash
    set -euo pipefail

    python -m dev.scripts.py.dev bump {{FLAGS}}

    just docs

    APP_VERSION=$(python -c 'from alltheutils.config import read_conf_file;print(read_conf_file("dev/values/programmatic_variables/main.dev.json")["version"])')

    DOCS_SOURCE_DIR="{{docs_api_unreleased_dir}}"
    DOCS_TARGET_DIR="{{docs_api_root_dir}}/$APP_VERSION"

    rm -rf "$DOCS_TARGET_DIR"
    mkdir -p "$DOCS_TARGET_DIR"
    cp -r "$DOCS_SOURCE_DIR"/* "$DOCS_TARGET_DIR"

    echo "Docs generated in $DOCS_TARGET_DIR"