# MakeOverMonday Challenges ✨

Repositorio personal para documentar los retos semanales de **MakeoverMonday**: descargo el dataset oficial, analizo y transformo la información, y preparo los datos limpios para su visualización. 📊

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
  - `notebooks/`: análisis y transformaciones reproducibles (formato `.ipynb`).
  - `README.md`: resumen rápido (fuente, hallazgos, decisiones de limpieza).
  - `metadata.yaml`: campos estructurados (fecha, link al dataset, hashtag, herramientas).

- `src/` – Código reutilizable de transformación y limpieza de datos.
  - `src/transformations/`: funciones de limpieza, imputación, normalización y conversión de tipos.
- `pyproject.toml` – Configuración de dependencias y metadatos del proyecto (usando `uv`).
- `cli/` – Herramientas interactivas para automatizar la creación de retos.
  - `cli/config/`: rutas y captura de inputs (incluye validaciones).
  - `cli/models/`: Pydantic models para los datos ingresados.
  - `cli/generators/`: scripts que producen README, metadata y notebooks desde templates.
  - `cli/workflows/`: orquestan los flujos completos (p. ej. `create_challenge.py`).

## Flujo de trabajo semanal 🔁
1. **Explorar el reto:** revisar el dataset publicado y registrar la referencia (link y descripción) en `metadata.yaml`.
2. **Preparar carpeta:** usar el CLI para generar la estructura `challenges/<año>/WkXX_Tema/` con subcarpetas `data/raw`, `data/processed` y `notebooks/`.
3. **Ingesta y limpieza:** almacenar el archivo original en `data/raw`, generar versiones limpias en `data/processed` usando funciones de `src/transformations`.
4. **Análisis:** trabajar el notebook dentro de `notebooks/` — EDA, transformaciones y exportación del dato limpio.
5. **Documentar:** completar el `README.md` del reto (contexto, hallazgos, decisiones de limpieza) y actualizar `metadata.yaml`.
6. **Visualizar:** importar `data/processed/` en [Da Vinci](https://github.com/JuanFeDS/da_vinci) para construir la visualización final.

## Entorno y dependencias (Poetry) 🧰
El proyecto utiliza Python ≥ 3.10 y gestiona dependencias con [Poetry](https://python-poetry.org/).

### Configuración del entorno virtual

1. Asegúrate de tener Poetry instalado (`pipx install poetry`, `pip install --user poetry`, etc.).
2. Dentro del repositorio ejecuta:
   ```powershell
   poetry install
   ```
   Esto creará `.venv/` y resolverá todas las dependencias declaradas en `pyproject.toml`.
3. Para abrir un shell con el entorno activo:
   ```powershell
   poetry shell
   ```
   También puedes prefijar cualquier comando con `poetry run ...` sin activar el shell.

### Uso en scripts y CLI

- Scripts locales: `poetry run python ruta/al/script.py` (garantiza que se use el entorno correcto).
- CLI interno: `poetry run python -m cli.workflows.create_challenge`.

### Uso en notebooks de Jupyter

- Se registró el kernel `MakeoverMonday (Poetry)` apuntando a `.venv`.
- Selecciona ese kernel en VS Code/Jupyter Lab para ejecutar notebooks ubicados en `challenges/<año>/...` o `notebooks/`.
- Si necesitas recrear el kernel tras reinstalar dependencias, ejecuta:
  ```powershell
  poetry run python -m ipykernel install --user --name makeovermonday-poetry --display-name "MakeoverMonday (Poetry)"
  ```

### Creación automática de retos ⚙️
Para generar la estructura de una nueva semana usando el CLI modular:

```bash
poetry run python -m cli.workflows.create_challenge
```

El comando solicita año, semana, tema y enlaces relevantes, valida los datos con Pydantic y crea la carpeta correspondiente (incluyendo `data/`, `notebooks/`, `reports/`, README, metadata y notebook base).
