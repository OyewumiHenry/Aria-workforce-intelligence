"""
Static configuration for the ARIA deployment app.

This module keeps styling, dataset names, and presentation constants out of
the main Streamlit script so the shipped app is easier to scan and maintain.
"""
from __future__ import annotations

from pathlib import Path
from typing import Dict

import streamlit as st

APP_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = APP_DIR.parent
DATA_DIR = PROJECT_ROOT / "01_Data"

RAW_DATASET_NAME = "final_aria_dataset.csv"
EXECUTIVE_DATASET_NAME = "aria_executive_review_dataset.csv"
OVERRIDE_TABLE_NAME = "aria_executive_overrides.csv"
MANIFEST_NAME = "aria_dataset_manifest.json"

RAW_CANONICAL_DATA_PATH = DATA_DIR / RAW_DATASET_NAME
EXECUTIVE_CANONICAL_DATA_PATH = DATA_DIR / EXECUTIVE_DATASET_NAME
OVERRIDE_CANONICAL_DATA_PATH = DATA_DIR / OVERRIDE_TABLE_NAME
MANIFEST_CANONICAL_PATH = DATA_DIR / MANIFEST_NAME

EXEC_THEMES = [
    "Workload & Burnout",
    "Management & Communication",
    "Compensation & Benefits",
    "Career Growth",
    "Work Culture",
]

PIPELINE_CONFIDENCE_SCORES: Dict[str, float] = {
    "HIGH": 1.0,
    "MEDIUM": 0.67,
    "LOW": 0.33,
    "NONE": 0.0,
}

PRIMARY_THEME_MAP: Dict[str, str] = {
    "T1_Physical_Degradation": "Workload & Burnout",
    "T2_Nepotism_Advancement": "Career Growth",
    "T3_Pay_Benefits": "Compensation & Benefits",
    "T4_Supervisor_Inconsistency": "Management & Communication",
    "T5_Bathroom_Dignity": "Work Culture",
}

THEME_COLORS: Dict[str, str] = {
    "Compensation & Benefits": "#13315c",
    "Workload & Burnout": "#b42318",
    "Management & Communication": "#b7791f",
    "Career Growth": "#157347",
    "Work Culture": "#64748b",
}

SENTIMENT_COLORS: Dict[str, str] = {
    "positive": "#157347",
    "neutral": "#94a3b8",
    "negative": "#b42318",
}

PLATFORM_COLORS: Dict[str, str] = {
    "Glassdoor": "#13315c",
    "YouTube": "#b42318",
}

PLOTLY_CONFIG = {
    "displayModeBar": False,
    "responsive": True,
}

BUSINESS_IMPACT_MODEL: Dict[str, Dict[str, object]] = {
    "Workload & Burnout": {
        "Productivity": 10.0,
        "Operations": 10.0,
        "Cost": 9.2,
        "Reputation": 7.4,
        "Impact Summary": "Immediate hit to throughput, fatigue, safety, and peak-week execution.",
    },
    "Compensation & Benefits": {
        "Productivity": 8.6,
        "Operations": 9.2,
        "Cost": 10.0,
        "Reputation": 7.4,
        "Impact Summary": "Largest pressure point on shift fill, overtime coverage, and staffing cost control.",
    },
    "Management & Communication": {
        "Productivity": 8.4,
        "Operations": 9.6,
        "Cost": 8.8,
        "Reputation": 7.0,
        "Impact Summary": "Creates execution variance through inconsistent standards, manager behavior, and weak escalation control.",
    },
    "Work Culture": {
        "Productivity": 6.8,
        "Operations": 7.2,
        "Cost": 8.0,
        "Reputation": 10.0,
        "Impact Summary": "Lower-volume issue with the highest employee-relations and employer-brand exposure.",
    },
    "Career Growth": {
        "Productivity": 6.0,
        "Operations": 6.6,
        "Cost": 7.0,
        "Reputation": 5.8,
        "Impact Summary": "Medium-term pressure on internal mobility credibility rather than immediate throughput loss.",
    },
}

APP_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;600&display=swap');

:root {
    --ink: #0f172a;
    --muted: #475569;
    --line: #cbd5e1;
    --panel: #ffffff;
    --bg: #f4f7fb;
    --navy: #13315c;
    --red: #b42318;
    --amber: #b7791f;
    --green: #157347;
    --slate: #64748b;
}

html, body, [data-testid="stAppViewContainer"] {
    font-family: 'IBM Plex Sans', sans-serif !important;
}

#MainMenu,
footer,
header,
[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
[data-testid="stSidebarCollapsedControl"],
[data-testid="collapsedControl"],
section[data-testid="stSidebar"],
.stDeployButton {
    display: none !important;
}

.stApp { background: var(--bg); }
.block-container {
    max-width: 1320px;
    padding: 2rem 2.8rem 2.8rem 2.8rem !important;
}

h1, h2, h3 {
    color: var(--ink) !important;
    letter-spacing: -0.02em !important;
}

h1 { font-size: 2.35rem !important; font-weight: 700 !important; }
h2 { font-size: 1.45rem !important; font-weight: 700 !important; }
h3 { font-size: 1.05rem !important; font-weight: 600 !important; }
p, li { color: var(--ink); }

[data-testid="metric-container"] {
    background: var(--panel) !important;
    border: 1px solid var(--line) !important;
    border-top: 4px solid var(--navy) !important;
    border-radius: 12px !important;
    padding: 20px 16px !important;
    box-shadow: 0 10px 24px rgba(15, 23, 42, 0.06) !important;
}

[data-testid="stMetricLabel"] p {
    color: var(--muted) !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
}

[data-testid="stMetricValue"] p {
    color: var(--ink) !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 30px !important;
    font-weight: 700 !important;
}

.hero {
    background: linear-gradient(135deg, #13315c 0%, #1d4e89 62%, #dce7f8 100%);
    border: 1px solid #2f528f;
    border-radius: 16px;
    padding: 26px 28px;
    margin-bottom: 22px;
    box-shadow: 0 16px 32px rgba(19, 49, 92, 0.16);
}

.hero-kicker {
    display: inline-block;
    background: rgba(255, 255, 255, 0.18);
    color: #f8fafc;
    border: 1px solid rgba(255, 255, 255, 0.25);
    border-radius: 999px;
    padding: 4px 10px;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 12px;
}

.hero h1,
.hero p {
    color: #f8fafc !important;
    margin: 0;
}

.hero p {
    font-size: 15px;
    line-height: 1.65;
    max-width: 980px;
    margin-top: 8px;
    color: rgba(248, 250, 252, 0.88) !important;
}

.section-sub {
    color: var(--muted);
    font-size: 14px;
    margin: -10px 0 18px 0;
    line-height: 1.65;
}

.panel {
    background: var(--panel);
    border: 1px solid var(--line);
    border-radius: 14px;
    padding: 18px 20px;
    box-shadow: 0 8px 22px rgba(15, 23, 42, 0.05);
}

.callout {
    background: #eef4ff;
    border: 1px solid #c7d7f4;
    border-left: 6px solid var(--navy);
    border-radius: 12px;
    padding: 18px 20px;
    margin: 12px 0 18px 0;
}

.driver-card {
    background: var(--panel);
    border: 1px solid var(--line);
    border-top: 5px solid var(--navy);
    border-radius: 14px;
    padding: 18px 18px 16px 18px;
    min-height: 180px;
    box-shadow: 0 8px 22px rgba(15, 23, 42, 0.05);
}

.callout,
.callout p,
.callout span,
.callout strong {
    color: var(--ink) !important;
    line-height: 1.65;
}

.driver-rank {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 6px;
}

.driver-theme {
    font-size: 22px;
    font-weight: 700;
    color: var(--ink);
    line-height: 1.2;
    margin-bottom: 8px;
}

.driver-meta {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 12px;
    color: var(--muted);
    line-height: 1.7;
}

.ranking-item {
    background: var(--panel);
    border: 1px solid var(--line);
    border-radius: 12px;
    padding: 14px 16px;
    margin-bottom: 10px;
}

.ranking-item strong {
    color: var(--ink);
    font-size: 15px;
}

.stTabs [data-baseweb="tab-list"] {
    background: transparent !important;
    border-bottom: 2px solid #dbe3ef !important;
    gap: 0 !important;
    padding: 0 !important;
}

.stTabs [data-baseweb="tab"] {
    color: var(--muted) !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    padding: 14px 18px !important;
    border-bottom: 3px solid transparent !important;
    border-radius: 0 !important;
    background: rgba(255, 255, 255, 0.62) !important;
}

.stTabs [aria-selected="true"] {
    color: var(--navy) !important;
    border-bottom: 3px solid var(--navy) !important;
    background: #ffffff !important;
}

[data-testid="stPlotlyChart"],
[data-testid="stDataFrame"] {
    background: var(--panel) !important;
    border: 1px solid var(--line) !important;
    border-radius: 14px !important;
    padding: 10px !important;
    box-shadow: 0 8px 22px rgba(15, 23, 42, 0.05) !important;
}

[data-testid="stDataFrame"] * {
    color: var(--ink) !important;
}

.stDownloadButton button,
.stButton button {
    background: var(--navy) !important;
    color: #f8fafc !important;
    border: 1px solid var(--navy) !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
}

.stDownloadButton button:hover,
.stButton button:hover {
    background: #1d4e89 !important;
    border-color: #1d4e89 !important;
    color: #ffffff !important;
}

.stExpander {
    background: var(--panel) !important;
    border: 1px solid var(--line) !important;
    border-radius: 14px !important;
    box-shadow: 0 8px 22px rgba(15, 23, 42, 0.05) !important;
}

.stExpander details summary p {
    color: var(--ink) !important;
    font-weight: 600 !important;
}

.small-note {
    font-size: 12px;
    color: var(--muted) !important;
    margin-top: 6px;
}

.gov-footer {
    margin-top: 48px;
    padding: 14px 20px;
    border-top: 1px solid var(--line);
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    color: var(--muted);
    text-align: center;
    letter-spacing: 0.03em;
}

@media (max-width: 768px) {
    .block-container {
        padding: 1rem 1rem 1.5rem 1rem !important;
    }
    h1 { font-size: 1.6rem !important; }
    h2 { font-size: 1.15rem !important; }
    [data-testid="stMetricValue"] p {
        font-size: 22px !important;
    }
    .hero { padding: 16px 16px; }
    .driver-card { min-height: 140px; padding: 14px; }
}
</style>
"""


def configure_app() -> None:
    """Apply Streamlit page configuration and the shared ARIA visual theme."""
    st.set_page_config(
        page_title="ARIA | Executive Workforce Risk Review",
        page_icon=":bar_chart:",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    st.markdown(APP_CSS, unsafe_allow_html=True)
