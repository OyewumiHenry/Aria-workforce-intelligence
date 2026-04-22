# ARIA Dashboard Walkthrough

What each tab does and how to present it cleanly.

---

## Before You Start

Open the dashboard locally at `http://localhost:8501` or use the deployed Streamlit link.

On load, ARIA:

- validates the governed bundle against the manifest
- prepares the executive dataset
- builds summary tables and ranking views

If governance fails, the app stops instead of rendering.

---

## Landing Page

The top of the dashboard shows six KPI cards:

- Total Reviews
- Negative Reviews
- Glassdoor Negative
- YouTube Negative
- Pipeline HIGH Confidence
- Top 3 Driver Share

The `Page Summary` expander gives a one-line purpose for each tab.

---

## Tab 1: Executive Brief

It contains:

- top driver cards
- observed findings
- executive judgment
- risk ranking summary
- impact case summary
- strategic recommendations

This tab condenses the full project into one readout.

---

## Tab 2: Decision Agenda

It contains:

- a three-point opening callout
- a 90-second boardroom opening
- download buttons for the brief, method appendix, and CSV exports
- a 30/60/90-day agenda
- KPI requests for leadership
- a challenge-response grid

---

## Tab 3: Risk Ranking

It contains:

- horizontal bar chart of workforce risk score by theme
- risk table with counts, rates, confidence intervals, and severity
- stacked sentiment chart by theme

The score is relative inside this dataset. It is not a prediction.

---

## Tab 4: Impact Case

It contains:

- evidence bullets behind the impact estimate
- top impact cards
- grouped comparison of business impact versus workforce risk
- operating-domain heatmap
- full impact table

This tab is the executive prioritization layer, not a financial model.

---

## Tab 5: Evidence By Platform

It contains:

- platform summary cards
- grouped bar chart of negative rate by theme and platform
- cross-platform readout

The main point is not that one platform is "truer." It is that the two platforms signal risk differently and should be read with sample-size context.

---

## Tab 6: Method Appendix

It contains:

- provenance metrics
- sentiment-model selection notes
- the 18 validation checks
- method facts
- explicit non-claims
- low-sample watchlist
- governance bundle status
- rank stability tables
- formula reference
- manual override audit

---

## Tab 7: Evidence Audit

It contains:

- filters for platform, theme, and sentiment
- row-level review table
- CSV export

This is the traceability layer for the whole dashboard.

---

## Footer

The governance footer shows:

- manifest timestamp
- executive dataset hash
- override table hash
- total review count
- theme count

This keeps the provenance visible during demos.
