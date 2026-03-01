# MakeOverMonday Challenges ✨

Repositorio personal para documentar los retos semanales de **MakeoverMonday**: descargo el dataset oficial, analizo/transformo la información, genero visualizaciones y registro aprendizajes. 📊

## ¿Qué es MakeoverMonday? 🌍
MakeoverMonday es un evento comunitario de visualización de datos. Cada lunes se publica un dataset en [MakeoverMonday](https://makeovermonday.co.uk) junto con una pieza original que sirve como punto de partida. El objetivo es "rehacer" esa visualización para comunicar mejor la historia de los datos y compartir el resultado usando el hashtag **#MakeoverMonday**.

## Organización de carpetas 📁

- `challenges/` – Artefactos de cada reto, organizados por año y semana.
  ```
  challenges/
  └── 2026/
      ├── W7_Living_Planet_Index/
      │   ├── data/           # raw y processed
      │   ├── notebooks/
      │   ├── reports/
      │   ├── README.md
      │   └── metadata.yaml
      └── W8_Periodic_Table_of_AI/
          └── ...
  ```
  Cada carpeta semanal contendrá:
  - `data/raw` y `data/processed`: datasets originales y versiones limpias.
  - `notebooks/`: análisis reproducible (formato `.ipynb`).
  - `reports/`: exportaciones finales (PNG/PDF, enlaces como `tableau_url.txt`).
  - `README.md`: resumen rápido (fuente, idea principal, visualización).
  - `metadata.yaml`: campos estructurados (fecha, link al dataset, hashtag, herramientas).

- `src/` – Código reutilizable (transformaciones, helpers y definiciones para gráficos).
  - `src/transformations/`: funciones de limpieza e imputación.
  - `src/charts/`: utilidades para construir visualizaciones consistentes.
  - `src/config/params.py`: parámetros comunes (rutas, colores, etc.).
- `pyproject.toml` – Configuración de dependencias y metadatos del proyecto (usando `uv`).
- `cli/` – Herramientas interactivas para automatizar la creación de retos.
  - `cli/config/`: rutas y captura de inputs (incluye validaciones).
  - `cli/models/`: Pydantic models para los datos ingresados.
  - `cli/generators/`: scripts que producen README, metadata y notebooks desde templates.
  - `cli/workflows/`: orquestan los flujos completos (p. ej. `create_challenge.py`).

## Flujo de trabajo semanal 🔁
1. **Explorar el reto:** revisar el dataset publicado y registrar la referencia (link y descripción) en `metadata.yaml`.
2. **Preparar carpeta:** copiar la estructura base `challenges/<año>/WkXX_Tema/` y crear subcarpetas `data/raw`, `data/processed`, `notebooks`, `reports`.
3. **Ingesta y limpieza:** almacenar el archivo original en `data/raw`, generar versiones limpias en `data/processed` utilizando funciones de `src/transformations` si aplica.
4. **Análisis y visualización:** trabajar el notebook principal dentro de `notebooks/`, invocando utilidades de `src/charts` para mantener consistencia.
5. **Documentar:** completar el `README.md` del reto (contexto, hallazgos, próximos pasos) y actualizar `metadata.yaml` con las URLs de publicación (Tableau Public, blog, etc.).
6. **Exportar resultados:** guardar la visualización final en `reports/` (PNG/PDF) y, si aplica, la URL pública en un `.txt`.

## Entorno y dependencias (uv) 🧰
El proyecto utiliza Python ≥ 3.10 y gestiona dependencias con [uv](https://github.com/astral-sh/uv).

### Creación automática de retos ⚙️
Para generar la estructura de una nueva semana usando el CLI modular:

```bash
uv run python -m cli.workflows.create_challenge
```

El comando solicita año, semana, tema y enlaces relevantes, valida los datos con Pydantic y crea la carpeta correspondiente (incluyendo `data/`, `notebooks/`, `reports/`, README, metadata y notebook base).
