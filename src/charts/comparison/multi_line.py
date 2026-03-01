"""Gráfico de líneas múltiples con Plotly."""
import plotly.graph_objects as go
import pandas as pd


def plot_multi_line(
    df: pd.DataFrame,
    x: str,
    y: str,
    group: str,
    title: str = "Gráfico de Líneas Múltiples",
    colors: list[str] | None = None,
) -> go.Figure:
    """
    Genera un gráfico de líneas múltiples.

    Args:
        df: DataFrame con los datos.
        x: Nombre de la columna para el eje X.
        y: Nombre de la columna para el eje Y (valores).
        group: Nombre de la columna para separar las líneas.
        title: Título del gráfico.
        colors: Lista de colores para cada línea (opcional).

    Returns:
        Figura de Plotly lista para mostrar o exportar.
    """
    fig = go.Figure()
    groups = df[group].unique()
    default_colors = ["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A"]
    color_map = colors or default_colors

    for idx, grp in enumerate(groups):
        subset = df[df[group] == grp]
        fig.add_trace(
            go.Scatter(
                x=subset[x],
                y=subset[y],
                mode="lines+markers",
                name=str(grp),
                line=dict(color=color_map[idx % len(color_map)]),
            )
        )

    fig.update_layout(
        title=title,
        xaxis_title=x,
        yaxis_title=y,
        template="plotly_white",
    )
    return fig
