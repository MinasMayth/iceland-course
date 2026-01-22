# Lab 4 — Data Preprocessing (2 hours)

**Notebook:** [notebooks/iceland-ml/lab4_preprocessing_patches.ipynb](../../notebooks/iceland-ml/lab4_preprocessing_patches.ipynb)

## ⏱️ Time Allocation (2 hours)
- **10 min:** Introduction to preprocessing pipeline
- **25 min:** Load and inspect Sentinel-2 imagery
- **30 min:** Normalization techniques and implementation
- **30 min:** Label alignment and creation
- **20 min:** Train/val/test splits and persistence
- **5 min:** Wrap-up and validation

## Goals
### Core (Essential)
- Load and inspect Sentinel-2 GeoTIFFs
- Apply normalization (standardization or percentile clipping)
- Align imagery with CORINE/CLC labels
- Define train/val/test splits (70/15/15)
- Persist normalization parameters for inference

### Optional (Time Permitting)
- Compare normalization methods (min-max, z-score, percentile)
- Advanced masking (clouds, shadows, water)
- Data augmentation strategies
- Class balancing techniques
- Quality assessment and outlier detection

## Outputs
### Required
- Normalized imagery ready for patch extraction
- Split definitions and metadata
- Saved normalization stats for later inference
- Label raster aligned with imagery

### Bonus
- Normalization comparison plots
- Quality assessment report
- Augmentation pipeline configured
- Class distribution analysis

## 📚 Session Structure

### Part 1: Data Loading (35 min)
1. **Introduction to Preprocessing** (10 min)
   - Why preprocessing matters
   - Common pitfalls in satellite imagery
   - Overview of the pipeline
   - **Demo:** Preprocessing workflow diagram

2. **Load Sentinel-2 Data** (25 min)
   - Use rasterio to open GeoTIFFs
   - Inspect metadata (CRS, resolution, bounds)
   - Check band count and data types
   - Handle nodata values
   - **Exercise:** Load all four scenes
   - **Troubleshooting:** Memory management for large files

### Part 2: Normalization (30 min)
3. **Normalization Theory** (10 min)
   - Why normalize?
   - Methods comparison:
     - Min-max scaling
     - Z-score standardization
     - Percentile clipping
   - Which to use for Sentinel-2?

4. **Implementation** (20 min)
   - Calculate statistics (mean, std, percentiles)
   - Apply normalization per band
   - Visualize before/after
   - Save parameters for inference
   - **Exercise:** Compare methods on sample patches

### Part 3: Label Alignment (30 min)
5. **Label Data** (15 min)
   - CORINE Land Cover overview
   - Load label raster
   - Reproject to match imagery CRS
   - Resample to imagery resolution
   - **Demo:** Overlay labels on imagery

6. **Alignment and Validation** (15 min)
   - Ensure spatial alignment
   - Handle label gaps and nodata
   - Class mapping (CORINE codes to simplified classes)
   - **Exercise:** Verify alignment visually

### Part 4: Splits and Persistence (25 min)
7. **Train/Val/Test Splits** (15 min)
   - Spatial vs random splitting
   - Define split strategy (70/15/15)
   - Create split masks
   - Verify class balance per split
   - **Exercise:** Implement stratified split

8. **Save Preprocessing Outputs** (10 min)
   - Save normalization parameters (JSON)
   - Save split definitions
   - Save metadata (dates, bands, CRS)
   - Validate saved files
   - **Exercise:** Load and verify saved data

### Part 5: Wrap-up (10+ min)
9. **Validation and Q&A** (5+ min)
   - Quick sanity checks
   - Preview next lab (patch extraction)
   - Address questions

## 🎯 If You Finish Early
- **Advanced Normalization:**
  - Per-scene vs global normalization
  - Robust scaling (removing outliers)
  - Histogram matching between scenes
  - Compare impact on downstream model

- **Data Quality:**
  - Detect and mask clouds with Sentinel-2 QA bands
  - Shadow detection algorithms
  - Snow/ice masking for Iceland
  - Water body masking with NDWI

- **Augmentation Pipeline:**
  - Rotation, flipping, cropping
  - Color jittering
  - Random noise injection
  - Mixup/CutMix strategies

- **Class Analysis:**
  - Compute class distribution
  - Identify rare classes
  - Plan balancing strategy (oversampling, SMOTE, weighted loss)
  - Visualize class spatial distribution

- **Alternative Approaches:**
  - Explore Albumentations library
  - TorchVision transforms
  - GDAL command-line tools
  - Rasterio windows for memory efficiency

## ✂️ If Running Out of Time
**Priority 1 (Must Complete - 75 min):**
- Load imagery (15 min)
- Apply standardization (20 min)
- Load and align labels (20 min)
- Create splits (15 min)
- Save parameters (5 min)

**Can Skip:**
- Normalization comparison (use standardization only)
- Detailed visualization (quick checks only)
- Advanced masking (simple nodata handling)
- Class balance analysis

**Can Do Asynchronously:**
- Normalization method comparison (homework)
- Cloud masking (optional refinement)
- Augmentation exploration (future labs)

**Minimal Viable Lab (90 min):**
- Load 2 scenes (10 min saved)
- Z-score normalization only (10 min)
- Use provided labels (15 min saved)
- Simple random split (10 min saved)
- Quick validation (5 min)

**Backup Plan:**
- If memory issues: Process one scene at a time
- If label data missing: Generate synthetic labels
- If time critical: Provide pre-normalized data and explain process
