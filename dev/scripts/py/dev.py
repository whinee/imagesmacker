import os
from pathlib import Path
from typing import Any, Optional

from alltheutils.cli.base import command
from alltheutils.cli.utils import parse_config_file_cli_config, select
from alltheutils.config import read_conf_file, write_to_conf_file
from alltheutils.exceptions import BumpVersionExceptions
from alltheutils.instance_config import set_instance_config
from alltheutils.utils import (
    bump_version,
    get_value_from_or_update_nested_dict,
    parent_dir_nth_times,
)
from click.decorators import group

BUMP_TYPES = ["major", "minor", "patch", "prerelease", "prerelease_num"]


program_vars_dir = os.path.join(parent_dir_nth_times(__file__, 3), "values", "programmatic_variables")
pyproject_fp = os.path.join(parent_dir_nth_times(__file__, 4), "pyproject.toml")

main_dev_json_fp = os.path.join(program_vars_dir, "main.dev.json")
version_fp = os.path.join(program_vars_dir, "version")

main_dev_json = read_conf_file(main_dev_json_fp)
pyproject = read_conf_file(pyproject_fp)

cli_config = parse_config_file_cli_config(os.path.join(parent_dir_nth_times(__file__), "values", "cli.yaml"))

translation_files_dir = Path(os.path.join(parent_dir_nth_times(__file__), "text"))

translation_file_dict = {}

for translation_file in translation_files_dir.glob("*.json"):
    translation_file_dict[translation_file.stem] = str(translation_file)

set_instance_config("language", "en")
set_instance_config("languages_texts", translation_file_dict)

@group(**cli_config.group_command_params.model_dump())
def cmd_group(**kwargs: dict[str, Any]) -> None:
    """Main command group."""


cli = command(cmd_group, cli_config.commands)

@cli
def bump(part: Optional[str], build: Optional[str] = None) -> None:  # noqa: C901
    """Bump the version of the project."""
    version: str = main_dev_json["version"]
    selection = {}
    if part is None:
        for part in BUMP_TYPES:
            try:
                theoretical_next_version = bump_version(version, part, build)
            except BumpVersionExceptions:
                continue
            else:
                selection[f"{part} ({theoretical_next_version})"] = {
                    "value": theoretical_next_version,
                }
        err, next_version = select("Select which part of the version to bump", selection, ret_err=True)
        if not err:
            exit(1)
    else:
        next_version = bump_version(version, part, build)

    main_dev_json["version"] = next_version

    get_value_from_or_update_nested_dict(pyproject, "project.version", next_version)

    write_to_conf_file(main_dev_json_fp, main_dev_json)
    write_to_conf_file(pyproject_fp, pyproject)

    with open(version_fp, "w") as f:
        f.write(next_version)

cmd_group()