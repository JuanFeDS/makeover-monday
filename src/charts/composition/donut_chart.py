"""Gráfico de dona (donut) con Plotly."""
import plotly.graph_objects as go
import pandas as pd


def plot_donut(
    df: pd.DataFrame,
    labels: str,
    values: str,
    title: str = "Gráfico de Dona",
    colors: list[str] | None = None,
    hole_size: float = 0.4,
) -> go.Figure:
    """
    Genera un gráfico de dona (pie chart con hueco central).

    Args:
        df: DataFrame con los datos.
        labels: Nombre de la columna con las etiquetas.
        values: Nombre de la columna con los valores.
        title: Título del gráfico.
        colors: Lista de colores para cada segmento (opcional).
        hole_size: Tamaño del hueco central (0 a 1).

    Returns:
        Figura de Plotly lista para mostrar o exportar.
    """
    fig = go.Figure(
        data=[
            go.Pie(
                labels=df[labels],
                values=df[values],
                hole=hole_size,
                marker=dict(colors=colors) if colors else None,
            )
        ]
    )
    fig.update_layout(
        title=title,
        template="plotly_white",
    )
    return fig
