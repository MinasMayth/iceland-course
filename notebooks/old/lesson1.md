# Lesson 1 — Data & Environment

Focus: set up the environment, choose an Area of Interest (AOI), obtain four Sentinel‑2 acquisitions, and align them with CORINE Land Cover (CLC) labels.

## Why this matters
We mimic a real project: pick a location you care about, collect observations, and use reliable land cover labels to train a model. This gives context and motivation.

## Agenda
- JupyterLab orientation, kernels, and environment reliability tips.
- AOI selection (city/region/park) and time range.
- Obtain 4 cloud‑filtered Sentinel‑2 L2A acquisitions.
- Retrieve and rasterize CLC labels over the AOI.
- Prepare a small dataset split for fine‑tuning.

## Hands-on
1. Environment
   - Create/activate a conda or venv, then install requirements (see repo `requirements.txt`).
   - If using HPC/JSC, review submission basics and storage paths.
2. AOI & Data
   - Use `scripts/s2_download.py` to search and download 4 S2 scenes for your AOI.
   - Use `scripts/corine_match.py` to fetch/rasterize CLC onto your imagery grid.
3. Validate
   - Open `notebooks/preprocessing.ipynb` (or your own) to verify band order, shapes, CRS, and label coverage.

## Deliverable
- A local folder with 4 S2 acquisitions and a corresponding label raster in the same grid/CRS.

## Tips
- Favor ≤20% cloud cover; prefer same season to reduce variability.
- Keep AOI small (tens of km²) to speed up processing.

## References
- Sentinel-2: Copernicus Open Access Hub, Microsoft Planetary Computer, AWS Open Data.
- CORINE/CLC: Copernicus Land Monitoring Service (CLMS).
