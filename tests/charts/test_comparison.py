"""Pruebas para gráficos de comparación."""
import pandas as pd

from src.charts.comparison.basic_bar import plot_basic_bar
from src.charts.comparison.grouped_bar import plot_grouped_bar
from src.charts.comparison.multi_line import plot_multi_line


def test_plot_basic_bar_crea_traza_bar():
    df = pd.DataFrame({"categoria": ["A", "B"], "valor": [10, 20]})

    fig = plot_basic_bar(df, x="categoria", y="valor", title="Test")

    assert fig.data[0].type == "bar"
    assert fig.layout.title.text == "Test"


def test_plot_grouped_bar_agrega_una_traza_por_grupo():
    df = pd.DataFrame(
        {
            "categoria": ["A", "A", "B", "B"],
            "valor": [10, 12, 20, 22],
            "grupo": ["2024", "2025", "2024", "2025"],
        }
    )

    fig = plot_grouped_bar(df, x="categoria", y="valor", group="grupo")

    assert len(fig.data) == df["grupo"].nunique()
    assert fig.layout.barmode == "group"


def test_plot_multi_line_crea_trazas_por_region():
    df = pd.DataFrame(
        {
            "mes": ["Ene", "Ene", "Feb", "Feb"],
            "valor": [10, 8, 15, 12],
            "region": ["Norte", "Sur", "Norte", "Sur"],
        }
    )

    fig = plot_multi_line(df, x="mes", y="valor", group="region")

    assert len(fig.data) == df["region"].nunique()
    assert all(trace.mode == "lines+markers" for trace in fig.data)
