"""Funciones para detección y tratamiento de outliers."""
import pandas as pd
import numpy as np


def detect_outliers_iqr(
    df: pd.DataFrame,
    column: str,
    multiplier: float = 1.5,
) -> pd.Series:
    """
    Detecta outliers usando el método IQR (Rango Intercuartílico).

    Args:
        df: DataFrame a analizar.
        column: Nombre de la columna numérica.
        multiplier: Multiplicador del IQR para definir límites (default 1.5).

    Returns:
        Serie booleana indicando si cada valor es outlier.
    """
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - multiplier * iqr
    upper_bound = q3 + multiplier * iqr
    return (df[column] < lower_bound) | (df[column] > upper_bound)


def detect_outliers_zscore(
    df: pd.DataFrame,
    column: str,
    threshold: float = 3.0,
) -> pd.Series:
    """
    Detecta outliers usando Z-score.

    Args:
        df: DataFrame a analizar.
        column: Nombre de la columna numérica.
        threshold: Umbral de desviaciones estándar (default 3).

    Returns:
        Serie booleana indicando si cada valor es outlier.
    """
    z_scores = np.abs((df[column] - df[column].mean()) / df[column].std())
    return z_scores > threshold


def winsorize_column(
    df: pd.DataFrame,
    column: str,
    limits: tuple[float, float] = (0.05, 0.95),
) -> pd.DataFrame:
    """
    Aplica winsorización a una columna (reemplaza extremos con percentiles).

    Args:
        df: DataFrame a transformar.
        column: Nombre de la columna numérica.
        limits: Tupla (percentil_inferior, percentil_superior).

    Returns:
        DataFrame con valores extremos winzorizados.
    """
    df_copy = df.copy()
    lower = df_copy[column].quantile(limits[0])
    upper = df_copy[column].quantile(limits[1])
    df_copy[column] = df_copy[column].clip(lower=lower, upper=upper)
    return df_copy


def cap_outliers_iqr(
    df: pd.DataFrame,
    column: str,
    multiplier: float = 1.5,
) -> pd.DataFrame:
    """
    Reemplaza outliers con los límites del IQR.

    Args:
        df: DataFrame a transformar.
        column: Nombre de la columna numérica.
        multiplier: Multiplicador del IQR para definir límites.

    Returns:
        DataFrame con outliers limitados a los bounds del IQR.
    """
    df_copy = df.copy()
    q1 = df_copy[column].quantile(0.25)
    q3 = df_copy[column].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - multiplier * iqr
    upper_bound = q3 + multiplier * iqr
    df_copy[column] = df_copy[column].clip(lower=lower_bound, upper=upper_bound)
    return df_copy


def remove_outliers(
    df: pd.DataFrame,
    column: str,
    method: str = "iqr",
    **kwargs,
) -> pd.DataFrame:
    """
    Elimina filas con outliers según el método especificado.

    Args:
        df: DataFrame a transformar.
        column: Nombre de la columna numérica.
        method: Método de detección ('iqr' o 'zscore').
        **kwargs: Argumentos adicionales para el método de detección.

    Returns:
        DataFrame sin filas que contienen outliers.
    """
    if method == "iqr":
        mask = detect_outliers_iqr(df, column, **kwargs)
    elif method == "zscore":
        mask = detect_outliers_zscore(df, column, **kwargs)
    else:
        raise ValueError("Método debe ser 'iqr' o 'zscore'")
    return df[~mask]
