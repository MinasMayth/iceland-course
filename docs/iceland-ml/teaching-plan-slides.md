---
marp: true
size: 16:9
theme: default
paginate: true
---

# Remote Sensing with Foundation Models
### 3-Lesson Module — University of Iceland

- Leads: Gabriele (course), Rocco (tech)
- Cohort: 5–20 students (elective)
- Modality: In-person or virtual (JupyterLab + Slack/Mattermost)

![w:120](../assets/computer.png) ![w:120](../assets/earth.png)

---

## Why This? (Storyline)

- Start with a location you care about (AOI)
- Acquire Sentinel‑2 observations, align CORINE labels
- Fine‑tune a geospatial FM (TerraTorch)
- Produce and evaluate a classification map
- Compare to a benchmark and reflect on generalization

---

## Learning Outcomes

- Find/access EO data (Sentinel‑2) and CORINE labels programmatically
- Prepare a small dataset fit for training
- Fine‑tune a foundation model (CLI + Notebook) and customize loaders
- Run inference, visualize maps, and compute mIoU/accuracy
- Operate reliably in JupyterLab and optionally HPC (JUDOOR)

---

## Module Overview

1) Data & Environment (Lesson 1)
- AOI selection, 4 S2 acquisitions, CORINE rasterization (Do we need students to obtain their own data?) (Students choosing their own tile has its merits)
- Environment reliability tips and JupyterLab orientation

2) Fine‑Tuning (Lesson 2)
- TerraTorch concepts, CLI run, notebook customization
- Checkpoints, metrics, early stopping

3) Inference & Benchmark (Lesson 3)
- Apply model on new data, evaluate, compare with benchmark

---

## Schedule & Modality

- Timeline: 2nd week of Jan → mid-April
- 3 focused lessons + async labs and office hours
- Virtual adaptation: shorter live blocks, recorded demos, active chat support

---

## Tools & Data

- JupyterLab (local or JSC)
- TerraTorch, PyTorch
- Sentinel‑2 L2A (Copernicus Hub / MPC / AWS)
- CORINE Land Cover (CLMS)
- Slack/Mattermost for Q&A and announcements

---

## Lesson 1 — Data & Environment

- Pick AOI + time window; target ≤20% clouds
- Download 4 S2 acquisitions (`scripts/s2_download.py`)
- Rasterize CORINE to match S2 grid (`scripts/corine_match.py`)
- Validate in notebook (band order, shapes, CRS)
- Deliverable: imagery + aligned label raster

---

## Lesson 2 — Fine‑Tuning with TerraTorch

- Configure data & classes (`configs/iceland.yaml`)
- Run CLI fine‑tune; monitor metrics and checkpoints
- Notebook: customize dataloader/model head (show pattern)
- Optional: Slurm job for long runs (`scripts/submit_finetune.sbatch`)
- Deliverable: best checkpoint + brief notes on customizations

---

## Lesson 3 — Inference & Benchmarking

- Load checkpoint; infer on new S2 acquisition
- Export classification GeoTIFF; visualize with legend
- Compute accuracy/mIoU if labels available
- Compare to provided benchmark (qualitative + quantitative)
- Deliverable: map + short comparison summary

---

## Benchmark Support

- Synthetic set for practice (`scripts/generate_synthetic_benchmark.py`)
- Evaluation notebook (`notebooks/iceland-ml/benchmark_evaluation.ipynb`)
- Real benchmark artifact optional (recommended for a fixed AOI)

---

## Assessment & Feedback

- Milestones:
  - L1: dataset prepared
  - L2: fine‑tuned checkpoint
  - L3: inference map + comparison
- Encourage reflection on limits, class confusion, AOI bias
- Share results in chat; light peer feedback

---

## Risks & Mitigations

- Environment instability → pinned deps, ready notebooks, fallback data
- API/data access issues → provide mirrors/small cached samples
- GPU scarcity → small batches/epochs, Slurm template for off-hours
- Motivation (virtual) → shorter blocks, clear deliverables, benchmarks

---

## Collaboration & Reuse

- Coordinate with Stefano; leverage existing materials
- Iteratively improve for conference workshops/tutorials
- Maintain docs in `docs/iceland-ml/` + runnable scripts/notebooks

---

## Next Steps

- Finalize AOI examples and a real benchmark artifact
- Pre-validate environments (local + JSC/JUDOOR)
- Open Slack/Mattermost and publish schedule/office hours

---

## Links (Repo)

- Overview & lessons: `docs/iceland-ml/`
- Scripts: `scripts/`
- Configs: `configs/`
- Notebooks: `notebooks/iceland-ml/`
