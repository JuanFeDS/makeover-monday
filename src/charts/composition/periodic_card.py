"""Tarjeta individual que replica el layout de referencia compartido."""
from typing import Mapping

import pandas as pd
import plotly.graph_objects as go

from src.config import CARD_STYLE, TREND_COLORS, GROUP_COLORS

CARD_BG = CARD_STYLE['background']
DEFAULT_HEADER_COLOR = CARD_STYLE['header_color']
DEFAULT_BORDER_COLOR = CARD_STYLE['border_color']
DOT_COLOR = CARD_STYLE['dot_default']
LINE_COLOR = CARD_STYLE['line_color']
TEXT_COLOR = CARD_STYLE['text_color']
GROWTH_COLOR = CARD_STYLE['growth_color']
FONT_FAMILY = CARD_STYLE['font_family']
CARD_RADIUS = CARD_STYLE['card_radius']
WHITE_TOP = CARD_STYLE['white_top']
WHITE_BOTTOM = CARD_STYLE['white_bottom']
ROW1_RATIO = CARD_STYLE['row1_ratio']
ROW2_RATIO = CARD_STYLE['row2_ratio']

def _base_shapes(border_color: str, header_color: str) -> list[dict]:
    return [
        dict(
            type="path",
            path=(
                f"M{0.05 + CARD_RADIUS},{0.05} L{0.95 - CARD_RADIUS},{0.05} "
                f"Q{0.95},{0.05} {0.95},{0.05 + CARD_RADIUS} "
                f"L{0.95},{0.95 - CARD_RADIUS} "
                f"Q{0.95},{0.95} {0.95 - CARD_RADIUS},{0.95} "
                f"L{0.05 + CARD_RADIUS},{0.95} "
                f"Q{0.05},{0.95} {0.05},{0.95 - CARD_RADIUS} "
                f"L{0.05},{0.05 + CARD_RADIUS} "
                f"Q{0.05},{0.05} {0.05 + CARD_RADIUS},{0.05} Z"
            ),
            line=dict(color=border_color, width=4),
            fillcolor="white",
            layer="below"
        ),
        dict(
            type="path",
            path=(
                f"M{0.05},{WHITE_TOP} "
                f"L{0.05},{0.95 - CARD_RADIUS} "
                f"Q{0.05},{0.95} {0.05 + CARD_RADIUS},{0.95} "
                f"L{0.95 - CARD_RADIUS},{0.95} "
                f"Q{0.95},{0.95} {0.95},{0.95 - CARD_RADIUS} "
                f"L{0.95},{WHITE_TOP} Z"
            ),
            line=dict(width=0),
            fillcolor=header_color
        ),
        dict(type="circle", x0=0.85, y0=0.84, x1=0.90, y1=0.89,
             line=dict(width=0), fillcolor=DOT_COLOR),
    ]


def _to_series(record: pd.Series | Mapping) -> pd.Series:
    return record if isinstance(record, pd.Series) else pd.Series(record)


def build_periodic_card(
    record: pd.Series | Mapping,
    *,
    width: int = 300,
    height: int = 300
) -> go.Figure:
    """Construye una tarjeta única basada en los valores del registro."""
    row = _to_series(record)
    symbol = row.get("symbol", "").upper()
    name = row.get("name", "---")
    funding = row.get("funding_billions", 0)
    growth = row.get("yoy_growth_pct", 0)
    startups = row.get("startup_count", 0)
    trend = row.get("trend")
    group = row.get("group")

    fig = go.Figure()
    fig.update_layout(
        width=width,
        height=height,
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor=CARD_BG,
        plot_bgcolor=CARD_BG,
        font=dict(family=FONT_FAMILY)
    )
    fig.update_xaxes(range=[0, 1], visible=False)
    fig.update_yaxes(range=[0, 1], visible=False)

    dot_color = TREND_COLORS.get(trend, DOT_COLOR)
    group_color = GROUP_COLORS.get(group, DEFAULT_HEADER_COLOR)
    base_shapes = _base_shapes(
        border_color=GROUP_COLORS.get(group, DEFAULT_BORDER_COLOR),
        header_color=group_color
    )

    for shape in base_shapes:
        if shape.get("type") == "circle":
            fig.add_shape({**shape, "fillcolor": dot_color})
        else:
            fig.add_shape(shape)

    white_height = WHITE_TOP - WHITE_BOTTOM
    row1_bottom = WHITE_TOP - white_height * ROW1_RATIO
    row2_bottom = row1_bottom - white_height * ROW2_RATIO

    # Líneas horizontales entre filas
    for y in (row1_bottom, row2_bottom):
        fig.add_shape(
            type="line",
            x0=0.06,
            x1=0.94,
            y0=y,
            y1=y,
            line=dict(color=LINE_COLOR, width=1, dash="dot")
        )

    # Línea vertical en la segunda fila (dos columnas)
    fig.add_shape(
        type="line",
        x0=0.5,
        x1=0.5,
        y0=row1_bottom,
        y1=row2_bottom,
        line=dict(color=LINE_COLOR, width=1, dash="dot")
    )

    def _annotation(text: str, x: float, y: float, *, size: int,
                    color: str = TEXT_COLOR, bold: bool = True,
                    xanchor: str = "center") -> dict:
        content = f"<b>{text}</b>" if bold else text
        return dict(
            text=content,
            x=x,
            y=y,
            showarrow=False,
            font=dict(size=size, color=color, family=FONT_FAMILY),
            xanchor=xanchor,
            yanchor="middle"
        )

    row1_center = (WHITE_TOP + row1_bottom) / 2
    row2_center = (row1_bottom + row2_bottom) / 2
    row3_center = (row2_bottom + WHITE_BOTTOM) / 2

    def _rich_block(title: str, value: str, *, x: float, color: str = TEXT_COLOR) -> dict:
        text = (
            f"<b>{title}</b><br>"
            "<br>"
            f"""
                <span 
                    style='display:inline-block;
                    padding-top:20px;
                    font-size:20px;
                    color:{color}'
                >
                    {value}
                </span>
            """
        )
        return dict(
            text=text,
            x=x,
            y=row2_center,
            showarrow=False,
            align="center",
            font=dict(size=12, color=TEXT_COLOR, family=FONT_FAMILY)
        )

    annotations = [
        _annotation(symbol, 0.09, 0.84, size=22, color="white", xanchor="left"),
        _annotation(name, 0.5, row1_center, size=15, color=TEXT_COLOR),
        _rich_block("Financiación", f"{funding:.0f} B", x=0.3, color="#111111"),
        _rich_block("% crec. anual", f"{growth:.0f}%", x=0.7, color=GROWTH_COLOR),
        dict(
            text=(
                "<b>Cant. Startups</b><br>"
                "<br>"
                f"""
                    <span 
                        style='display:inline-block;
                        padding-top:20px;
                        font-size:20px;
                        color:{TEXT_COLOR}'
                    >
                        {startups}
                    </span>
                """
            ),
            x=0.5,
            y=row3_center,
            showarrow=False,
            align="center",
            font=dict(size=12, color=TEXT_COLOR, family=FONT_FAMILY)
        )
    ]

    fig.update_layout(annotations=annotations)
    return fig
