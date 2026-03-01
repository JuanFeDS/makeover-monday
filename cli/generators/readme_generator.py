"""Generador de README para retos individuales."""
from pathlib import Path

from cli.generators.base import fill_placeholders, load_template, write_file


def generate_readme(target_dir: Path, mapping: dict) -> None:
    """Genera el archivo README.md del reto."""
    template_content = load_template("README_reto.md")
    filled_content = fill_placeholders(template_content, mapping)
    write_file(target_dir / "README.md", filled_content)
