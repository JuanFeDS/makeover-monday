"""Pruebas para funciones de imputación de datos."""
import pandas as pd

from src.transformations import (
    drop_missing,
    fill_with_mean,
    fill_with_median,
    fill_with_value,
    forward_fill_groups,
)


def test_fill_with_median_imputa_correspondiente():
    """Debe rellenar los nulos con la mediana de la columna."""
    df = pd.DataFrame({"valor": [1, None, 3]})
    resultado = fill_with_median(df, ["valor"])

    assert resultado["valor"].tolist() == [1, 2, 3]


def test_fill_with_mean():
    """Debe usar la media para imputar valores faltantes numéricos."""
    df = pd.DataFrame({"valor": [1, None, 4]})
    resultado = fill_with_mean(df, ["valor"])

    assert resultado["valor"].tolist() == [1, 2.5, 4]


def test_fill_with_value_personalizado():
    """Permite definir un valor fijo para completar categorías."""
    df = pd.DataFrame({"categoria": ["A", None, "B"]})
    resultado = fill_with_value(df, {"categoria": "Desconocido"})

    assert resultado["categoria"].tolist() == ["A", "Desconocido", "B"]


def test_forward_fill_groups():
    """Realiza forward fill dentro de cada grupo definido."""
    df = pd.DataFrame(
        {
            "grupo": ["A", "A", "B"],
            "valor": [1, None, 3],
        }
    )
    resultado = forward_fill_groups(df, ["grupo"], ["valor"])

    assert resultado["valor"].tolist() == [1, 1, 3]


def test_drop_missing_threshold():
    """Elimina filas que no cumplen con el umbral mínimo de datos."""
    df = pd.DataFrame({"a": [1, None], "b": [None, None]})
    resultado = drop_missing(df, threshold=0.5)

    assert len(resultado) == 1
