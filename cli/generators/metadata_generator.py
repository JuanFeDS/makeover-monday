"""Generador de metadata.yaml para retos individuales."""
from pathlib import Path

from cli.generators.base import fill_placeholders, load_template, write_file


def generate_metadata(
    target_dir: Path,
    mapping: dict,
) -> None:
    """Genera el archivo metadata.yaml del reto."""
    template_content = load_template("metadata_template.yaml")
    filled_content = fill_placeholders(template_content, mapping)
    write_file(target_dir / "metadata.yaml", filled_content)
