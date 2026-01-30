# Lab Coherence & Project Milestones

## Complete Project Workflow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ICELAND ML COURSE: COMPLETE WORKFLOW                      │
└─────────────────────────────────────────────────────────────────────────────┘

LAB 1-2: SETUP (3 hours)
├─ Lab 1: Judoor HPC Access
├─ Lab 2: Jupyter-JSC & Git
└─ Output: Development environment ready

LAB 3.1-3.2: DATA ACQUISITION (5 hours)
├─ Lab 3.2: Google Earth Engine
│  ├─ Authenticate with GEE
│  ├─ Define ROI in Iceland
│  ├─ Query Sentinel-2 L2A imagery
│  └─ Download SAFE archives
│
└─ Lab 3.1: Data Preprocessing
   ├─ Read raster files (GDAL)
   ├─ Reproject CORINE to match S2
   ├─ Extract spectral bands
   ├─ Convert to GeoTIFF
   └─ Output: 
      ├─ trainSet1_cleaned.csv (10K-100K patches)
      ├─ valSet1_cleaned.csv
      └─ Processed GeoTIFF files

LAB 4: LEARNING PHASE (2 hours)
├─ PyTorch Fundamentals
│  ├─ Tensors & Operations
│  ├─ Autograd & Backpropagation
│  └─ Dynamic Computation Graphs
│
├─ Attention Mechanisms
│  ├─ Query, Key, Value
│  ├─ Multi-head Attention
│  └─ Scaled Dot-Product
│
└─ Transformer Architecture
   ├─ Encoder-Decoder Stacks
   ├─ Position Encoding
   └─ Feed-forward Networks

LAB 4.1: CUSTOM MODEL TRAINING (6-8 hours)
├─ Load preprocessing data from Lab 3.1
├─ Build transformer (5 layers, 10 heads, 254 hidden)
├─ Train on Sentinel-2 patches
├─ Achieve 75-80% validation accuracy
└─ Output: 
   ├─ best_model.ckpt (50 MB)
   ├─ Training logs & metrics
   └─ checkpoint/

LAB 5: DISTRIBUTED TRAINING (2 hours)
├─ Enable multi-GPU training (DDP)
├─ Scale from 1 GPU → 4-8 GPUs
├─ Achieve 3-6x speedup
└─ Output:
   └─ Optimized model weights

LAB 6: VALIDATION & METRICS (2 hours)
├─ Load trained model
├─ Run inference on validation set
├─ Calculate:
│  ├─ Confusion Matrix
│  ├─ Overall Accuracy (OA)
│  ├─ Producer's Accuracy (PA) per class
│  ├─ User's Accuracy (UA) per class
│  └─ Errors of Omission/Commission
│
├─ Compare with:
│  ├─ WorldCover 2021 (77% OA)
│  └─ Esri Land Cover (82% OA)
│
└─ Output:
   ├─ Validation report
   ├─ Confusion matrix visualization
   ├─ predictions.npy
   └─ metrics.txt

LAB 7: FOUNDATION MODELS (2-3 hours)
├─ Load TerraToRCH backbone (pre-trained on 1M+ S2 images)
├─ Two training strategies:
│  ├─ Strategy A: Frozen Backbone (30 min, 84-87% OA)
│  └─ Strategy B: Fine-tuning (2h, 87-92% OA)
│
├─ Compare with custom model
├─ Deploy for large-scale inference
└─ Output:
   ├─ terratorch_model.pth
   ├─ Production-ready classifier
   └─ Full tile predictions (GeoTIFF)

TOTAL: ~25 hours of hands-on work
```

---

## Data Flow Through Labs

```
GOOGLE EARTH ENGINE (Lab 3.2)
         │
         ├─ Sentinel-2 L2A SAFE archives (.zip)
         │  ├─ 11 spectral bands (B01-B12)
         │  ├─ Cloud mask (SCL)
         │  └─ Metadata (geometry, CRS, etc.)
         │
         ▼
GDAL PREPROCESSING (Lab 3.1)
         │
         ├─ Read raster data
         ├─ Reproject CORINE
         ├─ Extract spectral bands [B02, B03, B04, B05, B06, B07, B08, B8A, B11, B12]
         │
         ▼
CSV TRAINING DATA
         │
         ├─ trainSet1_cleaned.csv (10K patches)
         │  Format: [label, band1, band2, ..., band10]
         │  Values: label ∈ [0-11], bands ∈ [0-1]
         │
         └─ valSet1_cleaned.csv
         │
         ▼
LAB 4.1: CUSTOM TRANSFORMER
         │
         ├─ Load CSV data
         ├─ Create PyTorch datasets
         ├─ Build 5-layer transformer
         ├─ Train for 150 epochs
         │
         ▼
TRAINED CHECKPOINT
         │
         ├─ best_model.ckpt (Lab 4.1 output)
         │
         ├─ Split path A: Continue Lab 5
         │  ├─ Fine-tune with DDP
         │  └─ Multi-GPU optimization
         │
         ├─ Split path B: Lab 6
         │  ├─ Run inference
         │  ├─ Calculate metrics
         │  └─ Compare with products
         │
         └─ Split path C: Lab 7 (Recommended)
            ├─ Load TerraToRCH backbone
            ├─ Add classification head
            ├─ Fine-tune on your data (2 hours)
            └─ Achieve 85-92% OA

PRODUCTION MODEL (Lab 7)
         │
         ├─ terratorch_model.pth (50 MB)
         │
         ├─ Deploy to inference server
         ├─ Process entire tiles
         └─ Create land cover maps
```

---

## Accuracy Progression Through Labs

```
Accuracy over labs:
───────────────────────────────────────────

Random Guessing:     8% (1/12 classes)
                     
Lab 3.1 Quality →    Data readiness check
                     
Lab 4.1 Custom →     75-80% OA ▓▓▓▓░░░░░░░
                     (6h training, 1 GPU)
                     
Lab 5 DDP →          75-80% OA (same, 2h, 4 GPUs)
                     ▓▓▓▓░░░░░░░
                     
Lab 6 Metrics →      Same model, detailed analysis
                     Confusion matrix, per-class PA/UA
                     
Lab 7 Foundation →   87-92% OA ▓▓▓▓▓▓▓░░░░
                     (TerraToRCH fine-tuned)
                     
Lab 7 Frozen →       84-87% OA ▓▓▓▓▓░░░░░░
                     (TerraToRCH, no fine-tune, 30 min)

WorldCover 2021:     77% OA (benchmark)
───────────────────────────────────────────
```

---

## Time Investment vs Benefit

```
Lab          Hours    Difficulty    New Skills              Output
────────────────────────────────────────────────────────────────────
1-2          3        Easy           HPC basics             Environment
3.1-3.2      5        Moderate       GDAL, GEE, geospatial Training data
4            2        Challenging    DL theory              Knowledge
4.1          8        Hard           PyTorch, transformers  Model (75% OA)
5            2        Moderate       DDP, distributed DL    Same model, fast
6            2        Easy           Metrics, validation    Analysis report
7            3        Moderate       Transfer learning      Model (90% OA)
────────────────────────────────────────────────────────────────────
TOTAL       25

Best ROI (return on investment):
- Lab 3.1 → output: usable training data ✓
- Lab 7 → accuracy jump: 75% → 90% with same data ✓
```

---

## Key Milestones & Dependencies

```
CRITICAL PATH (must do in order):
Lab 1 → Lab 2 → Lab 3.1 → Lab 4.1 → Lab 7

PARALLEL PATHS (can do independently):
Lab 4 (learning) can be done while Lab 3.1 is processing

OPTIONAL ENHANCEMENT:
Lab 5 (distributed training) for faster iteration
Lab 6 (detailed metrics) for thorough validation

RECOMMENDED SEQUENCE:
1. Labs 1-2 (setup)
2. Labs 3.1-3.2 (get data)
3. Lab 4 (understand theory)
4. Lab 4.1 (train custom model, 6-8 hours)
5. Lab 6 (validate, understand failures)
6. Lab 7 (apply foundation models for better accuracy)
```

---

## Cross-Lab References

### Lab 3.1 Outputs Used In:
- **Lab 4.1**: trainSet1_cleaned.csv, valSet1_cleaned.csv
- **Lab 5**: Same CSV files with DDP
- **Lab 6**: Same trained model from Lab 4.1
- **Lab 7**: Same CSV files for TerraToRCH fine-tuning

### Lab 4 Concepts Used In:
- **Lab 4.1**: Transformer architecture implementation
- **Lab 5**: Same model, distributed across GPUs
- **Lab 7**: Understanding attention in foundation models

### Lab 4.1 Outputs Used In:
- **Lab 5**: Load checkpoint, fine-tune with DDP
- **Lab 6**: Load best_model.ckpt, run inference
- **Lab 7**: Compare accuracy with TerraToRCH

### Lab 5 Outputs Used In:
- **Lab 6**: Use optimized weights for validation
- **Lab 7**: Baseline for comparison

### Lab 6 Outputs Used In:
- **Lab 7**: Metrics comparison table

---

## Hardware Requirements by Lab

```
Lab         CPU      GPU      RAM      Storage    Duration
──────────────────────────────────────────────────────────
1-2         2 cores  -        4 GB     10 GB      30 min
3.1-3.2     4 cores  -        8 GB     500 GB     5 hours
4           2 cores  -        4 GB     1 GB       2 hours
4.1         8 cores  1x V100  16 GB    100 GB     6-8 hours
5           32 cores 8x V100  32 GB    100 GB     2 hours
6           4 cores  1x GPU   8 GB     50 GB      2 hours
7           8 cores  1x V100  16 GB    100 GB     3 hours

Total storage needed: ~500 GB (mostly for Sentinel-2 raw data)
```

---

## Common Mistakes & How to Avoid Them

### Lab 3.1 Mistakes
```
❌ WRONG: Using raw Sentinel-2 DN values
✅ RIGHT: Normalize to [0, 1] by dividing by 10000

❌ WRONG: Not checking CRS compatibility
✅ RIGHT: Verify with GetProjection() before operations

❌ WRONG: Mixing different resolution bands (10m vs 20m)
✅ RIGHT: Resample all to common resolution first
```

### Lab 4.1 Mistakes
```
❌ WRONG: Learning rate too high (1e-1)
✅ RIGHT: Start with 1e-3 or 1e-4

❌ WRONG: Training on entire tile at once
✅ RIGHT: Extract patches for manageable batch sizes

❌ WRONG: No validation during training
✅ RIGHT: Use val_loader to prevent overfitting
```

### Lab 6 Mistakes
```
❌ WRONG: Summing PA/UA without weighting
✅ RIGHT: Weight by class frequency (macro vs weighted average)

❌ WRONG: Using pixel-level accuracy for patch-level task
✅ RIGHT: Evaluate on patch labels (what you trained on)
```

### Lab 7 Mistakes
```
❌ WRONG: Trying to train entire TerraToRCH on small data
✅ RIGHT: Freeze backbone, train head only (or low LR fine-tune)

❌ WRONG: Using different input format than pre-trained expects
✅ RIGHT: Match original input dimensions (11 bands, normalized)
```

---

## Success Criteria by Lab

### Lab 3.1 Success
- [ ] CSV files have 10,000+ samples
- [ ] Label distribution is reasonable (not all one class)
- [ ] Band values are in [0, 1] range
- [ ] No NaN or infinite values

### Lab 4.1 Success
- [ ] Training loss decreases over epochs
- [ ] Validation accuracy > 50% (better than random)
- [ ] No GPU out-of-memory errors
- [ ] Checkpoint file created

### Lab 6 Success
- [ ] Overall Accuracy > 70%
- [ ] Confusion matrix shows some clear predictions
- [ ] Comparison with other products is meaningful

### Lab 7 Success
- [ ] TerraToRCH achieves > 80% OA
- [ ] Comparison shows improvement over custom model
- [ ] Model can be exported and deployed

---

## Project Timeline Example (4 weeks)

```
WEEK 1: Setup & Learning
├─ Monday: Labs 1-2 (environment)
├─ Wednesday: Lab 4 (theory)
└─ Friday: Review documentation

WEEK 2: Data Acquisition
├─ Monday: Start Lab 3.2 (GEE queries)
├─ Wednesday: Continue Lab 3.1 (preprocessing)
├─ Overnight: Let jobs run on HPC
└─ Friday: Verify CSV files created

WEEK 3: Model Training
├─ Monday: Start Lab 4.1 (submit SLURM job)
├─ Overnight: Let training run (6-8 hours)
├─ Wednesday: Lab 4.1 complete, start Lab 5
├─ Overnight: DDP training (2 hours)
└─ Friday: Jobs complete

WEEK 4: Evaluation & Production
├─ Monday: Lab 6 (validation, metrics)
├─ Wednesday: Lab 7 (TerraToRCH training)
├─ Overnight: Foundation model training (2-3 hours)
├─ Thursday: Complete Lab 7
└─ Friday: Write final report, celebrate! 🎉
```

---

## Path Recommendations

### For Quick Results (11 hours)
```
1. Skip theory, download preprocessed data
2. Lab 4.1: Train custom transformer (6h)
3. Lab 7: Train TerraToRCH (3h)
4. Lab 6: Quick validation (2h)
→ Final accuracy: 85-90% OA
```

### For Deep Learning (25 hours)
```
1. Labs 1-2: Setup (3h)
2. Labs 3.1-3.2: Data (5h)
3. Lab 4: Theory (2h)
4. Lab 4.1: Custom model (6h)
5. Lab 5: Distributed training (2h)
6. Lab 6: Detailed validation (2h)
7. Lab 7: Foundation models (3h)
→ Final accuracy: 88-92% OA + Deep understanding
```

### For Production Deployment (12 hours)
```
1. Skip theory
2. Lab 3.1: Ensure good data (3h)
3. Lab 7: TerraToRCH directly (3h)
4. Lab 6: Validation (2h)
5. Export model for deployment (2h)
6. Integration with geospatial stack (2h)
→ Production-ready classifier
```

---

**Next Step**: Pick your learning path and start with the prerequisites!
