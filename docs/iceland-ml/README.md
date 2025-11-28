# Iceland ML Module: Remote Sensing with Foundation Models

This 3-lesson module guides students through building a practical EO ML pipeline using Sentinel-2 imagery, CORINE Land Cover labels, and fine-tuning a geospatial foundation model (via TerraTorch). The storyline: start from a real location of interest, acquire data, prepare labels, fine-tune a model, and apply it to produce a classification map, comparing against a benchmark.

- Audience: 5–20 students (elective), mixed in-person/virtual.
- Instructors: Rocco (tech lead), Gabriele (course lead). Consult Stefano for existing materials.
- Schedule: 2nd week of Jan → mid-April (flexible pacing; 3 intensive sessions + async lab time).
- Modality: JupyterLab-based, with optional HPC (JSC/JUDOOR) for heavier runs.
- Comms: Slack or Mattermost workspace for Q&A, announcements, troubleshooting.

## Learning Outcomes
- Find and access EO data programmatically (Sentinel-2) and labels (CORINE/CLC).
- Prepare a small dataset around a chosen AOI and time window.
- Fine-tune a geospatial FM using TerraTorch (CLI + Notebook) and customize a data loader.
- Evaluate and visualize classification results; compare to a benchmark.
- Run jobs and manage environments reliably in Jupyter-based setups.

## Lesson Overview
- Lesson 1: Data & Environment — data sources, API access, AOI selection, 4 S2 acquisitions, CORINE label matching, environment reliability tips.
- Lesson 2: Fine-tuning — TerraTorch intro, CLI workflow, notebook customization (dataloader/class), tracking, and checkpoints.
- Lesson 3: Inference & Use — apply the fine-tuned model to new data, visualize maps, compare to a baseline/benchmark, and discuss limitations.

## Virtual vs In-Person
- In-person: whiteboard walkthrough + live coding segments.
- Virtual: shorter live blocks, more guided notebooks, async Slack support. Record demos to reduce cognitive load.

## Benchmarking Option
- Provide a reference model output on a fixed AOI to compare mIoU/accuracy and qualitative maps.

## Next Steps
- Follow Lesson 1 to set up your AOI and data.
- Use provided scripts in `scripts/` and notebooks in `notebooks/iceland-ml/`.