"""Módulo de transformaciones para limpieza de datos."""

from .type_converter import (
    coerce_numeric,
    parse_dates,
    standardize_text,
    convert_to_category,
)
from .data_imputer import (
    fill_with_median,
    fill_with_mean,
    fill_with_value,
    forward_fill_groups,
    drop_missing,
)
from .duplicates import (
    drop_full_duplicates,
    drop_subset_duplicates,
    flag_duplicates,
    count_duplicates,
)
from .outliers import (
    detect_outliers_iqr,
    detect_outliers_zscore,
    winsorize_column,
    cap_outliers_iqr,
    remove_outliers,
)
from .normalizer import (
    trim_whitespace,
    replace_null_like,
    standardize_categories,
    normalize_column_names,
    remove_special_chars,
)

__all__ = [
    "coerce_numeric",
    "parse_dates",
    "standardize_text",
    "convert_to_category",
    "fill_with_median",
    "fill_with_mean",
    "fill_with_value",
    "forward_fill_groups",
    "drop_missing",
    "drop_full_duplicates",
    "drop_subset_duplicates",
    "flag_duplicates",
    "count_duplicates",
    "detect_outliers_iqr",
    "detect_outliers_zscore",
    "winsorize_column",
    "cap_outliers_iqr",
    "remove_outliers",
    "trim_whitespace",
    "replace_null_like",
    "standardize_categories",
    "normalize_column_names",
    "remove_special_chars",
]
