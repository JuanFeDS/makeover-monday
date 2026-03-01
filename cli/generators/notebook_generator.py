"""Generador de notebooks para retos individuales."""
from pathlib import Path

from cli.generators.base import fill_placeholders, load_template, write_file
from cli.models.challenge_input import ChallengeInput


def generate_notebook(
    target_dir: Path,
    data: ChallengeInput,
    mapping: dict,
) -> None:
    """Genera el notebook .ipynb del reto."""
    template_content = load_template("notebook_base.ipynb")
    filled_content = fill_placeholders(template_content, mapping)
    slug = data.get_slug()
    week_code = data.get_week_code()
    notebook_path = target_dir / "notebooks" / f"{week_code}_{slug}.ipynb"
    write_file(notebook_path, filled_content)
