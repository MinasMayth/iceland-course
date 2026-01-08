# Lab 5 — Patch Extraction (2 hours)

**Notebook:** [notebooks/iceland-ml/lab4_preprocessing_patches.ipynb](../../notebooks/iceland-ml/lab4_preprocessing_patches.ipynb)

## ⏱️ Time Allocation (2 hours)
- **10 min:** Introduction to patch-based learning
- **30 min:** Patch extraction implementation
- **25 min:** Class balancing strategies
- **25 min:** Data persistence and validation
- **20 min:** Dataset statistics and quality checks
- **10 min:** Advanced techniques (optional) + Q&A

## Goals
### Core (Essential)
- Extract 224×224 patches from normalized imagery
- Balance classes across train/val/test splits
- Write patch metadata and persist arrays efficiently (NumPy/NPZ)
- Validate patch quality and coverage

### Optional (Time Permitting)
- Multi-scale patch extraction
- Overlap strategies for augmentation
- Hard negative mining
- Patch-level quality filtering
- Memory-efficient HDF5 storage

## Outputs
### Required
- Patch datasets for train/val/test (NPZ or NPY format)
- Patch-level metadata (coordinates, class, scene ID)
- Integrity checks and dataset statistics
- Stored patch arrays ready for training

### Bonus
- Multi-resolution patches
- Augmented patch variants
- HDF5 dataset for large-scale training
- Visualization dashboard

## 📚 Session Structure

### Part 1: Patch Extraction Basics (40 min)
1. **Introduction** (10 min)
   - Why patches instead of full scenes?
   - Patch size considerations (224×224 standard for CNNs)
   - Stride and overlap strategies
   - Memory vs compute tradeoffs
   - **Demo:** Patch extraction visualization

2. **Implementation** (30 min)
   - Sliding window approach
   - Extract patches from each scene
   - Match patches with labels
   - Handle edge cases and partial patches
   - **Exercise:** Extract patches from one scene
   - **Troubleshooting:** Memory management

### Part 2: Class Balancing (25 min)
3. **Balancing Strategy** (10 min)
   - Why balance?
   - Class distribution analysis
   - Sampling strategies:
     - Random undersampling
     - Random oversampling
     - Stratified sampling
   - **Demo:** Class distribution before/after

4. **Implementation** (15 min)
   - Calculate class counts
   - Apply balancing per split
   - Verify balanced distribution
   - **Exercise:** Balance your dataset

### Part 3: Data Persistence (25 min)
5. **Storage Formats** (10 min)
   - NumPy (.npy, .npz)
   - HDF5 (.h5) for large datasets
   - Memory-mapped arrays
   - Compression options
   - **Comparison:** Speed vs size tradeoffs

6. **Save and Validate** (15 min)
   - Save train/val/test patches
   - Write metadata JSON
   - Verify file integrity
   - Test loading speed
   - **Exercise:** Save and reload dataset

### Part 4: Quality Checks (30 min)
7. **Dataset Statistics** (15 min)
   - Patch count per class and split
   - Spatial coverage visualization
   - Band statistics per class
   - Outlier detection
   - **Exercise:** Generate dataset report

8. **Visualization** (15 min)
   - Sample patches per class
   - RGB visualization
   - False color composites
   - Label overlay verification
   - **Exercise:** Create visualization grid

### Part 5: Advanced Topics (Optional, 10+ min)
9. **Advanced Techniques** (if time permits)
   - Multi-scale patches (128, 224, 448)
   - Overlapping patches for test-time augmentation
   - Hard negative mining (misclassified patches)
   - Contextual patches (include surrounding area)
   - **Exercise:** Implement one advanced technique

10. **Q&A and Next Steps** (5 min)

## 🎯 If You Finish Early
- **Advanced Extraction:**
  - Multi-scale pyramid (extract at 2-3 resolutions)
  - Adaptive sampling (more patches from rare classes)
  - Spatially-aware splits (avoid train/test leakage)
  - Temporal patches (same location, different dates)

- **Data Augmentation:**
  - On-the-fly augmentation pipeline
  - Rotation (90°, 180°, 270°)
  - Horizontal/vertical flipping
  - Random crops and scaling
  - Color jittering

- **Quality Filtering:**
  - Remove patches with >50% nodata
  - Filter high-cloud-cover patches
  - Detect and remove blurry patches
  - Identify and handle mixed-class patches

- **Storage Optimization:**
  - Convert to HDF5 for faster loading
  - Implement data streaming
  - Test PyTorch DataLoader integration
  - Benchmark different formats

- **Dataset Analysis:**
  - Per-class spectral signatures
  - Class separability analysis (t-SNE, PCA)
  - Spatial autocorrelation
  - Dataset bias detection

## ✂️ If Running Out of Time
**Priority 1 (Must Complete - 75 min):**
- Extract patches (30 min)
- Basic class counting (10 min)
- Save as NPZ (15 min)
- Quick validation (20 min)

**Can Skip:**
- Detailed balancing (do simple random sampling)
- HDF5 exploration (use NPZ only)
- Extensive visualization (show 2-3 examples)
- Advanced statistics

**Can Do Asynchronously:**
- Class balancing refinement
- Storage format comparison
- Detailed quality analysis
- Advanced extraction techniques

**Minimal Viable Lab (90 min):**
- Extract 224×224 patches (25 min)
- Simple random sampling (10 min)
- Save train/val/test NPZ (15 min)
- Load and verify shapes (5 min)
- Show sample patches (5 min)
- (30 min saved by skipping balancing and stats)

**Backup Plan:**
- If extraction is slow: Extract from 1-2 scenes only
- If memory issues: Process in batches, save incrementally
- If time critical: Provide pre-extracted patches, focus on understanding
