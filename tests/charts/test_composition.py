"""Pruebas para gráficos de composición."""
import pandas as pd

from src.charts.composition.donut_chart import plot_donut
from src.charts.composition.stacked_area import plot_stacked_area


def test_plot_donut_generates_pie_trace():
    df = pd.DataFrame(
        {
            "segmento": ["A", "B", "C"],
            "participacion": [40, 35, 25],
        }
    )

    fig = plot_donut(df, labels="segmento", values="participacion", title="Participación")

    assert fig.data[0].type == "pie"
    assert fig.layout.title.text == "Participación"
    assert fig.data[0]["hole"] > 0


def test_plot_stacked_area_crea_trazas_apiladas():
    df = pd.DataFrame(
        {
            "anio": ["2024", "2025", "2024", "2025"],
            "valor": [30, 40, 20, 25],
            "canal": ["Online", "Online", "Retail", "Retail"],
        }
    )

    fig = plot_stacked_area(df, x="anio", y="valor", group="canal")

    assert len(fig.data) == df["canal"].nunique()
    assert all(trace.stackgroup == "one" for trace in fig.data)
