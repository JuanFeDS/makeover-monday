"""Pruebas para normalización de texto y categorías."""
import pandas as pd

from src.transformations import (
    normalize_column_names,
    remove_special_chars,
    replace_null_like,
    standardize_categories,
    trim_whitespace,
)


def test_trim_whitespace_elimina_espacios():
    df = pd.DataFrame({"col": ["  dato ", "valor"]})
    resultado = trim_whitespace(df, ["col"])

    assert resultado["col"].tolist() == ["dato", "valor"]


def test_replace_null_like_convierte_a_na():
    df = pd.DataFrame({"col": ["NA", "dato"]})
    resultado = replace_null_like(df, ["col"])

    assert resultado["col"].isna().sum() == 1


def test_standardize_categories_aplica_mapping():
    df = pd.DataFrame({"segmento": ["ventas", "MKT"]})
    mapping = {"ventas": "Ventas", "MKT": "Marketing"}
    resultado = standardize_categories(df, "segmento", mapping)

    assert resultado["segmento"].tolist() == ["Ventas", "Marketing"]


def test_normalize_column_names():
    df = pd.DataFrame({"Nombre Cliente": ["A"]})
    resultado = normalize_column_names(df, case="lower", replace_spaces="_")

    assert "nombre_cliente" in resultado.columns


def test_remove_special_chars_limita_caracteres():
    df = pd.DataFrame({"col": ["Dato$#1", "Dato 2"]})
    resultado = remove_special_chars(df, ["col"], keep_pattern=r"[^a-zA-Z0-9\s]")

    assert resultado["col"].tolist() == ["Dato1", "Dato 2"]
