#!/usr/bin/env python3
"""
Generate a tiny synthetic benchmark dataset for Lesson 3 evaluation.
Writes two small GeoTIFFs under data/benchmark/: labels and a mock prediction.
This lets students run the evaluation notebook even without real data.
"""
import os
import numpy as np
import rasterio as rio
from rasterio.transform import from_origin

OUT_DIR = os.environ.get("BENCH_DIR", "data/benchmark")
W = int(os.environ.get("BENCH_W", 128))
H = int(os.environ.get("BENCH_H", 128))
NUM_CLASSES = int(os.environ.get("BENCH_CLASSES", 4))

os.makedirs(OUT_DIR, exist_ok=True)

# Simple synthetic label field: regions with different class ids
yy, xx = np.mgrid[0:H, 0:W]
labels = ((xx // (W // NUM_CLASSES)) % NUM_CLASSES).astype(np.uint8)

# Synthetic prediction: noisy version of labels
rng = np.random.default_rng(42)
noise_mask = rng.random((H, W)) < 0.15
pred = labels.copy()
pred[noise_mask] = rng.integers(0, NUM_CLASSES, size=noise_mask.sum(), dtype=np.uint8)

# Write GeoTIFFs with a simple geotransform (not tied to real-world AOI)
transform = from_origin(0.0, 0.0, 10.0, 10.0)
crs = "EPSG:3857"

profile = {
    "driver": "GTiff",
    "height": H,
    "width": W,
    "count": 1,
    "dtype": "uint8",
    "crs": crs,
    "transform": transform,
}

labels_path = os.path.join(OUT_DIR, "labels.tif")
preds_path = os.path.join(OUT_DIR, "preds_mock.tif")

with rio.open(labels_path, "w", **profile) as dst:
    dst.write(labels, 1)
with rio.open(preds_path, "w", **profile) as dst:
    dst.write(pred, 1)

print(f"Wrote labels: {labels_path}")
print(f"Wrote preds:  {preds_path}")
