"""Gráficos treemap para visualización de composición jerárquica."""
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

from src.config.styles import TREND_COLORS, FONT_FAMILY

def plot_hierarchical_treemap(
    df: pd.DataFrame,
    path_cols: list[str],
    value_col: str,
    color_col: str | None = None,
    color_map: dict | None = None,
    title: str = '',
    width: int = 900,
    height: int = 600
) -> go.Figure:
    """
    Crea un treemap jerárquico para visualizar composición.
    
    Args:
        df: DataFrame con los datos.
        path_cols: Lista de columnas que definen la jerarquía (de mayor a menor nivel).
        value_col: Columna con los valores numéricos para el tamaño de cada rectángulo.
        color_col: Columna opcional para colorear por categoría.
        color_map: Diccionario opcional de mapeo de colores.
        title: Título del gráfico.
        width: Ancho de la figura en píxeles.
        height: Alto de la figura en píxeles.
    
    Returns:
        Figura de Plotly lista para mostrar o exportar.
    """
    if color_map is None:
        color_map = TREND_COLORS

    hover_data = {value_col: ':.1f'}

    fig = px.treemap(
        df,
        path=path_cols,
        values=value_col,
        color=color_col if color_col else path_cols[0],
        color_discrete_map=color_map,
        hover_data=hover_data,
        title=title
    )

    fig.update_traces(
        texttemplate='%{label}<br>$%{value:.1f}B',
        textfont={
            'size': 16, 
            'color': 'white', 
            'family': FONT_FAMILY
        },
        marker={
            'line': {
                'color': 'white', 
                'width': 3
            }
        }
    )

    fig.update_layout(
        width=width,
        height=height,
        margin={
            'l': 0, 
            'r': 0, 
            't': 80, 
            'b': 20
        }
    )

    return fig
