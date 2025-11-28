# Lesson 2 — Fine‑Tuning with TerraTorch

Focus: fine‑tune a geospatial foundation model using TerraTorch from the CLI and in a notebook, including a simple data loader customization.

## Agenda
- TerraTorch concepts: datasets, modules, configs, checkpoints.
- CLI fine‑tuning run from a provided YAML config.
- Notebook-based fine‑tuning to illustrate customization of the dataloader or a model head.
- Logging/monitoring: metrics, early stopping, saving artifacts.

## Hands-on
1. Config
   - Copy `configs/iceland.yaml` and set dataset paths, classes, and training params.
2. CLI Run
   - From the terminal, run fine‑tuning with the CLI (see config for command).
3. Notebook
   - Open `notebooks/iceland-ml/lesson2_finetune.ipynb` to customize a dataloader or class.
4. Checkpoints
   - Identify the best checkpoint and export it for inference in Lesson 3.
 5. HPC (optional)
    - Use the Slurm template `scripts/submit_finetune.sbatch` for long runs on your cluster (fill in partition/account and env).

## Deliverable
- A fine‑tuned checkpoint and a short note on custom changes (if any).

## Notes
- Keep epochs small for class; encourage students to extend asynchronously.
- If environments are unstable, pin versions and cache downloads.
