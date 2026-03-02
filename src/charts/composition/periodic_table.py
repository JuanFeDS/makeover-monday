"""Visualización de tabla periódica con Plotly."""
import pandas as pd

import plotly.graph_objects as go

from src.config.styles import (
    GROUP_COLORS,
    TREND_ICONS,
    GROUP_LABELS,
    FONT_FAMILY,
    FONT_SIZES,
    COLORS,
    get_yoy_color
)


def _build_shapes(df: pd.DataFrame, layout_positions: dict, id_col: str, group_col: str) -> list:
    """Construye las formas (rectángulos) de la tabla periódica."""
    shapes = []
    for _, row in df.iterrows():
        cat_id = row[id_col]
        if cat_id not in layout_positions:
            continue

        x, y = layout_positions[cat_id]
        bg_color = GROUP_COLORS.get(row[group_col], '#EEEEEE')
        shapes.append(
            dict(
                type='rect',
                x0=x,
                y0=y,
                x1=x + 0.95,
                y1=y + 0.95,
                line={
                    'color': COLORS['border'],
                    'width': 2
                },
                fillcolor=bg_color,
                layer='below'
            )
        )
    return shapes


def _build_annotations(
    df: pd.DataFrame,
    layout_positions: dict,
    id_col: str,
    symbol_col: str,
    name_col: str,
    trend_col: str,
    value_col: str,
    count_col: str,
    growth_col: str
) -> list:
    """Construye las anotaciones (textos) de la tabla periódica."""
    annotations = []

    for _, row in df.iterrows():
        cat_id = row[id_col]
        if cat_id not in layout_positions:
            continue

        x, y = layout_positions[cat_id]

        annotations.extend([
            dict(
                x=x + 0.08,
                y=y + 0.87,
                text=str(cat_id),
                showarrow=False,
                font=dict(size=FONT_SIZES['tiny'], color=COLORS['text_light'])
            ),
            dict(
                x=x + 0.87,
                y=y + 0.87,
                text=TREND_ICONS.get(row[trend_col], ''),
                showarrow=False,
                font=dict(size=FONT_SIZES['medium']),
                xanchor='right'
            )
        ])

        annotations.append(
            dict(
                x=x + 0.47,
                y=y + 0.70,
                text=row[symbol_col],
                showarrow=False,
                font=dict(
                    size=FONT_SIZES['large'],
                    color=COLORS['text_secondary'],
                    family=FONT_FAMILY,
                    weight='bold'
                )
            )
        )

        annotations.append(
            dict(
                x=x + 0.47,
                y=y + 0.54,
                text=f"${row[value_col]:.1f}B",
                showarrow=False,
                font=dict(
                    size=FONT_SIZES['medium'],
                    color=COLORS['text_primary'],
                    family=FONT_FAMILY,
                    weight='bold'
                )
            )
        )

        annotations.append(
            dict(
                x=x + 0.47,
                y=y + 0.40,
                text=f"{row[count_col]} startups",
                showarrow=False,
                font=dict(size=FONT_SIZES['small'], color=COLORS['text_subtle'])
            )
        )

        yoy_color = get_yoy_color(row[growth_col])
        annotations.append(
            dict(
                x=x + 0.47,
                y=y + 0.27,
                text=f"+{row[growth_col]:.0f}% YoY",
                showarrow=False,
                font=dict(size=FONT_SIZES['regular'], color=yoy_color, weight='bold')
            )
        )

        name_short = row[name_col] if len(row[name_col]) <= 22 else row[name_col][:22] + '…'
        annotations.append(
            dict(
                x=x + 0.47,
                y=y + 0.12,
                text=name_short,
                showarrow=False,
                font=dict(
                    size=FONT_SIZES['tiny'],
                    color=COLORS['text_tertiary'],
                    style='italic'
                )
            )
        )

    return annotations


def build_periodic_table_figure(
    df: pd.DataFrame,
    id_col: str = 'id',
    symbol_col: str = 'symbol',
    name_col: str = 'name',
    group_col: str = 'group',
    trend_col: str = 'trend',
    value_col: str = 'funding_billions',
    count_col: str = 'startup_count',
    growth_col: str = 'yoy_growth_pct',
    layout_positions: dict | None = None,
    title: str = 'The Periodic Table of AI Startups',
    subtitle: str = 'Reimagined • Funding, Startups & YoY Growth',
    width: int = 1200,
    height: int = 850
) -> go.Figure:
    """
    Genera una visualización de tabla periódica genérica.
    
    Args:
        df: DataFrame con los datos.
        id_col: Columna con el ID único de cada elemento.
        symbol_col: Columna con el símbolo a mostrar.
        name_col: Columna con el nombre completo.
        group_col: Columna con el grupo/categoría.
        trend_col: Columna con la tendencia.
        value_col: Columna con el valor principal (ej. funding).
        count_col: Columna con el conteo (ej. número de startups).
        growth_col: Columna con el porcentaje de crecimiento.
        layout_positions: Diccionario opcional {id: (x, y)} para posiciones personalizadas.
        title: Título principal del gráfico.
        subtitle: Subtítulo del gráfico.
        width: Ancho de la figura en píxeles.
        height: Alto de la figura en píxeles.
    
    Returns:
        Figura de Plotly lista para mostrar o exportar.
    """
    if layout_positions is None:
        layout_positions = {
            1: (0, 3), 2: (1, 3),
            3: (0, 2), 4: (1, 2), 5: (2, 2), 6: (3, 2),
            7: (0, 1), 8: (1, 1), 9: (2, 1), 10: (3, 1), 11: (4, 1),
            12: (0, 0), 13: (1, 0), 14: (2, 0)
        }

    shapes = _build_shapes(df, layout_positions, id_col, group_col)
    annotations = _build_annotations(
        df, layout_positions, id_col, symbol_col, name_col,
        trend_col, value_col, count_col, growth_col
    )

    fig = go.Figure()

    for group_key, label in GROUP_LABELS.items():
        fig.add_trace(
            go.Scatter(
                x=[None],
                y=[None],
                mode='markers',
                marker=dict(
                    size=16,
                    color=GROUP_COLORS[group_key],
                    line=dict(color=COLORS['border'], width=1.5)
                ),
                showlegend=True,
                name=label
            )
        )

    fig.update_layout(
        shapes=shapes,
        annotations=annotations + [
            dict(
                x=2.2,
                y=4.4,
                text=title,
                showarrow=False,
                font=dict(
                    size=FONT_SIZES['title'],
                    color=COLORS['text_primary'],
                    family=FONT_FAMILY,
                    weight='bold'
                )
            ),
            dict(
                x=2.2,
                y=4.2,
                text=subtitle,
                showarrow=False,
                font=dict(
                    size=FONT_SIZES['subtitle'],
                    color=COLORS['text_muted'],
                    family=FONT_FAMILY
                )
            )
        ],
        xaxis=dict(visible=False, range=[-0.5, 5]),
        yaxis=dict(visible=False, range=[-0.5, 4.7]),
        width=width,
        height=height,
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='center',
            x=0.5,
            bgcolor='rgba(255,255,255,0.7)',
            bordercolor=COLORS['border_light'],
            borderwidth=1
        ),
        margin=dict(l=30, r=30, t=40, b=30),
        paper_bgcolor=COLORS['background'],
        plot_bgcolor=COLORS['background']
    )

    fig.update_xaxes(fixedrange=True)
    fig.update_yaxes(fixedrange=True)

    return fig
