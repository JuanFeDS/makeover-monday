"""Pruebas para manejo de duplicados."""
import pandas as pd

from src.transformations import (
    count_duplicates,
    drop_full_duplicates,
    drop_subset_duplicates,
    flag_duplicates,
)


def _sample_df():
    return pd.DataFrame(
        {
            "id": [1, 1, 2, 2, 3],
            "tipo": ["A", "A", "B", "B", "C"],
            "valor": [10, 10, 20, 21, 30],
        }
    )


def test_drop_full_duplicates_elimina_repetidos_totales():
    df = _sample_df()
    resultado = drop_full_duplicates(df)

    assert len(resultado) == 4
    assert resultado["valor"].tolist() == [10, 20, 21, 30]


def test_drop_subset_duplicates_considerando_subset():
    df = _sample_df()
    resultado = drop_subset_duplicates(df, ["id", "tipo"])

    assert len(resultado) == 3
    assert resultado["id"].tolist() == [1, 2, 3]


def test_flag_duplicates_agrega_columna():
    df = _sample_df()
    resultado = flag_duplicates(df, subset=["id", "tipo"], keep="first")

    assert "is_duplicate" in resultado.columns
    assert resultado["is_duplicate"].tolist() == [False, True, False, True, False]


def test_count_duplicates_retorna_conteos_ordenados():
    df = _sample_df()
    conteos = count_duplicates(df, subset=["id", "tipo"])

    assert list(conteos["count"]) == [2, 2, 1]
    assert conteos.iloc[0]["id"] == 1
