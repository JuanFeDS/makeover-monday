"""Flujo principal para crear un nuevo reto de MakeOverMonday."""
from pathlib import Path

from cli.config.inputs import gather_data
from cli.config.paths import CHALLENGE_ROOT
from cli.generators.metadata_generator import generate_metadata
from cli.generators.notebook_generator import generate_notebook
from cli.generators.readme_generator import generate_readme
from cli.models.challenge_input import ChallengeInput


def build_replacements(data: ChallengeInput) -> dict:
    """Genera el diccionario de reemplazos usando los datos capturados."""
    slug = data.get_slug()
    week_code = data.get_week_code()
    raw_name = f"{data.year}_{week_code}_{slug}_raw.csv"
    processed_name = raw_name.replace("_raw", "_processed")
    return {
        "WEEK_CODE": week_code,
        "THEME": data.theme,
        "DATASET_URL": data.dataset,
        "SOURCE_URL": data.source or data.dataset,
        "PUBLISHED_DATE": data.published,
        "DATASET_SUMMARY": data.summary or "Añade un resumen breve",
        "ORIGINAL_VIZ_URL": data.original or "",
        "IMPROVEMENT_NOTES": "¿Qué mejorarás?",
        "RAW_FILENAME": raw_name,
        "PROCESSED_FILENAME": processed_name,
        "STEP_ONE": "Describe el primer paso",
        "STEP_TWO": "Describe el segundo paso",
        "INSIGHT_ONE": "Insight preliminar",
        "INSIGHT_TWO": "Insight adicional",
        "PUBLIC_LINK": data.public or "",
        "EXPORT_NAME": f"{week_code}_{slug}.png",
        "NEXT_STEPS": "Lista de pendientes",
        "DIMENSION": "dimension",
        "METRIC": "metric",
        "CHART_TITLE": data.theme,
        "THEME_SLUG": slug,
        "NOTES": "",
    }


def create_structure(target_dir: Path):
    """Crea las subcarpetas estándar del reto."""
    folders = ["data/raw", "data/processed", "notebooks", "reports"]
    for folder in folders:
        (target_dir / folder).mkdir(parents=True, exist_ok=True)


def main():
    """Ejecuta el flujo completo de creación del reto."""
    data = gather_data()
    slug = data.get_slug()
    week_code = data.get_week_code()
    target_dir = CHALLENGE_ROOT / data.year / f"{week_code}_{slug}"

    if target_dir.exists():
        raise FileExistsError(f"La carpeta {target_dir} ya existe")

    create_structure(target_dir)
    mapping = build_replacements(data)

    generate_readme(target_dir, mapping)
    generate_metadata(target_dir, mapping)
    generate_notebook(target_dir, data, mapping)

    print(f"✅ Reto creado exitosamente en: {target_dir}")

if __name__ == "__main__":
    main()
