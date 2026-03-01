"""Funciones para conversión de tipos de datos."""
import pandas as pd


def coerce_numeric(
    df: pd.DataFrame,
    columns: list[str],
    errors: str = "coerce",
) -> pd.DataFrame:
    """
    Convierte columnas a tipo numérico.

    Args:
        df: DataFrame a transformar.
        columns: Lista de nombres de columnas a convertir.
        errors: Estrategia para valores inválidos ('coerce', 'raise', 'ignore').

    Returns:
        DataFrame con columnas convertidas a numéricas.
    """
    df_copy = df.copy()
    for col in columns:
        df_copy[col] = pd.to_numeric(df_copy[col], errors=errors)
    return df_copy


def parse_dates(
    df: pd.DataFrame,
    columns: list[str],
    dayfirst: bool = True,
    format_date: str | None = None,
) -> pd.DataFrame:
    """
    Convierte columnas a tipo datetime.

    Args:
        df: DataFrame a transformar.
        columns: Lista de nombres de columnas a convertir.
        dayfirst: Si True, interpreta fechas como DD/MM/YYYY.
        format_date: Formato específico de fecha (opcional).

    Returns:
        DataFrame con columnas convertidas a datetime.
    """
    df_copy = df.copy()
    for col in columns:
        df_copy[col] = pd.to_datetime(
            df_copy[col],
            dayfirst=dayfirst,
            format=format_date,
            errors="coerce",
        )
    return df_copy


def standardize_text(
    df: pd.DataFrame,
    columns: list[str],
    case: str = "lower",
    strip: bool = True,
) -> pd.DataFrame:
    """
    Normaliza columnas de texto.

    Args:
        df: DataFrame a transformar.
        columns: Lista de nombres de columnas a normalizar.
        case: Transformación de mayúsculas ('lower', 'upper', 'title').
        strip: Si True, elimina espacios al inicio y final.

    Returns:
        DataFrame con columnas de texto normalizadas.
    """
    df_copy = df.copy()
    for col in columns:
        if strip:
            df_copy[col] = df_copy[col].str.strip()
        if case == "lower":
            df_copy[col] = df_copy[col].str.lower()
        elif case == "upper":
            df_copy[col] = df_copy[col].str.upper()
        elif case == "title":
            df_copy[col] = df_copy[col].str.title()
    return df_copy


def convert_to_category(
    df: pd.DataFrame,
    columns: list[str],
) -> pd.DataFrame:
    """
    Convierte columnas a tipo category para optimizar memoria.

    Args:
        df: DataFrame a transformar.
        columns: Lista de nombres de columnas a convertir.

    Returns:
        DataFrame con columnas convertidas a category.
    """
    df_copy = df.copy()
    for col in columns:
        df_copy[col] = df_copy[col].astype("category")
    return df_copy
