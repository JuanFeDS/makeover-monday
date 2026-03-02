"""Gráficos de dispersión para análisis de relaciones."""
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

def plot_scatter_with_size(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    size_col: str,
    color_col: str,
    text_col: str | None = None,
    color_map: dict | None = None,
    title: str = '',
    x_label: str | None = None,
    y_label: str | None = None,
    size_max: int = 80,
    width: int = 950,
    height: int = 650
) -> go.Figure:
    """
    Crea un scatter plot con tamaño variable y colores por categoría.
    
    Args:
        df: DataFrame con los datos.
        x_col: Columna para el eje X.
        y_col: Columna para el eje Y.
        size_col: Columna para el tamaño de los puntos.
        color_col: Columna para el color de los puntos.
        text_col: Columna opcional para etiquetas de texto en los puntos.
        color_map: Diccionario opcional de mapeo de colores por categoría.
        title: Título del gráfico.
        x_label: Etiqueta del eje X (por defecto usa x_col).
        y_label: Etiqueta del eje Y (por defecto usa y_col).
        size_max: Tamaño máximo de los puntos.
        width: Ancho de la figura en píxeles.
        height: Alto de la figura en píxeles.
    
    Returns:
        Figura de Plotly lista para mostrar o exportar.
    """
    if color_map is None:
        color_map = TREND_COLORS

    labels = {}
    if x_label:
        labels[x_col] = x_label
    if y_label:
        labels[y_col] = y_label

    hover_data = {
        x_col: True,
        y_col: ':.1f' if df[y_col].dtype in ['float64', 'float32'] else True,
        size_col: True
    }

    fig = px.scatter(
        df,
        x=x_col,
        y=y_col,
        size=size_col,
        color=color_col,
        color_discrete_map=color_map,
        size_max=size_max,
        text=text_col,
        hover_data=hover_data,
        labels=labels,
        title=title
    )

    fig.update_traces(
        marker=dict(line=dict(width=1.5, color='black'), opacity=0.7),
        textposition='middle center'
    )

    fig.update_layout(
        legend_title=color_col.replace('_', ' ').title(),
        width=width,
        height=height,
        margin={
            'l': 40, 
            'r': 40, 
            't': 90, 
            'b': 50
        }
    )

    return fig
