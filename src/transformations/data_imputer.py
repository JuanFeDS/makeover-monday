"""Funciones para imputación de valores faltantes."""
import pandas as pd


def fill_with_median(
    df: pd.DataFrame,
    columns: list[str],
) -> pd.DataFrame:
    """
    Rellena valores faltantes con la mediana de cada columna.

    Args:
        df: DataFrame a transformar.
        columns: Lista de nombres de columnas numéricas a imputar.

    Returns:
        DataFrame con valores faltantes imputados con la mediana.
    """
    df_copy = df.copy()
    for col in columns:
        df_copy[col] = df_copy[col].fillna(df_copy[col].median())
    return df_copy


def fill_with_mean(
    df: pd.DataFrame,
    columns: list[str],
) -> pd.DataFrame:
    """
    Rellena valores faltantes con la media de cada columna.

    Args:
        df: DataFrame a transformar.
        columns: Lista de nombres de columnas numéricas a imputar.

    Returns:
        DataFrame con valores faltantes imputados con la media.
    """
    df_copy = df.copy()
    for col in columns:
        df_copy[col] = df_copy[col].fillna(df_copy[col].mean())
    return df_copy


def fill_with_value(
    df: pd.DataFrame,
    mapping: dict[str, any],
) -> pd.DataFrame:
    """
    Rellena valores faltantes con valores específicos por columna.

    Args:
        df: DataFrame a transformar.
        mapping: Diccionario {columna: valor} para imputación.

    Returns:
        DataFrame con valores faltantes imputados según el mapping.
    """
    df_copy = df.copy()
    for col, value in mapping.items():
        df_copy[col] = df_copy[col].fillna(value)
    return df_copy


def forward_fill_groups(
    df: pd.DataFrame,
    group_cols: list[str],
    target_cols: list[str],
) -> pd.DataFrame:
    """
    Aplica forward fill dentro de grupos específicos.

    Args:
        df: DataFrame a transformar.
        group_cols: Columnas para agrupar.
        target_cols: Columnas donde aplicar forward fill.

    Returns:
        DataFrame con valores imputados por grupo.
    """
    df_copy = df.copy()
    df_copy[target_cols] = df_copy.groupby(group_cols)[target_cols].ffill()
    return df_copy


def drop_missing(
    df: pd.DataFrame,
    columns: list[str] | None = None,
    threshold: float | None = None,
) -> pd.DataFrame:
    """
    Elimina filas con valores faltantes.

    Args:
        df: DataFrame a transformar.
        columns: Columnas a considerar (None = todas).
        threshold: Porcentaje mínimo de valores no nulos requerido (0-1).

    Returns:
        DataFrame sin filas con valores faltantes según criterio.
    """
    df_copy = df.copy()
    if threshold is not None:
        thresh_count = int(threshold * len(df_copy.columns))
        df_copy = df_copy.dropna(thresh=thresh_count)
    elif columns:
        df_copy = df_copy.dropna(subset=columns)
    else:
        df_copy = df_copy.dropna()
    return df_copy
