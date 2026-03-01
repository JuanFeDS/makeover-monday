"""Boxplot agrupado con Plotly."""
import plotly.graph_objects as go
import pandas as pd


def plot_grouped_boxplot(
    df: pd.DataFrame,
    y: str,
    group: str,
    title: str = "Boxplot Agrupado",
    colors: list[str] | None = None,
) -> go.Figure:
    """
    Genera un boxplot agrupado por categoría.

    Args:
        df: DataFrame con los datos.
        y: Nombre de la columna con valores numéricos.
        group: Nombre de la columna para agrupar.
        title: Título del gráfico.
        colors: Lista de colores para cada grupo (opcional).

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
            go.Box(
                y=subset[y],
                name=str(grp),
                marker_color=color_map[idx % len(color_map)],
            )
        )

    fig.update_layout(
        title=title,
        yaxis_title=y,
        template="plotly_white",
    )
    return fig
