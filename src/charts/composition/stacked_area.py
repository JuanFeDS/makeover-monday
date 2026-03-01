"""Gráfico de área apilada con Plotly."""
import plotly.graph_objects as go
import pandas as pd


def plot_stacked_area(
    df: pd.DataFrame,
    x: str,
    y: str,
    group: str,
    title: str = "Gráfico de Área Apilada",
    colors: list[str] | None = None,
) -> go.Figure:
    """
    Genera un gráfico de área apilada.

    Args:
        df: DataFrame con los datos.
        x: Nombre de la columna para el eje X.
        y: Nombre de la columna para el eje Y (valores).
        group: Nombre de la columna para separar las áreas.
        title: Título del gráfico.
        colors: Lista de colores para cada área (opcional).

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
                mode="lines",
                name=str(grp),
                stackgroup="one",
                fillcolor=color_map[idx % len(color_map)],
            )
        )

    fig.update_layout(
        title=title,
        xaxis_title=x,
        yaxis_title=y,
        template="plotly_white",
    )
    return fig
