"""Pruebas para funciones de conversión de tipos."""
import pandas as pd

from src.transformations import (
    coerce_numeric,
    convert_to_category,
    parse_dates,
    standardize_text,
)


def test_coerce_numeric_convierte_columnas():
    df = pd.DataFrame({"valor": ["1", "2", "3"], "texto": ["a", "b", "c"]})
    resultado = coerce_numeric(df, ["valor"])

    assert pd.api.types.is_numeric_dtype(resultado["valor"])
    assert resultado.equals(df.assign(valor=[1, 2, 3]))


def test_parse_dates_respeta_formato():
    df = pd.DataFrame({"fecha": ["25/02/2026"]})
    resultado = parse_dates(df, ["fecha"], dayfirst=True, format_date="%d/%m/%Y")

    assert resultado["fecha"].dt.year.iloc[0] == 2026
    assert resultado["fecha"].notna().all()


def test_standardize_text_aplica_minusc_y_strip():
    df = pd.DataFrame({"categoria": ["  Ventas  ", "Marketing"]})
    resultado = standardize_text(df, ["categoria"], case="lower", strip=True)

    assert resultado.loc[0, "categoria"] == "ventas"
    assert resultado.loc[1, "categoria"] == "marketing"


def test_convert_to_category_optimiza_memoria():
    df = pd.DataFrame({"segmento": ["A", "B", "A"]})
    resultado = convert_to_category(df, ["segmento"])

    assert pd.api.types.is_categorical_dtype(resultado["segmento"])
    assert list(resultado["segmento"].cat.categories) == ["A", "B"]
