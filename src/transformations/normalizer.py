"""Funciones para normalización de texto y categorías."""
import pandas as pd


def trim_whitespace(
    df: pd.DataFrame,
    columns: list[str],
) -> pd.DataFrame:
    """
    Elimina espacios en blanco al inicio y final de columnas de texto.

    Args:
        df: DataFrame a transformar.
        columns: Lista de nombres de columnas de texto.

    Returns:
        DataFrame con espacios eliminados.
    """
    df_copy = df.copy()
    for col in columns:
        df_copy[col] = df_copy[col].str.strip()
    return df_copy


def replace_null_like(
    df: pd.DataFrame,
    columns: list[str],
    replacements: list[str] | None = None,
) -> pd.DataFrame:
    """
    Reemplaza valores tipo null (strings como 'NA', 'n/a') con NaN.

    Args:
        df: DataFrame a transformar.
        columns: Lista de nombres de columnas a procesar.
        replacements: Lista de valores a considerar como null (default común).

    Returns:
        DataFrame con valores null-like reemplazados por NaN.
    """
    if replacements is None:
        replacements = ["NA", "N/A", "n/a", "null", "NULL", "None", "-", ""]

    df_copy = df.copy()
    for col in columns:
        df_copy[col] = df_copy[col].replace(replacements, pd.NA)
    return df_copy


def standardize_categories(
    df: pd.DataFrame,
    column: str,
    mapping: dict[str, str],
) -> pd.DataFrame:
    """
    Estandariza valores categóricos usando un mapeo.

    Args:
        df: DataFrame a transformar.
        column: Nombre de la columna categórica.
        mapping: Diccionario {valor_original: valor_estandarizado}.

    Returns:
        DataFrame con categorías estandarizadas.
    """
    df_copy = df.copy()
    df_copy[column] = df_copy[column].replace(mapping)
    return df_copy


def normalize_column_names(
    df: pd.DataFrame,
    case: str = "lower",
    replace_spaces: str = "_",
) -> pd.DataFrame:
    """
    Normaliza nombres de columnas del DataFrame.

    Args:
        df: DataFrame a transformar.
        case: Transformación de mayúsculas ('lower', 'upper').
        replace_spaces: Carácter para reemplazar espacios (default '_').

    Returns:
        DataFrame con nombres de columnas normalizados.
    """
    df_copy = df.copy()
    columns = df_copy.columns.str.strip()

    if replace_spaces:
        columns = columns.str.replace(" ", replace_spaces)

    if case == "lower":
        columns = columns.str.lower()
    elif case == "upper":
        columns = columns.str.upper()

    df_copy.columns = columns
    return df_copy


def remove_special_chars(
    df: pd.DataFrame,
    columns: list[str],
    keep_pattern: str = r"[^a-zA-Z0-9\s]",
) -> pd.DataFrame:
    """
    Elimina caracteres especiales de columnas de texto.

    Args:
        df: DataFrame a transformar.
        columns: Lista de nombres de columnas de texto.
        keep_pattern: Patrón regex de caracteres a eliminar.

    Returns:
        DataFrame con caracteres especiales eliminados.
    """
    df_copy = df.copy()
    for col in columns:
        df_copy[col] = df_copy[col].str.replace(keep_pattern, "", regex=True)
    return df_copy
