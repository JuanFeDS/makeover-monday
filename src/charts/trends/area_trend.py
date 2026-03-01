"""Gráfico de área para tendencias con Plotly."""
import pandas as pd
import plotly.graph_objects as go


def plot_area_trend(
    df: pd.DataFrame,
    x: str,
    y: str,
    title: str = "Tendencia de Área",
    color: str = "#636EFA",
    fill_opacity: float = 0.5,
) -> go.Figure:
    """
    Genera un gráfico de área simple para visualizar tendencias.

    Args:
        df: DataFrame con los datos.
        x: Nombre de la columna para el eje X.
        y: Nombre de la columna para el eje Y (valores).
        title: Título del gráfico.
        color: Color del área.
        fill_opacity: Opacidad del relleno (0 a 1).

    Returns:
        Figura de Plotly lista para mostrar o exportar.
    """
    fig = go.Figure(
        data=[
            go.Scatter(
                x=df[x],
                y=df[y],
                mode="lines",
                fill="tozeroy",
                fillcolor=color,
                line=dict(color=color),
                opacity=fill_opacity,
            )
        ]
    )
    fig.update_layout(
        title=title,
        xaxis_title=x,
        yaxis_title=y,
        template="plotly_white",
    )
    return fig
