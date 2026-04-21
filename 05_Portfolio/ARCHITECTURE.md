# ARIA Technical Architecture

How the project moves from raw review text to an executive dashboard.

---

## Project Layout

The production-facing part of ARIA is fully represented in this repository: governed data bundle, executive translation layer, dashboard logic, deployment configuration, and documentation. Notebook work supports that core app.

---

## System Layers

```text
Raw sources
  |- Glassdoor reviews
  `- YouTube transcripts

Notebook and governance layer
  |- pipeline cleaning and theme preparation
  |- executive review translation
  |- explicit override audit
  `- manifest generation

Governed data bundle
  |- final_aria_dataset.csv
  |- aria_executive_review_dataset.csv
  |- aria_executive_overrides.csv
  `- aria_dataset_manifest.json

Deployment layer
  |- Streamlit dashboard flow in aria_app.py
  `- shared app chrome and constants in aria_config.py
```

---

## Data Pipeline

### 1. Acquisition And Cleaning

- Glassdoor review fields are combined into a single cleaned text field.
- YouTube transcript evidence is normalized into the same review schema.
- Every row receives a stable `source_id`.

Output: `final_aria_dataset.csv`

### 2. Sentiment Reference

- VADER compound scores are computed for each review.
- Final sentiment remains governed by the prepared dataset logic.
- Negative intensity is retained as a comparative severity reference.

### 3. Executive Theme Translation

Pipeline theme codes are translated into five executive themes:

- Compensation & Benefits
- Workload & Burnout
- Management & Communication
- Career Growth
- Work Culture

Most rows map directly. Unsupported rows are handled only through explicit overrides.

### 4. Override Audit

The override table records:

- `source_id`
- original pipeline theme
- assigned executive theme
- reason for override
- original confidence context

### 5. Governance Bundle

The governed bundle includes the raw pipeline output, executive review dataset, override table, and manifest hashes. The dashboard checks these files at startup before it renders.

---

## Dashboard Startup Sequence

1. Resolve the governed data paths.
2. Load the manifest and CSV files.
3. Verify file hashes against the manifest.
4. Stop immediately on governance mismatch.
5. Prepare the executive dataset.
6. Stop on unresolved theme mappings.
7. Build summaries, rankings, and impact tables.
8. Render the 7-tab dashboard.

---

## Core Application Functions

| Function | Purpose |
|----------|---------|
| `prepare_dataset()` | Normalize fields and finalize executive-theme assignment |
| `build_theme_summary()` | Aggregate review and sentiment metrics by theme |
| `build_platform_summary()` | Compare the five themes across platforms |
| `build_stability_tables()` | Stress-test rankings across six scenario views |
| `build_business_impact_table()` | Blend operating impact assumptions with observed evidence |
| `validate_governance_bundle()` | Enforce manifest integrity before rendering |

The deployment code is split deliberately:

- `aria_app.py` handles data preparation, scoring, and page rendering
- `aria_config.py` holds shared styling, theme constants, dataset paths, and visual configuration

---

## Scoring Logic

### Workforce Risk Index

```text
Risk Score = Negative Reviews x Negative Rate % x (0.5 + Avg Negative Intensity / 200)
```

This is a relative ranking inside the dataset, not a probability model.

### Business Impact Estimate

```text
Impact Potential = 0.35 Productivity + 0.30 Operations + 0.20 Cost + 0.15 Reputation
Evidence Pressure = blended signal from volume, rate, intensity, exposure, and theme scale
Business Impact = 0.50 Impact Potential + 0.50 Evidence Pressure
```

The impact estimate is an executive prioritization tool. It is transparent by design.

---

## Deployment Notes

- Runtime: Python 3.10 in local development, with Streamlit Community Cloud pointed to `deployment/aria_app.py`
- Frontend: Streamlit
- Core libraries: pandas, numpy, plotly, vaderSentiment
- Data location: `01_Data/`

The deployed app no longer depends on deployment-time ML training. Exploratory modeling remains in notebooks only.

---

## Known Constraints

- **150 rows**: enough for structured executive review, not for high-confidence prediction
- **Single employer context**: results should not be generalized without more data
- **Platform imbalance**: YouTube is smaller and harsher, so it is treated as an escalation signal
- **Sentiment ceiling**: VADER is useful here, but still imperfect

The architecture is intentionally simpler now: governed evidence first, executive interpretation second, no synthetic prediction layer in production.
