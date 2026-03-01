"""Funciones para capturar inputs del usuario por consola."""
from datetime import date

from pydantic import ValidationError

from cli.models.challenge_input import ChallengeInput


def ask(
    prompt: str,
    required: bool = False,
    default: str | None = None,
) -> str:
    """Solicita un valor por consola y valida si es obligatorio."""
    suffix = f" [{default}]" if default else ""
    while True:
        value = input(f"{prompt}{suffix}: ").strip()
        if value:
            return value
        if default:
            return default
        if not required:
            return ""
        print("Este campo es obligatorio.")


def gather_data() -> ChallengeInput:
    """Recoge y valida los datos necesarios para crear el reto."""
    while True:
        raw = {
            "year": ask("Año del reto", True),
            "week": ask("Semana (sin W)", True),
            "theme": ask("Tema del reto", True),
            "dataset": ask("URL del dataset oficial", default="https://makeovermonday.co.uk"),
            "source": ask("URL de la visualización original"),
            "published": ask("Fecha de publicación (YYYY-MM-DD)", default=date.today().isoformat()),
            "summary": ask("Resumen breve del dataset"),
            "original": ask("Link a la visualización original"),
            "public": ask("Link público de tu visualización"),
        }
        try:
            return ChallengeInput(**raw)
        except ValidationError as err:
            print("\n⚠️  Revisa los campos ingresados:")
            for issue in err.errors():
                field = issue.get("loc", ["dato"])[0]
                print(f"- {field}: {issue.get('msg')}")
            print()
