# ARIA Business Case

What the project is useful for, what it can support, and where the hard limits are.

---

## The Problem

Public employee sentiment is messy, visible, and usually ignored until it becomes a staffing, operations, or reputation issue. ARIA gives leadership a governed way to review that signal before it gets dismissed as noise.

The project reads 150 public reviews from one fulfillment-style employer, organizes them into five themes, and turns them into an executive action agenda.

---

## Project Scope

ARIA covers source preparation, governance, executive theme translation, scoring logic, dashboard delivery, and documentation in one project scope.

---

## What The Data Supports

ARIA is useful for:

- identifying which workforce themes dominate the negative public signal
- showing where operating pressure is most likely to be concentrated
- comparing written review tone versus public video testimony
- checking whether the top conclusions still hold across platform, employee-status, and tenure cuts
- focusing leadership on a smaller set of immediate actions
- deciding which internal HR and operations metrics should be requested next

The current business conclusion is strongest when it is framed this way:

- These are the clearest external workforce-risk signals in the current governed sample.
- These are the themes with enough segment support to justify immediate internal KPI testing.
- These are the operating questions most worth escalating now.

---

## What The Data Does Not Support

ARIA does **not** directly support:

- measured turnover reduction claims
- ROI forecasts
- causal claims about exits, injuries, or absenteeism
- individual-level risk scoring

So the business case is strongest as a prioritization case, not a forecast case.

That means the best current conclusion is not "this proved turnover."
It is "this is the strongest external warning signal and the best place to investigate next."

---

## Why The Business Read Is Stronger Now

The current version is more defensible because it does more than rank themes:

- the top-theme order is stress-tested across six scenario views
- the platform comparison prevents one source from carrying the whole story alone
- segment checks across employee status and tenure reduce reliance on one blended average
- Fisher exact tests pressure-test the strongest subgroup gaps instead of leaving them as descriptive impressions
- each theme is tied to a next-step KPI and a confirmation pattern through the validation matrix

That does not create causality, but it does make the business read harder to dismiss as a one-view opinion.

---

## Decision Value

The value of ARIA is that it shortens the path from unstructured public complaints to leadership action:

- Compensation & Benefits becomes a pay-transparency and scheduling question.
- Workload & Burnout becomes a throughput, fatigue, and safety question.
- Management & Communication becomes a manager-control and escalation question.
- Career Growth becomes an internal-mobility credibility question.
- Work Culture becomes an employee-relations and reputation question.

That framing is operationally useful even before internal data is added.

---

## Current Executive Read

These are the strongest evidence-bounded conclusions in the current version:

- The negative signal is concentrated rather than diffuse, so executive attention does not need to be spread across all five themes equally.
- Compensation & Benefits is the largest negative-volume issue in the sample and should be treated as the first compensation and scheduling review priority.
- Workload & Burnout and Management & Communication are the clearest execution-risk themes because they point to fatigue pressure, frontline inconsistency, and weak escalation control.
- Public video testimony is materially harsher than Glassdoor in this sample, but because YouTube is smaller, it should still be read as escalation pressure rather than equal-weight proof.
- Management & Communication is materially harsher among former employees than current employees in the current sample, which strengthens the case that the issue is tied to exit-stage control friction rather than broad onboarding dissatisfaction.
- Segment checks show that the top themes are not being created by one blended average alone.
- The best current use of ARIA is to direct internal validation, not to close the case on causality.

Those statements are strong enough for executive discussion because they stay inside the evidence boundary.

---

## Current Conclusion Strength

What is already strong:

- concentration of negative signal in a small number of themes
- ranking of current external pressure points
- segment support behind the top themes, so the conclusion is not resting on one blended average alone
- exact within-sample checks behind the strongest subgroup claims
- identification of the first policies and operating levers worth reviewing
- argument for which internal KPIs should be requested next

What still needs validation:

- whether the public signal aligns with measured turnover or exits
- whether burnout signal aligns with absenteeism or safety loss
- whether pay friction is weakening overtime fill or shift coverage
- whether manager inconsistency is visible in promotion or discipline data

So the current business conclusion should be presented as "high-confidence prioritization" rather than "high-confidence proof."

---

## Business Validation Matrix

| Theme | Current external read | Segment support now | Next KPI to test | What would strengthen the conclusion |
|-------|-----------------------|---------------------|------------------|--------------------------------------|
| Compensation & Benefits | Largest negative-volume issue and the first pay and scheduling review priority. | Present across both platforms and still visible across current/former and early/later tenure cuts. | Overtime fill, shift coverage, voluntary exits | High-friction sites also show weaker shift fill or higher exits. |
| Workload & Burnout | Sharpest operational-strain signal and the clearest fatigue-control priority. | Harsher in the smaller but more severe video testimony, with limited-base caution still applied. | Absenteeism, call-offs, safety incidents | Workload-heavy areas also show higher call-offs or incident rates. |
| Management & Communication | Manager-control and escalation risk with advancement credibility concerns. | More pronounced in former-employee segments than in the blended average alone. | Promotion approvals, write-up variance, escalation closure | Manager-level outliers track complaint concentration. |
| Career Growth | Advancement-credibility issue with lower volume than the top three themes. | Concentrated signal, but not broad enough yet to outrank the core operating risks. | Promotion rate, time-to-promotion | Low-mobility units also show stronger advancement complaints. |
| Work Culture | Employee-relations and reputation risk with lower direct operating weight. | Cross-platform signal, but lighter than the top operational themes. | Employee-relations cases, referral rate, retention | Culture-heavy sites also show weaker referrals or retention. |

---

## Next Metrics Leadership Should Request

To turn ARIA from external signal into a stronger business case, leadership should request:

- voluntary exit rate by site, shift, tenure band, and manager
- absenteeism and call-off rates by workload-heavy department
- overtime acceptance and fill rates by site and pay band
- safety incidents by department and peak period
- promotion approvals and write-up rates by manager

These internal cuts are what let the team test whether the public signal aligns with real operating loss.

Once those metrics are added, the business conclusion gets materially stronger because the story becomes:

`external signal -> internal KPI check -> action decision`

---

## Recommendations

### 0-30 Days

- publish pay bands, overtime rules, and schedule predictability guardrails
- remove dignity-based discipline triggers

### 30-60 Days

- install manager-control metrics for write-ups, promotions, and escalation closure

### 60-90 Days

- redesign peak-workload controls and break protections
- publish clearer advancement criteria

---

## Limits

1. The review base is small.
2. The data reflects one employer context.
3. Public sentiment is partial, not complete.
4. Business impact weights are explicit judgment calls.
5. VADER is useful here, but still imperfect.

The business case is simple: ARIA helps leadership decide where to investigate and act first. It should not be presented as proof that a specific intervention will create a specific financial return, but it is strong enough to support a focused review agenda and a sharper KPI request list.
