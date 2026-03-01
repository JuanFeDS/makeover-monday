"""Pruebas para gráficos de distribución."""
import pandas as pd

from src.charts.distribution.basic_hist import plot_histogram
from src.charts.distribution.grouped_box import plot_grouped_boxplot


def test_plot_histogram_crea_histograma():
    df = pd.DataFrame({"edad": [25, 30, 35]})

    fig = plot_histogram(df, column="edad", bins=5, title="Edades")

    assert fig.data[0].type == "histogram"
    assert fig.layout.title.text == "Edades"


def test_plot_grouped_boxplot_crea_trazas_por_segmento():
    df = pd.DataFrame(
        {
            "ingreso": [50, 60, 70, 80],
            "segmento": ["A", "A", "B", "B"],
        }
    )

    fig = plot_grouped_boxplot(df, y="ingreso", group="segmento")

    assert len(fig.data) == df["segmento"].nunique()
    assert all(trace.type == "box" for trace in fig.data)
