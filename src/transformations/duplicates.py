"""Funciones para manejo de duplicados."""
import pandas as pd


def drop_full_duplicates(
    df: pd.DataFrame,
    keep: str = "first",
) -> pd.DataFrame:
    """
    Elimina filas completamente duplicadas.

    Args:
        df: DataFrame a transformar.
        keep: Qué duplicado mantener ('first', 'last', False para eliminar todos).

    Returns:
        DataFrame sin duplicados completos.
    """
    return df.drop_duplicates(keep=keep)


def drop_subset_duplicates(
    df: pd.DataFrame,
    subset: list[str],
    keep: str = "first",
) -> pd.DataFrame:
    """
    Elimina duplicados basándose en un subconjunto de columnas.

    Args:
        df: DataFrame a transformar.
        subset: Lista de columnas a considerar para detectar duplicados.
        keep: Qué duplicado mantener ('first', 'last', False para eliminar todos).

    Returns:
        DataFrame sin duplicados en el subset especificado.
    """
    return df.drop_duplicates(subset=subset, keep=keep)


def flag_duplicates(
    df: pd.DataFrame,
    subset: list[str] | None = None,
    keep: str = "first",
) -> pd.DataFrame:
    """
    Añade una columna booleana indicando si la fila es duplicada.

    Args:
        df: DataFrame a transformar.
        subset: Columnas a considerar (None = todas).
        keep: Qué duplicado marcar como False ('first', 'last', False marca todos).

    Returns:
        DataFrame con columna 'is_duplicate' agregada.
    """
    df_copy = df.copy()
    df_copy["is_duplicate"] = df_copy.duplicated(subset=subset, keep=keep)
    return df_copy


def count_duplicates(
    df: pd.DataFrame,
    subset: list[str] | None = None,
) -> pd.DataFrame:
    """
    Cuenta cuántas veces aparece cada combinación de valores.

    Args:
        df: DataFrame a analizar.
        subset: Columnas a considerar (None = todas).

    Returns:
        DataFrame con conteos de duplicados ordenados descendentemente.
    """
    if subset:
        df_count = df.groupby(subset).size().reset_index(name="count")
        df_count = df_count.sort_values("count", ascending=False)
        return df_count
    return df.value_counts().reset_index(name="count")
