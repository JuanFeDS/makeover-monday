# Semana W08 – Periodic Table of AI ✨

## Dataset 🌍
- **Fuente oficial**: https://data.world/makeovermonday/2026wk-8-the-periodic-table-of-ai-startups
- **Artículo original**: https://www.voronoiapp.com/investing/The-Periodic-Table-of-AI-Startups--14-categories-of-AI-companies-foundedfunded-Feb-2025-Feb-2026-7663
- **Fecha de publicación**: 2026-02-23
- **Descripción**: 305 startups de IA que recibieron financiamiento entre Feb 2025 - Feb 2026, organizadas en 14 categorías que representan diferentes capas del ecosistema (Foundation, Horizontal, Vertical, Emerging & Frontier).

## Objetivo 📌
**Visualización original**: Tabla periódica estilizada donde cada categoría aparece como una "tarjeta" con símbolo químico, funding total, número de startups, crecimiento YoY y tendencia de momentum.

**Mejoras implementadas**:
- Reducir protagonismo del símbolo químico para priorizar métricas clave (funding, startups, YoY).
- Usar íconos de tendencia y colores diferenciados por macrogrupo para mejorar legibilidad.
- Crear visualizaciones analíticas complementarias que revelen correlaciones entre las 3 variables numéricas y el campo `trend`.

## Limpieza y transformación 🧼
- **Archivos trabajados**: `data/raw/data_raw.xlsx` → `data/processed/ai_periodic_clean.parquet`
- **Pasos clave**:
  1. Carga del dataset original (14 categorías × 11 columnas).
  2. Creación de columnas derivadas:
     - `funding_pct_total`: porcentaje del funding total.
     - `funding_per_startup`: capital promedio por startup.
     - `rank_by_funding` y `rank_by_yoy`: rankings para análisis comparativo.
  3. Exportación a formato Parquet para reutilización eficiente.

## Hallazgos principales 💡
1. **Concentración extrema de capital**: Foundation Models captura $80B (>50% del total) con solo 15 startups, mientras categorías "Explosive" como AI Coding tienen $4.8B repartidos en 22 startups.

2. **Correlaciones identificadas**:
   - Funding y startup_count muestran correlación positiva moderada.
   - YoY growth NO correlaciona fuertemente con funding actual → las categorías emergentes (alto crecimiento) aún no concentran capital masivo.

3. **Patrones por Trend**:
   - **Explosive**: Alto YoY (~260%), funding moderado, pocas startups → oportunidad de inversión temprana.
   - **Mature**: Bajo YoY (~75%), funding masivo, pocas startups → mercado consolidado.
   - **Rising/Steady**: Zona intermedia con balance entre crecimiento y capital.

4. **Desequilibrios funding/startups**: Foundation Models tiene $5.3B por startup vs AI Coding con $0.22B por startup, revelando diferentes etapas de madurez.

## Visualización final 📊

### Poster Editorial (Nuevo)
**Archivo**: `generate_poster.py` → genera 3 formatos en `reports/`

Visualización editorial tipo poster (1600×2000px) con estética profesional inspirada en The Economist y Bloomberg Graphics:

- **Título**: "El Panorama de Startups de IA (2025-2026)"
- **Subtítulo**: "Dónde fluye el capital y dónde crece la innovación"
- **Componentes**:
  - **Mapa del Ecosistema**: Scatter plot (Funding vs Startups, tamaño = YoY Growth)
  - **Concentración de Capital**: Barras horizontales por categoría
  - **Sectores de Mayor Crecimiento**: Top 5 categorías por YoY
- **Paleta**: Fondo oscuro (#0B132B), texto claro (#EAEAEA), colores por categoría
- **Outputs**:
  - `ai_startup_landscape_poster.png` (prioritario para redes)
  - `ai_startup_landscape.html` (interactivo)
  - `ai_startup_landscape_poster.svg` (portafolio)

**Ejecución**:
```bash
python generate_poster.py
```

### Visualizaciones Exploratorias
- **Tabla periódica renovada**: `reports/periodic_table_ai_renovated.png`
- **Análisis complementarios** (en notebook):
  - Scatter plot: Funding vs Startups (tamaño = YoY, color = Trend)
  - Boxplot: Distribución de YoY Growth por Trend
  - Treemap: Distribución de Funding por Trend
  - Heatmap: Correlaciones entre métricas numéricas

## Arquitectura del Código 🏗️
```
src/charts/editorial/
├── __init__.py
├── ecosystem_scatter.py      # Scatter plot principal
├── funding_concentration.py  # Barras de funding
├── growth_leaders.py         # Barras de crecimiento
└── ai_landscape_poster.py    # Compositor final

src/config/
└── editorial_styles.py       # Paleta y estilos editoriales
```

## Próximos pasos 🚀
- ✅ Implementar visualización editorial modularizada
- Ejecutar `generate_poster.py` y validar outputs
- Publicar en redes con #MakeoverMonday #DataViz
- Compartir en portafolio profesional
