"""Estilos y temas visuales centralizados para MakeOverMonday."""
import plotly.graph_objects as go

GROUP_COLORS = {
    'foundation': '#E8D5F2',
    'horizontal': '#D5F2E8',
    'vertical': '#FFE5CC',
    'emerging': '#FFD5D5'
}

TREND_COLORS = {
    'Explosive': '#FF6B35',
    'Rising': '#4ECDC4',
    'Steady': '#F7B801',
    'Mature': '#95389E'
}

TREND_ICONS = {
    'Explosive': '🔥',
    'Rising': '📈',
    'Steady': '➡️',
    'Mature': '🔵'
}

GROUP_LABELS = {
    'foundation': 'Foundation Layer',
    'horizontal': 'Horizontal AI',
    'vertical': 'Vertical AI',
    'emerging': 'Emerging & Frontier'
}

FONT_FAMILY = 'Nunito'

FONT_SIZES = {
    'title': 26,
    'subtitle': 16,
    'large': 20,
    'medium': 14,
    'regular': 13,
    'small': 12,
    'tiny': 10
}

COLORS = {
    'text_primary': '#111111',
    'text_secondary': '#1F1F1F',
    'text_tertiary': '#444444',
    'text_muted': '#555555',
    'text_light': '#666666',
    'text_subtle': '#4F4F4F',
    'border': '#333333',
    'border_light': '#DDDDDD',
    'background': 'white',
    'yoy_high': '#D32F2F',
    'yoy_medium': '#388E3C',
    'yoy_low': '#F57C00'
}

YOY_THRESHOLDS = {
    'high': 200,
    'medium': 125
}

DEFAULT_LAYOUT = {
    'paper_bgcolor': 'white',
    'plot_bgcolor': 'white',
    'font': {'family': FONT_FAMILY, 'size': 12},
    'margin': {'l': 40, 'r': 40, 't': 80, 'b': 50}
}


def get_yoy_color(yoy_growth_pct: float) -> str:
    """Determina el color según el porcentaje de crecimiento YoY."""
    if yoy_growth_pct >= YOY_THRESHOLDS['high']:
        return COLORS['yoy_high']
    elif yoy_growth_pct >= YOY_THRESHOLDS['medium']:
        return COLORS['yoy_medium']
    else:
        return COLORS['yoy_low']


def apply_default_layout(
    fig: go.Figure,
    title: str = '',
    width: int = 900,
    height: int = 600
) -> go.Figure:
    """Aplica configuración de layout por defecto a una figura de Plotly."""
    fig.update_layout(
        title=title,
        width=width,
        height=height,
        **DEFAULT_LAYOUT
    )
    return fig
