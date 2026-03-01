"""Pruebas para el workflow de creación de retos."""
from pathlib import Path

from cli.models.challenge_input import ChallengeInput
from cli.workflows import create_challenge


def _sample_data() -> ChallengeInput:
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


def test_build_replacements_generates_expected_fields():
    """Verifica que los reemplazos contienen valores clave."""
    data = _sample_data()
    mapping = create_challenge.build_replacements(data)

    assert mapping["WEEK_CODE"] == "W08"
    assert mapping["THEME_SLUG"] == "periodic_table_of_ai"
    assert mapping["RAW_FILENAME"].endswith("_raw.csv")
    assert mapping["PROCESSED_FILENAME"].endswith("_processed.csv")


def test_create_structure_builds_subfolders(tmp_path):
    """La estructura base debe incluir las carpetas estándar."""
    target = tmp_path / "W08_periodic_table_of_ai"
    create_challenge.create_structure(target)

    assert (target / "data" / "raw").exists()
    assert (target / "data" / "processed").exists()
    assert (target / "notebooks").exists()
    assert (target / "reports").exists()


def test_main_creates_directories_and_calls_generators(monkeypatch, tmp_path):
    """El flujo principal debe orquestar la creación del reto completo."""
    data = _sample_data()
    calls: list[str] = []

    def fake_gather_data():
        return data

    def fake_generate_readme(target_dir: Path, mapping: dict):  # pragma: no cover - stub
        calls.append("readme")
        assert target_dir.exists()
        assert mapping["THEME"] == data.theme

    def fake_generate_metadata(target_dir: Path, mapping: dict):  # pragma: no cover - stub
        calls.append("metadata")
        assert target_dir.exists()
        assert mapping["DATASET_URL"] == data.dataset

    def fake_generate_notebook(target_dir: Path, challenge: ChallengeInput, mapping: dict):
        calls.append("notebook")
        assert challenge.theme == data.theme
        assert mapping["EXPORT_NAME"].startswith("W08")

    monkeypatch.setattr(create_challenge, "gather_data", fake_gather_data)
    monkeypatch.setattr(create_challenge, "generate_readme", fake_generate_readme)
    monkeypatch.setattr(create_challenge, "generate_metadata", fake_generate_metadata)
    monkeypatch.setattr(create_challenge, "generate_notebook", fake_generate_notebook)
    monkeypatch.setattr(create_challenge, "CHALLENGE_ROOT", tmp_path)

    create_challenge.main()

    target = tmp_path / data.year / f"W08_{data.get_slug()}"
    assert target.exists()
    assert sorted(calls) == ["metadata", "notebook", "readme"]
