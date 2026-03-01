"""Modelo de validación para datos de entrada de un reto."""
from datetime import date

from pydantic import BaseModel, field_validator


def slugify(text: str) -> str:
    """Convierte un texto en un slug en minúsculas separado por guiones bajos."""
    clean = "".join(ch.lower() if ch.isalnum() or ch == " " else " " for ch in text)
    return "_".join(filter(None, clean.split()))


class ChallengeInput(BaseModel):
    """Modelo que valida los datos capturados desde consola."""

    year: str
    week: str
    theme: str
    dataset: str = "https://makeovermonday.co.uk"
    source: str | None = None
    published: str
    summary: str | None = None
    original: str | None = None
    public: str | None = None

    @field_validator("year")
    @classmethod
    def year_digits(cls, value: str) -> str:
        """Valida que el año tenga 4 dígitos."""
        if len(value) != 4 or not value.isdigit():
            raise ValueError("El año debe tener 4 dígitos")
        return value

    @field_validator("week")
    @classmethod
    def week_range(cls, value: str) -> str:
        """Valida que la semana esté entre 1 y 53."""
        if not value.isdigit() or not (1 <= int(value) <= 53):
            raise ValueError("La semana debe estar entre 1 y 53")
        return value

    @field_validator("published")
    @classmethod
    def published_format(cls, value: str) -> str:
        """Valida que la fecha tenga formato ISO (YYYY-MM-DD)."""
        try:
            date.fromisoformat(value)
        except ValueError as exc:
            raise ValueError("Usa el formato YYYY-MM-DD") from exc
        return value

    def get_slug(self) -> str:
        """Devuelve el slug generado a partir del tema."""
        return slugify(self.theme)

    def get_week_code(self) -> str:
        """Devuelve el código de semana formateado (WXX)."""
        return f"W{self.week.zfill(2)}"
