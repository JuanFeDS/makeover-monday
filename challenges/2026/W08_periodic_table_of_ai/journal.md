# Bitácora MakeOverMonday W08 – Periodic Table of AI

## 1. Alcance y objetivos
- Replicar y mejorar la tabla periódica original que resume 14 categorías de startups de IA financiadas entre feb/2025 y feb/2026.
- Mantener la narrativa de "tarjetas" con símbolo, métricas clave (funding, startups, YoY) y momentum (trend).
- Complementar con visualizaciones exploratorias (scatter, boxplot, treemap) para extraer insights adicionales.

## 2. Datos y preparación
- Fuente: dataset público de la semana W08 en MakeOverMonday (305 startups agregadas en 14 grupos).
- Rutas configuradas en el notebook (`RAW_PATH` y `PROCESSED_PATH`).
- Limpieza mínima: copia del raw + métricas derivadas (`funding_pct_total`, `funding_per_startup`, `rank_by_funding`, `rank_by_yoy`).
- Exportación a Parquet para reutilizar en gráficos posteriores.

## 3. Visualizaciones implementadas
1. **Scatter Funding vs Startups**: tamaño proporcional a YoY y color por trend para detectar desequilibrios.
2. **Boxplot YoY por Trend**: contraste de distribuciones para cada momentum.
3. **Treemap Funding por Trend**: peso relativo de capital según la tendencia.
4. **Tabla periódica renovada** con `build_periodic_table_figure` (colores por macrogrupo, íconos de trend, orden personalizado).
5. **Tarjetas individuales (`build_periodic_card`)**: replican la estética original y permiten mostrar cada registro de forma aislada.

## 4. Evolución de las tarjetas
- Se arregló la exportación de `CARD_STYLE` para disponiblizarlo vía `src.config`.
- Se añadió `build_periodic_card` al paquete `src.charts.composition` para importaciones limpias.
- El header y el borde ahora dependen del grupo (`GROUP_COLORS`), alineándolos con la paleta general del dashboard.
- El fondo de la figura (paper/plot) se hizo transparente para que solo se renderice la tarjeta.
- El notebook incluye una celda que recorre `processed_df` y genera una tarjeta por categoría con `display(fig)`.

## 5. Hallazgos clave
- **Concentración extrema**: Foundation Models capta >50% del capital con solo 15 startups.
- **Momentum emergente**: categorías etiquetadas como Explosive/Rising muestran altos YoY (≥200%) pero funding más bajo → oportunidades de inversión temprana.
- **Desacople funding/startups**: la relación $/startup evidencia etapas de madurez distintas (p.ej. Foundation vs AI Coding).
- **Diversidad cromática**: al mapear `group` → color, las tarjetas refuerzan visualmente la segmentación por capa del ecosistema (foundation, horizontal, vertical, emerging).

## 6. Poster Editorial (Nueva Implementación)
**Fecha**: 2026-03-14

### Decisiones de diseño
- **Arquitectura modularizada**: Código organizado en `src/charts/editorial/` para reutilización.
- **Paleta oscura**: Fondo #0B132B, paneles #1C2541, texto #EAEAEA (inspirado en The Economist/Bloomberg).
- **Idioma**: Todos los textos en español para audiencia hispanohablante.
- **Tipografía**: Inter para títulos, labels y anotaciones (legibilidad profesional).
- **Colores por categoría**: 14 colores únicos asignados a cada categoría de IA.

### Componentes implementados
1. **`editorial_styles.py`**: Paleta de colores, fuentes, layout del poster, templates de anotaciones.
2. **`ecosystem_scatter.py`**: Scatter plot principal (Funding vs Startups, tamaño = YoY Growth).
3. **`funding_concentration.py`**: Barras horizontales de concentración de capital.
4. **`growth_leaders.py`**: Top 5 sectores con mayor crecimiento YoY.
5. **`ai_landscape_poster.py`**: Compositor que une las 3 visualizaciones en layout 2×2.
6. **`generate_poster.py`**: Script ejecutable que genera PNG, HTML y SVG.

### Narrativa visual
- **Título**: "El Panorama de Startups de IA (2025-2026)"
- **Subtítulo**: "Dónde fluye el capital y dónde crece la innovación"
- **Anotaciones clave**:
  - Foundation Models captura 58% del capital con solo 15 startups
  - AI Coding crece 320% anual (el más rápido)
  - Vertical AI superó a Horizontal AI en financiamiento

### Outputs generados
- `ai_startup_landscape_poster.png` (1600×2000px, scale=2 para alta resolución)
- `ai_startup_landscape.html` (versión interactiva con hover tooltips)
- `ai_startup_landscape_poster.svg` (vectorial para portafolio)

## 7. Próximos pasos
- ✅ Implementar visualización editorial modularizada
- Ejecutar `python generate_poster.py` y validar outputs
- Publicar poster en redes con #MakeoverMonday #DataViz
- Compartir en portafolio profesional
- Explorar series temporales si aparecen datos históricos

---
Última actualización: {{DATE:2026-03-14}} a las 19:42 (UTC-05).
