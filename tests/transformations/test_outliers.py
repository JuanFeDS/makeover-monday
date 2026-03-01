"""Pruebas para manejo de outliers."""
import pandas as pd

from src.transformations import (
    cap_outliers_iqr,
    detect_outliers_iqr,
    detect_outliers_zscore,
    remove_outliers,
    winsorize_column,
)


def _df_outliers():
    return pd.DataFrame({"valor": [1, 2, 3, 100]})


def test_detect_outliers_iqr_identifica_valores_extremos():
    df = _df_outliers()
    mask = detect_outliers_iqr(df, "valor")

    assert mask.tolist() == [False, False, False, True]


def test_detect_outliers_zscore_identifica_valores_extremos():
    df = _df_outliers()
    mask = detect_outliers_zscore(df, "valor", threshold=1.0)

    assert mask.tolist() == [False, False, False, True]


def test_winsorize_column_limita_extremos():
    df = _df_outliers()
    resultado = winsorize_column(df, "valor", limits=(0.0, 0.75))

    assert resultado["valor"].max() < 100


def test_cap_outliers_iqr_clipea_valores():
    df = _df_outliers()
    resultado = cap_outliers_iqr(df, "valor", multiplier=1.5)

    assert resultado["valor"].max() < 100


def test_remove_outliers_elimina_filas_extremas():
    df = _df_outliers()
    resultado = remove_outliers(df, "valor", method="iqr")

    assert len(resultado) == 3
