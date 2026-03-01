"""Funcionalidad base compartida por todos los generadores."""
from pathlib import Path

from cli.config.paths import TEMPLATE_DIR


def load_template(name: str) -> str:
    """Lee y devuelve el contenido de una plantilla."""
    path = TEMPLATE_DIR / name
    if not path.exists():
        raise FileNotFoundError(f"No se encontró la plantilla {name} en {TEMPLATE_DIR}")
    return path.read_text(encoding="utf-8")


def fill_placeholders(content: str, mapping: dict) -> str:
    """Reemplaza los marcadores {{KEY}} con los valores del diccionario."""
    for key, value in mapping.items():
        content = content.replace(f"{{{{{key}}}}}", value)
    return content


def write_file(target: Path, content: str):
    """Escribe contenido en un archivo."""
    target.write_text(content, encoding="utf-8")
