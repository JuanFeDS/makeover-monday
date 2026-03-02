"""Gráficos de caja (boxplot) para análisis de distribución."""
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

from src.config.styles import TREND_COLORS

def plot_category_boxplot(
    df: pd.DataFrame,
    category_col: str,
    value_col: str,
    category_order: list | None = None,
    color_map: dict | None = None,
    title: str = '',
    x_label: str | None = None,
    y_label: str | None = None,
    show_points: bool = True,
    width: int = 850,
    height: int = 600
) -> go.Figure:
    """
    Crea un boxplot agrupado por categoría.
    
    Args:
        df: DataFrame con los datos.
        category_col: Columna de categorías para el eje X.
        value_col: Columna de valores para el eje Y.
        category_order: Orden opcional de las categorías.
        color_map: Diccionario opcional de mapeo de colores por categoría.
        title: Título del gráfico.
        x_label: Etiqueta del eje X (por defecto usa category_col).
        y_label: Etiqueta del eje Y (por defecto usa value_col).
        show_points: Si mostrar puntos individuales sobre las cajas.
        width: Ancho de la figura en píxeles.
        height: Alto de la figura en píxeles.
    
    Returns:
        Figura de Plotly lista para mostrar o exportar.
    """
    if color_map is None:
        color_map = TREND_COLORS

    labels = {}
    if x_label:
        labels[category_col] = x_label
    if y_label:
        labels[value_col] = y_label

    category_orders = {}
    if category_order:
        category_orders[category_col] = category_order

    fig = px.box(
        df,
        x=category_col,
        y=value_col,
        category_orders=category_orders,
        color=category_col,
        color_discrete_map=color_map,
        points='all' if show_points else False,
        labels=labels,
        title=title
    )

    fig.update_traces(boxmean=True, jitter=0.2)

    fig.update_layout(
        showlegend=False,
        width=width,
        height=height,
        margin={
            'l': 40, 
            'r': 30, 
            't': 80, 
            'b': 40
        }
    )

    return fig
