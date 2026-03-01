"""Pruebas para los generadores de archivos CLI."""
from pathlib import Path

from cli.generators.metadata_generator import generate_metadata
from cli.generators.notebook_generator import generate_notebook
from cli.generators.readme_generator import generate_readme
from cli.workflows import create_challenge
from cli.models.challenge_input import ChallengeInput


def _challenge_data() -> ChallengeInput:
    return ChallengeInput(
        year="2026",
        week="8",
        theme="Periodic Table of AI",
        dataset="https://data.test/dataset",
        source="https://data.test/source",
        published="2026-02-23",
        summary="Empresas de IA",
        original="https://viz.original",
        public="https://viz.public",
    )


def _mapping() -> dict:
    return create_challenge.build_replacements(_challenge_data())


def test_generate_readme_crea_archivo(tmp_path):
    """Valida que se genere un README con la información clave."""
    destino = tmp_path
    mapping = _mapping()

    generate_readme(destino, mapping)

    contenido = (destino / "README.md").read_text(encoding="utf-8")
    assert "Periodic Table of AI" in contenido
    assert mapping["WEEK_CODE"] in contenido


def test_generate_metadata_crea_yaml(tmp_path):
    """Comprueba que metadata.yaml incluye los campos del mapping."""
    destino = tmp_path
    mapping = _mapping()

    generate_metadata(destino, mapping)

    contenido = (destino / "metadata.yaml").read_text(encoding="utf-8")
    assert "dataset_url" in contenido.lower()
    assert mapping["DATASET_URL"] in contenido


def test_generate_notebook_crea_archivo(tmp_path):
    """Asegura que se produzca un notebook dentro de la carpeta notebooks."""
    destino = tmp_path
    mapping = _mapping()

    (destino / "notebooks").mkdir(parents=True, exist_ok=True)
    generate_notebook(destino, _challenge_data(), mapping)

    notebook_dir = destino / "notebooks"
    assert notebook_dir.exists()
    archivos = list(notebook_dir.glob("*.ipynb"))
    assert archivos, "Se esperaba un notebook generado"
    contenido = archivos[0].read_text(encoding="utf-8")
    assert mapping["THEME"] in contenido
