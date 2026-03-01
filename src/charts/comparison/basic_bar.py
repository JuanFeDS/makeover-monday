"""Gráfico de barras básico con Plotly."""
import pandas as pd
import plotly.graph_objects as go


def plot_basic_bar(
    df: pd.DataFrame,
    x: str,
    y: str,
    title: str = "Gráfico de Barras",
    color: str = "#636EFA",
    orientation: str = "v",
) -> go.Figure:
    """
    Genera un gráfico de barras básico.

    Args:
        df: DataFrame con los datos.
        x: Nombre de la columna para el eje X.
        y: Nombre de la columna para el eje Y.
        title: Título del gráfico.
        color: Color de las barras (hex o nombre).
        orientation: 'v' para vertical, 'h' para horizontal.

    Returns:
        Figura de Plotly lista para mostrar o exportar.
    """
    fig = go.Figure(
        data=[
            go.Bar(
                x=df[x] if orientation == "v" else df[y],
                y=df[y] if orientation == "v" else df[x],
                marker_color=color,
                orientation=orientation,
            )
        ]
    )
    fig.update_layout(
        title=title,
        xaxis_title=x if orientation == "v" else y,
        yaxis_title=y if orientation == "v" else x,
        template="plotly_white",
    )
    return fig
