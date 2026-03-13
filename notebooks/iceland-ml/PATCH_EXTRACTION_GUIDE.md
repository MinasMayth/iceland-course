# Patch Extraction Helper Guide
## Lab 4.2: Complete Reference for Understanding Patch Extraction

---

## Table of Contents
1. [Core Concepts](#core-concepts)
2. [Why Patch Extraction?](#why-patch-extraction)
3. [How Patch Extraction Works](#how-patch-extraction-works)
4. [Normalization Techniques](#normalization-techniques)
5. [Data Structures](#data-structures)
6. [Common Questions](#common-questions)
7. [Technical Details](#technical-details)

---

## Core Concepts

### What is Patch Extraction?
**Patch extraction** is the process of dividing large satellite images into small, fixed-size pieces (patches) that can be used to train machine learning models.

**Analogy:** Think of cutting a large poster into small square tiles, where each tile represents a training example.

### Key Terms
- **Patch**: A small square region extracted from a larger image (e.g., 3×3 pixels)
- **Patch Size**: The dimensions of each patch in pixels (e.g., 3×3 = 30m×30m at 10m resolution)
- **Stride**: The step size between consecutive patch extractions
- **Center-pixel labeling**: Using the label at the center of a patch to represent the entire patch
- **Normalization**: Scaling pixel values to a standard range for ML training

---

## Why Patch Extraction?

### Problem: Satellite Images are Too Large
- Sentinel-2 tiles are 10,980 × 10,980 pixels (~120 million pixels)
- Cannot feed entire images into neural networks (memory constraints)
- Need fixed-size inputs for batch processing

### Solution: Extract Small Patches
- Convert one large image → thousands of small training samples
- Each patch = one training example
- Fixed size enables batch training
- Captures local spatial patterns

### Benefits
1. **Memory Efficient**: Small patches fit in GPU memory
2. **Data Augmentation**: One image → many training samples
3. **Local Context**: Each patch contains relevant spatial information
4. **Balanced Batches**: Can mix patches from different classes

---

## How Patch Extraction Works

### Step-by-Step Process

#### 1. **Input Data**
We start with two aligned images:
- **S2 stacked bands**: 4 spectral bands (B02, B03, B04, B08) - the features
- **CORINE aligned**: Land cover labels (1-44) - the ground truth

Both images have the **same dimensions and alignment** (from Lab 4.1).

#### 2. **Sliding Window Approach**
```
Image (e.g., 10980 × 10980 pixels)
┌─────────────────────────────────┐
│ ╔═══╗                           │  Patch 1 (3×3)
│ ║   ║→ stride →╔═══╗            │  Patch 2 (3×3)
│ ╚═══╝          ║   ║            │
│                ╚═══╝            │
│       ↓ stride                  │
│     ╔═══╗                       │
│     ║   ║                       │  ...continue scanning
│     ╚═══╝                       │
└─────────────────────────────────┘
```

The algorithm:
```python
for y in range(0, height - patch_size + 1, stride):
    for x in range(0, width - patch_size + 1, stride):
        # Extract patch at position (x, y)
        patch = image[y:y+patch_size, x:x+patch_size]
        # Get center pixel label
        center_label = labels[y + patch_size//2, x + patch_size//2]
```

#### 3. **Patch Extraction Details**

**Example with 3×3 patch:**
```
Satellite Bands (S2)          CORINE Labels
┌───┬───┬───┐                 ┌───┬───┬───┐
│ B │ B │ B │                 │ 12│ 12│ 12│
│ G │ G │ G │  +              │ 12│ 23│ 12│  → Label: 23 (forest)
│ R │ R │ R │                 │ 12│ 12│ 23│
└───┴───┴───┘                 └───┴───┴───┘
    ↓                              ↓
Patch: (3, 3, 4)              Center Label: 23
[height, width, bands]
```

**What gets extracted:**
- **Feature patch**: 3×3 pixels × 4 bands = 36 values (the X)
- **Label**: 1 value from center pixel (the y)
- **Shape**: Each patch becomes (H, W, C) = (3, 3, 4)

#### 4. **Quality Filtering**

Patches are **skipped** if:
- Center pixel label is invalid (< 1 or > 44)
- Any pixel has missing data (value = 0)
- Patch extends beyond image boundaries

This ensures only **valid, complete patches** are used for training.

#### 5. **Output Format**

After processing all positions:
```python
patches: array of shape (N, H, W, C)
    N = number of patches
    H = patch height (e.g., 3)
    W = patch width (e.g., 3)
    C = number of bands (4)

labels: array of shape (N,)
    One label per patch (1-44)
```

---

## Normalization Techniques

### Why Normalize?

**Problem:** Raw Sentinel-2 values range from 0 to 4000+ (12-bit data)
- Different bands have different ranges
- Atmospheric conditions create variations
- Large values slow down neural network training

**Solution:** Scale values to a standard range (typically [0, 1])

### Method 1: Min-Max Normalization
```
normalized = (value - min) / (max - min)
```

**How it works:**
- Sets minimum to 0, maximum to 1
- Linear scaling between these bounds

**Example:**
```
Raw value: 2000
Min: 0, Max: 10000
Normalized: (2000 - 0) / (10000 - 0) = 0.2
```

**Pros:**
- Simple and intuitive
- Preserves relative differences
- Fixed range [0, 1]

**Cons:**
- Sensitive to outliers (one bright cloud affects everything)
- Need to know min/max beforehand

**Use when:** You have well-behaved data with known ranges

---

### Method 2: Z-Score (Standardization)
```
normalized = (value - mean) / std_dev
```

**How it works:**
- Centers data around 0
- Scales by standard deviation
- Result has mean=0, std=1

**Example:**
```
Raw value: 2000
Mean: 1500, Std: 500
Normalized: (2000 - 1500) / 500 = 1.0
```

**Pros:**
- Handles different band ranges well
- Not bounded (can go beyond [0, 1])
- Standard for many ML algorithms

**Cons:**
- Sensitive to outliers
- Range not fixed
- Harder to interpret

**Use when:** Feeding into models that expect standardized inputs

---

### Method 3: Percentile Normalization (RECOMMENDED)
```
low_val = percentile(data, 2)    # e.g., 100
high_val = percentile(data, 98)  # e.g., 3000
normalized = (value - low_val) / (high_val - low_val)
clip to [0, 1]
```

**How it works:**
- Finds 2nd and 98th percentile values
- Scales using these as min/max
- Clips extreme values

**Example:**
```
Raw value: 2000
2nd percentile: 100
98th percentile: 3000
Normalized: (2000 - 100) / (3000 - 100) = 0.655
```

**Pros:**
- **Robust to outliers** (ignores extreme 2% at each end)
- Adaptive to each image's characteristics
- Fixed range [0, 1]
- Works well for satellite imagery

**Cons:**
- More computation (needs sorting)
- Different normalization per image (must save parameters)

**Use when:** Working with satellite imagery (BEST CHOICE for this lab)

---

### Normalization Timing

**Important:** We normalize the **entire image first**, then extract patches.

Why not patch-by-patch?
- ✅ Consistent statistics across all patches
- ✅ More efficient computation
- ✅ Better represents global image characteristics
- ❌ Patch-by-patch would create inconsistent training data

---

## Data Structures

### Input Files (from Lab 4.1)

**Stacked S2 Bands:**
```
*_stacked.tif
├─ Band 1: B02 (Blue)
├─ Band 2: B03 (Green)
├─ Band 3: B04 (Red)
└─ Band 4: B08 (NIR)
Shape: (4, height, width)
Dtype: uint16 (0-10000+)
```

**Aligned CORINE:**
```
corine_aligned_*.tif
└─ Band 1: Land cover class (1-44)
Shape: (height, width)
Dtype: uint8
```

### Output Files

**Training Data (.npz):**
```python
patches_*_data.npz
├─ 'patches': array(N, H, W, C), dtype=float32
│   └─ Normalized satellite values [0, 1]
└─ 'labels': array(N,), dtype=uint8
    └─ CORINE class IDs (1-44)
```

**Metadata (.json):**
```json
{
  "s2_file": "tile_name_stacked.tif",
  "corine_file": "corine_aligned_tile_name.tif",
  "patch_size": 3,
  "stride": 3,
  "n_patches": 45678,
  "n_bands": 4,
  "n_classes": 28,
  "label_distribution": {
    "12": 12500,
    "23": 8900,
    ...
  },
  "normalization": {
    "method": "percentile",
    "low_pct": 2,
    "high_pct": 98,
    "low_val": 125.0,
    "high_val": 3421.0
  }
}
```

---

## Common Questions

### Q: Why 3×3 patches? Why so small?
**A:** Several reasons:
1. **Center-pixel labeling works best with small patches** - the center pixel truly represents the patch
2. **Computational efficiency** - fewer parameters, faster training
3. **More training samples** - one 10980×10980 image yields ~13 million 3×3 patches
4. **Mixed pixels are common** - larger patches often contain multiple land cover types

However, you can experiment with larger patches (5×5, 7×7, etc.) - see the trade-offs!

---

### Q: What is stride and when should I change it?
**A:** Stride controls patch overlap:

**stride = patch_size (no overlap):**
```
┌───┬───┬───┐
│ 1 │ 2 │ 3 │  Non-overlapping
└───┴───┴───┘
```
- Fewer patches
- No redundancy
- **DEFAULT - use this**

**stride < patch_size (overlap):**
```
┌───┐
│ 1 ├─┐
└─┬─┘2├─┐
  └─┬─┘3│  Overlapping
    └───┘
```
- More patches (data augmentation)
- Redundant information
- Longer processing time
- **Use when:** You need more training data from limited images

---

### Q: Why center-pixel labeling?
**A:** Alternatives and reasoning:

1. **Center pixel** ✅ (our approach)
   - Fast and simple
   - One clear label per patch
   - Assumes spatial autocorrelation (nearby pixels similar)

2. **Majority voting** (alternative)
   - Count most common label in patch
   - More robust to mixed pixels
   - More computation

3. **All pixels** (alternative)
   - Semantic segmentation approach
   - Requires different model architecture
   - More complex

For **classification tasks** with small patches, center-pixel is standard practice.

---

### Q: How do I handle class imbalance?
**A:** If one class dominates (e.g., 80% agricultural land):

**Detection:**
- Check `label_distribution` in metadata
- Calculate imbalance ratio (most common / least common)
- Visualize with bar charts (provided in notebook)

**Solutions:**
1. **Weighted loss function** (training time)
   ```python
   class_weights = compute_class_weight('balanced', classes, labels)
   ```

2. **Stratified sampling** (before training)
   - Sample equal numbers from each class
   - May discard data

3. **Data augmentation** (for minority classes)
   - Create variations of rare classes

4. **Accept imbalance** (if it reflects reality)
   - Use appropriate metrics (F1-score, not accuracy)

---

### Q: What if patches contain multiple land cover types?
**A:** This is **expected and normal**:

```
Patch with mixed pixels:
┌──────┬──────┬──────┐
│Forest│Forest│ Crop │
├──────┼──────┼──────┤
│Forest│Forest│ Crop │  Label: 23 (forest)
├──────┼──────┼──────┤  Center pixel
│ Crop │ Crop │ Crop │
└──────┴──────┴──────┘
```

- Center pixel determines label
- Model learns from context
- Transitions zones are actually informative
- This is why small patches (3×3) work well

**Alternative:** Use larger patches or semantic segmentation if you need pixel-level purity.

---

### Q: How much data do I need?
**A:** Rule of thumb:
- **Minimum per class:** ~1,000 patches
- **Good amount:** ~10,000 patches per class
- **Excellent:** 50,000+ patches per class

From one Sentinel-2 tile (10980×10980), you can extract:
- 3×3 patches, stride=3: ~13 million patches
- 3×3 patches, stride=1: ~120 million patches (overlapping)

**You likely have enough data!** The challenge is class balance, not total quantity.

---

### Q: Why normalize the entire image before extracting patches?
**A:** Consistency and efficiency:

**Correct approach** (image-level normalization):
```python
# 1. Compute statistics from entire image
low_val = percentile(entire_image, 2)
high_val = percentile(entire_image, 98)

# 2. Normalize entire image
normalized_image = (entire_image - low_val) / (high_val - low_val)

# 3. Extract patches
for each position:
    patch = normalized_image[y:y+h, x:x+w]
```
✅ All patches normalized consistently
✅ Statistics represent global scene
✅ More efficient

**Wrong approach** (patch-level normalization):
```python
for each position:
    patch = image[y:y+h, x:x+w]
    # Normalize each patch independently
    patch = (patch - patch.min()) / (patch.max() - patch.min())
```
❌ Each patch has different normalization
❌ Bright patch becomes same as dim patch
❌ Loses relative intensity information

---

### Q: What coordinate system is used?
**A:** Image coordinates (row, column):
- Origin at top-left corner
- Y increases downward (row index)
- X increases rightward (column index)

```
(0,0) ────────→ X (width)
  │
  │
  ↓
  Y (height)
```

Geographic coordinates (lat/lon) are handled by rasterio but not needed for patch extraction.

---

## Technical Details

### Memory Considerations

**Full tile in memory:**
```
10980 × 10980 pixels × 4 bands × 2 bytes (uint16) = ~966 MB per tile
```

**Extracted patches:**
```
50,000 patches × 3 × 3 × 4 bands × 4 bytes (float32) = ~21.6 MB
```

Patch extraction **reduces memory by 45×** while providing more training samples!

---

### Performance Tips

1. **Read entire image into memory once** (faster than repeated file I/O)
2. **Normalize before extraction** (avoid redundant computation)
3. **Use NumPy views when possible** (avoid copying data)
4. **Batch save with compression** (npz with compression)

---

### Data Flow Summary

```
Input: Aligned GeoTIFFs (Lab 4.1)
           │
           ├─→ S2 stacked bands (4, H, W) - uint16
           └─→ CORINE aligned (H, W) - uint8
           │
           ↓
Step 1: Read into memory
           │
           ↓
Step 2: Normalize S2 bands → (4, H, W) float32 [0,1]
           │
           ↓
Step 3: Sliding window extraction
           ├─→ Extract patches: (h, w, 4)
           ├─→ Extract labels: center pixel
           └─→ Filter invalid patches
           │
           ↓
Step 4: Stack into arrays
           ├─→ patches: (N, h, w, 4)
           └─→ labels: (N,)
           │
           ↓
Step 5: Save to disk
           ├─→ .npz (compressed numpy arrays)
           └─→ .json (metadata)
           │
           ↓
Output: ML-ready training data
```

---

## Quick Reference

### Essential Parameters

| Parameter | Default | Description | When to Change |
|-----------|---------|-------------|----------------|
| `PATCH_SIZE` | 3 | Patch dimensions in pixels | Larger for more context, smaller for speed |
| `STRIDE` | None (=patch_size) | Step between patches | Set < patch_size for data augmentation |
| `MAX_PATCHES` | 50,000 | Limit per tile | Increase if you want more data |
| `NORMALIZATION` | 'percentile' | Normalization method | Rarely - percentile is best |
| `PERCENTILE_LOW` | 2 | Low clip percentile | If images are unusually dark/bright |
| `PERCENTILE_HIGH` | 98 | High clip percentile | If images are unusually dark/bright |

---

### CORINE Class Categories

**Remember the 5 main groups:**
1. **Artificial surfaces (1-11)**: Urban, industrial, infrastructure
2. **Agricultural areas (12-22)**: Croplands, pastures, orchards
3. **Forests & semi-natural (23-34)**: Forests, grasslands, bare areas
4. **Wetlands (35-39)**: Marshes, peat bogs, salt marshes
5. **Water bodies (40-44)**: Rivers, lakes, coastal waters

---

## Troubleshooting

### "No aligned data found"
- ✅ Complete Lab 4.1 first
- ✅ Check `ALIGNED_DATA_DIR` path
- ✅ Verify files exist: `ls $ALIGNED_DATA_DIR`

### "No patches extracted"
- ✅ Check for invalid labels (should be 1-44)
- ✅ Check for missing S2 data (zeros)
- ✅ Try smaller `MAX_PATCHES` or different tile

### "Class imbalance is too high"
- ✅ This is normal for real-world data
- ✅ Use weighted loss during training
- ✅ Consider combining multiple tiles
- ✅ Use appropriate evaluation metrics

### "Patches look too dark/bright"
- ✅ Check normalization parameters
- ✅ Verify percentile values in metadata
- ✅ Try different normalization method

---

## Summary Checklist

Before moving to model training, ensure:
- [ ] Patches extracted successfully
- [ ] Normalization applied (check metadata)
- [ ] No missing data (all patches valid)
- [ ] Class distribution analyzed
- [ ] Output files saved (.npz + .json)
- [ ] Understand patch format: (N, H, W, C)
- [ ] Labels are integers 1-44

**You're ready for Lab 5: Deep Learning! 🚀**

---

*Last updated: March 5, 2026*
*Part of Iceland ML Course - Lab 4.2*
