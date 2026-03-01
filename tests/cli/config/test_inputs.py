"""Pruebas para la captura de datos en CLI."""
from datetime import date

from cli.config import inputs
from cli.models.challenge_input import ChallengeInput


def _mock_input(monkeypatch, responses: list[str]):
    iterator = iter(responses)

    def _fake_input(_: str):  # pragma: no cover - helper
        return next(iterator)

    monkeypatch.setattr("builtins.input", _fake_input)


def test_gather_data_devuelve_modelo_valido(monkeypatch):
    """Verifica que gather_data construye ChallengeInput con datos correctos."""
    _mock_input(
        monkeypatch,
        [
            "2026",
            "8",
            "Energía Solar",
            "https://data.test",
            "https://viz.original",
            "2026-03-01",
            "Resumen breve",
            "https://original",
            "https://public",
        ],
    )

    resultado = inputs.gather_data()

    assert isinstance(resultado, ChallengeInput)
    assert resultado.year == "2026"
    assert resultado.week == "8"
    assert resultado.theme == "Energía Solar"
    assert resultado.dataset == "https://data.test"
    assert resultado.published == "2026-03-01"


def test_gather_data_aplica_defaults(monkeypatch):
    """Comprueba que se usan valores por defecto cuando el usuario deja campos vacíos."""

    class FakeDate:
        """Stub sencillo para fijar la fecha actual."""

        @staticmethod
        def today():  # pragma: no cover - método auxiliar
            return date(2026, 3, 5)

    _mock_input(
        monkeypatch,
        [
            "2026",
            "9",
            "Tema Default",
            "",  # dataset → usa default
            "",
            "",  # published → usa fecha actual
            "",
            "",
            "",
        ],
    )
    monkeypatch.setattr(inputs, "date", FakeDate)

    resultado = inputs.gather_data()
    assert resultado.dataset == "https://makeovermonday.co.uk"
    assert resultado.published == "2026-03-05"


def test_gather_data_reintenta_si_hay_error(monkeypatch):
    """Simula un error de validación y luego una entrada válida."""
    respuestas = [
        "20",  # Año inválido
        "8",
        "Tema inválido",
        "",
        "",
        "2026-03-01",
        "",
        "",
        "",
        "2026",  # Año válido
        "10",
        "Tema válido",
        "https://dataset",
        "",
        "2026-03-02",
        "",
        "",
        "",
    ]
    _mock_input(monkeypatch, respuestas)

    resultado = inputs.gather_data()
    assert resultado.year == "2026"
    assert resultado.week == "10"
