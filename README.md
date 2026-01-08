<div align="center">
    <img src="docs/assets/computer.png" width="200" height=200>
    <img src="docs/assets/earth.png" width="200" height=200>
    <h1>Large-scale Deep Learning with High-Performance Comptuing for Earth Observation</h1>
</div>

This repository hosts support material for a condensed “Large-Scale Deep Learning with HPC for Earth Observation” track at the University of Iceland. It combines a short HPC primer (Units 0–3) with the Iceland ML module (hands-on labs and lesson notebooks) so everything lives in one place for the Iceland cohort.


## Content

Eight lab modules form the backbone of the Iceland track and mirror the structure described in the Iceland ML docs:

| Week | Lab | Topic | Notebook |
|------|-----|-------|----------|
| 1 | 1 | Judoor & HPC Access | [lab1_judoor_hpc_access.ipynb](notebooks/iceland-ml/lab1_judoor_hpc_access.ipynb) |
| 3 | 2 | Jupyter-JSC & Git | [lab2_jupyter_jsc_git.ipynb](notebooks/iceland-ml/lab2_jupyter_jsc_git.ipynb) |
| 6 | 3 | Sentinel-2 Acquisition (GEE) | [lab3_gee_sentinel2_acquisition.ipynb](notebooks/iceland-ml/lab3_gee_sentinel2_acquisition.ipynb) |
| 8 | 4 | Data Preprocessing | [lab4_preprocessing_patches.ipynb](notebooks/iceland-ml/lab4_preprocessing_patches.ipynb) (preprocessing section) |
| 9 | 5 | Patch Extraction | [lab4_preprocessing_patches.ipynb](notebooks/iceland-ml/lab4_preprocessing_patches.ipynb) (patch extraction section) |
| 11 | 6 | Baseline Model Training | [lab5.1_baseline_training.ipynb](notebooks/iceland-ml/lab5.1_baseline_training.ipynb) |
| 12 | 7 | Model Evaluation | [lab5.2_model_evaluation.ipynb](notebooks/iceland-ml/lab5.2_model_evaluation.ipynb) |
| 13 | 8 | TerraTorch Fine-tuning | [finetune.ipynb](notebooks/finetune.ipynb) |

For detailed agendas and outcomes, see [docs/iceland-ml/README.md](docs/iceland-ml/README.md).

### Ongoing activities

### Work on existing units

Collection of the support material for the course is still at its early stages. The following list of activities is going to be updated as more resources are created.

| Unit | Status        | Contributions                                                          |
|------|--------------|------------------------------------------------------------------------|
| 0    | 🗓️ Planned     | Slides to be compiled and provided. |
| 1    | 🚧 In Progress | Environment configuration scripts from existing projects currently under refinement. |
| 2    | 🗓️ Planned | Content to be discussed with Gabriele. |
| 3    | 🗓️ Planned    | Content to be discussed with Gabriele. |

## Iceland ML Module (New)

This repository now also includes a 3-lesson module tailored for an elective ML course at the University of Iceland that connects practical remote sensing workflows with state-of-the-art geospatial foundation models (via TerraTorch):

- Lesson 1 — Data & Environment: pick an AOI, obtain four Sentinel‑2 acquisitions, and align with CORINE/CLC labels.
- Lesson 2 — Fine‑Tuning: run TerraTorch from CLI and a notebook; optionally customize a dataloader or model head.
- Lesson 3 — Inference & Use: generate a classification map on new data and compare to a benchmark.

Logistics and guidance:
- Cohort: 5–20 students (elective → higher engagement).
- Modality: in-person preferred; virtual supported with shorter blocks and recorded demos.
- Schedule: 2nd week of Jan → mid-April; intensive sessions with async practice.
- Communication: set up Slack or Mattermost for announcements and help.
- Environments: JupyterLab-first; for heavier runs consider JSC/JUDOOR. See `docs/iceland-ml/` for details.

Navigation in docs:
- Overview and lessons under “Iceland ML Module” in the MkDocs sidebar.