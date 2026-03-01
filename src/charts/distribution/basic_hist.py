"""Histograma básico con Plotly."""
import plotly.graph_objects as go
import pandas as pd


def plot_histogram(
    df: pd.DataFrame,
    column: str,
    title: str = "Histograma",
    bins: int = 30,
    color: str = "#636EFA",
) -> go.Figure:
    """
    Genera un histograma básico.

    Args:
        df: DataFrame con los datos.
        column: Nombre de la columna a visualizar.
        title: Título del gráfico.
        bins: Número de bins para el histograma.
        color: Color de las barras.

    Returns:
        Figura de Plotly lista para mostrar o exportar.
    """
    fig = go.Figure(
        data=[
            go.Histogram(
                x=df[column],
                nbinsx=bins,
                marker_color=color,
            )
        ]
    )
    fig.update_layout(
        title=title,
        xaxis_title=column,
        yaxis_title="Frecuencia",
        template="plotly_white",
    )
    return fig
