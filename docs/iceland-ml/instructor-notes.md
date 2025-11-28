# Instructor Notes

## Roles
- Gabriele: course lead, context, and HPC access (JUDOOR).
- Rocco: technical lead (data, TerraTorch, fine‑tuning, troubleshooting).
- Stefano: consult existing material and slides; align narrative.

## Timeline
- Jan (wk 2): Lesson 1 + environment checks and AOI/data prep.
- Feb: Lesson 2 (fine‑tuning) + async practice.
- Mar: Lesson 3 (inference/benchmark) + project wrap‑up.
- Apr (mid): submissions, optional presentations.

## Cohort & Modality
- 5–20 students; elective → higher engagement.
- In-person preferred; for virtual, shorten lectures, add checkpoints and recorded demos; maintain active Slack/Mattermost for support.

## Environments
- Pin critical libs; provide a `requirements.txt` and a lockfile (e.g., `uv.lock`).
- Test on JupyterLab; for heavy runs, offer HPC/JSC job templates.
- Provide a fallback dataset to bypass downloads when APIs are flaky.

## Assessment
- Milestones: data prepared (L1), FT checkpoint + notes (L2), inference map + comparison (L3).
- Encourage reflection on model limits, class confusion, and AOI bias.

## Benchmarking
- Provide a reference prediction on a fixed AOI with reported metrics.
- Students compare maps and metrics; discuss reasons for gaps.

## Communication
- Set up Slack/Mattermost channels: #announcements, #help, #share-results.
- Office hours after each lesson.
