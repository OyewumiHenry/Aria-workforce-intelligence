# ARIA Technical Specification

What is in the deployed app, how the data is shaped, and which formulas drive the outputs.

---

## Runtime

- **Python**: 3.10.15
- **Deployment dependencies**: Streamlit, pandas, numpy, plotly, vaderSentiment, and utility packages
- **Deployment posture**: governed analytics only; no deployment-time ML training
- **Production scope**: governed bundle, executive scoring, dashboard delivery, and auditability

---

## Data Schemas

### Raw Dataset: `final_aria_dataset.csv`

Core fields include:

- `source_id`
- `platform`
- cleaned Glassdoor or YouTube text fields
- `primary_theme`
- `confidence`
- `vader_score`
- `vader_label`

### Executive Dataset: `aria_executive_review_dataset.csv`

Adds the executive reporting layer:

- `executive_theme`
- `executive_theme_confidence`
- `assignment_method`
- `override_reason`
- `final_sentiment`
- `negative_intensity_pct`
- `cleaned_text`
- `rating_overall`

### Override Audit: `aria_executive_overrides.csv`

Tracks each manual translation used for executive reporting.

### Manifest: `aria_dataset_manifest.json`

Stores bundle metadata and SHA-256 hashes for the governed files.

---

## Formulas

### Sentiment Thresholds

- positive: `compound >= 0.05`
- neutral: `-0.05 < compound < 0.05`
- negative: `compound <= -0.05`

### Negative Intensity

```text
negative_intensity_pct = abs(VADER negative magnitude) x 100
```

Used only as a comparative severity cue.

### Workforce Risk Index

```text
Risk Score = Negative Reviews x Negative Rate % x (0.5 + Avg Negative Intensity / 200)
```

This combines volume, rate, and severity into a comparable theme ranking.

### Wilson Interval

Used for theme-level and platform-level negative-rate confidence intervals.

### Evidence Pressure

Observed support signal blended from:

- negative-review share
- negative-rate share
- intensity share
- public-exposure share
- theme-size share

### Business Impact Estimate

```text
Impact Potential = 0.35 Productivity + 0.30 Operations + 0.20 Cost + 0.15 Reputation
Business Impact = 0.50 Impact Potential + 0.50 Evidence Pressure
```

The operating weights are explicit judgment calls, not learned coefficients.

---

## Streamlit Configuration

The deployment config keeps the app in a presentation-safe posture:

- headless mode
- viewer toolbar
- XSRF protection enabled
- reduced log noise
- light theme

---

## Dashboard Output

The deployed app exposes seven views:

1. Executive Brief
2. Decision Agenda
3. Risk Ranking
4. Impact Case
5. Evidence by Platform
6. Method Appendix
7. Evidence Audit

---

## Performance

With 150 governed rows, the deployed app is lightweight:

- file load and validation are near-instant
- summary tables build quickly
- charts render without special optimization

Cold start is primarily Streamlit startup plus file validation, not model training.

---

## Boundaries

- ARIA is not a churn prediction system.
- ARIA does not estimate individual-level risk.
- ARIA does not ship a financial forecast model in production.
- ARIA is strongest as a governed external-signal review tool.
