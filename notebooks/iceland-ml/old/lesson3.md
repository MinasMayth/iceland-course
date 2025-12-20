# Lesson 3 — Inference, Visualization, and Benchmarking

Focus: use the fine‑tuned model to produce a classification map for a new scene or AOI; visualize results; compare against a benchmark.

## Agenda
- Load checkpoint and run inference on a new Sentinel‑2 acquisition.
- Post‑processing: argmax, color mapping, smoothing (optional).
- Evaluation: compute mIoU/accuracy vs. CLC (or a held‑out label set).
- Benchmarking: compare to a reference model’s predictions.
- Discussion: what worked, what didn’t, and next steps.

## Hands-on
1. Inference
   - Open `notebooks/iceland-ml/lesson3_inference.ipynb` and load your checkpoint.
   - Run inference on a new scene; export a GeoTIFF of the predicted map.
2. Visualization
   - Display the classification map with a legend; overlay boundaries or basemaps.
3. Metrics
   - If labels are available, compute IoU/accuracy; else perform qualitative analysis.
4. Compare
   - Load the provided benchmark map and compare quantitatively and qualitatively.
 5. Evaluate (Notebook)
    - Open `notebooks/iceland-ml/benchmark_evaluation.ipynb` to compute accuracy/mIoU and visualize side-by-side.
    - If you don't have data yet, run `python scripts/generate_synthetic_benchmark.py` and use the outputs in `data/benchmark/`.

## Deliverable
- A classification map (GeoTIFF/PNG) and a brief comparison to the benchmark.

## Notes
- Encourage students to try different AOIs and document generalization.
