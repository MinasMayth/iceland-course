# Iceland ML Course: Sentinel-2 Land Cover Classification Project Guide

## Complete Project Overview

This guide connects all labs into a coherent project workflow for classifying land cover using Sentinel-2 satellite imagery and deep learning.

---

## Project Objectives

By completing this course, you will:

✅ **Acquire** Sentinel-2 satellite imagery from Google Earth Engine  
✅ **Preprocess** data with geospatial tools (GDAL)  
✅ **Extract labels** from CORINE land cover maps  
✅ **Build** a custom transformer model from scratch  
✅ **Scale** training across multiple GPUs and nodes  
✅ **Validate** model accuracy with confusion matrices  
✅ **Deploy** foundation models (TerraToRCH) for production  

---

## Project Architecture

```
DATA ACQUISITION
├─ Lab 3.2: Google Earth Engine
│  └─ Query Sentinel-2 Level 2A imagery
│     Input: Region of interest (ROI) in Iceland
│     Output: Sentinel-2 SAFE archives (.zip)
│
DATA PREPROCESSING
├─ Lab 3.1: GDAL Processing
│  ├─ Read and inspect raster files
│  ├─ Reproject CORINE to match Sentinel-2 CRS
│  ├─ Extract spectral bands (B02, B03, B04, B08)
│  └─ Generate training patches (10K-100K samples)
│     Output: CSV files (features + labels)
│
MODEL DEVELOPMENT
├─ Lab 4: Learn Deep Learning Fundamentals
│  ├─ PyTorch tensors and autograd
│  ├─ Self-attention mechanisms
│  └─ Transformer architecture
│
├─ Lab 4.1: Train Custom Transformer
│  ├─ Load preprocessed Sentinel-2 data
│  ├─ Build multi-layer transformer
│  ├─ Train on single/multiple GPUs
│  └─ Save model checkpoints
│     Output: Best validation model
│
├─ Lab 5: Distributed Deep Learning
│  ├─ Set up PyTorch DDP
│  ├─ Train across 8+ GPUs
│  ├─ Reduce training time 6x
│  └─ Fine-tune hyperparameters
│     Output: Optimized model weights
│
VALIDATION & EVALUATION
├─ Lab 6: Performance Metrics
│  ├─ Calculate confusion matrices
│  ├─ Compute OA, PA, UA per class
│  ├─ Compare with WorldCover/Esri
│  └─ Visualize results
│     Output: Validation report
│
FOUNDATION MODELS (PRODUCTION)
└─ Lab 7: TerraToRCH Fine-tuning
   ├─ Load pre-trained backbone
   ├─ Fine-tune classification head
   ├─ Achieve 85-92% accuracy
   ├─ Deploy for large-scale inference
   └─ Create prediction maps
      Output: Production-ready model
```

---

## Lab-by-Lab Breakdown

### Lab 1: HPC Access (Judoor)
**Duration**: 30 minutes  
**Prerequisites**: None  
**Deliverable**: HPC account access

- Login to Judoor cluster
- Submit first SLURM job
- Understand job scheduling
- Verify computational resources

### Lab 2: Jupyter-JSC & Git
**Duration**: 2 hours  
**Prerequisites**: Lab 1  
**Deliverable**: Git repository cloned, Python environment configured

- Launch Jupyter-JSC on JURECA
- Learn Git basics and clone course repo
- Create Python virtual environment
- Register custom Jupyter kernel
- Run first analysis notebook

### Lab 3.1: Data Preprocessing
**Duration**: 3 hours  
**Prerequisites**: Lab 2  
**Deliverable**: Processed GeoTIFF files + CSV training sets

**What you'll do:**
```python
# Open raster files
from osgeo import gdal
s2 = gdal.Open("sentinel2_tile.tif")
data = s2.ReadAsArray()

# Reproject CORINE to match S2
gdal.Warp("corine_reprojected.tif", "corine_original.tif", 
         dstSRS=s2.GetProjection())

# Extract tiles and convert to GeoTIFF
gdal.Warp("corine_extracted.tif", "corine_reprojected.tif",
         projwin=[ulx, uly, lrx, lry])
```

**Output format:**
```
trainSet1_cleaned.csv:
label,B02,B03,B04,B05,B06,B07,B08,B11,B12,SCL
5,234,456,789,100,200,300,400,500,600,0
3,245,467,790,101,201,301,401,501,601,0
...
```

### Lab 3.2: Google Earth Engine (In Lab 3.1 attachment)
**Duration**: 2 hours  
**Prerequisites**: Lab 2, GEE account  
**Deliverable**: Sentinel-2 SAFE archives downloaded

- Authenticate with GEE
- Define AOI in Iceland
- Query Sentinel-2 L2A imagery
- Download SAFE archives to HPC storage
- Extract cloud-free scenes

### Lab 4: Understanding Deep Learning
**Duration**: 2 hours  
**Prerequisites**: Lab 2  
**Deliverable**: Conceptual understanding

- PyTorch fundamentals
  - Tensors
  - Autograd and backpropagation
  - Dynamic computation graphs

- Attention mechanisms
  - Query, Key, Value mechanism
  - Multi-head attention
  - Scaled dot-product attention

- Transformer architecture
  - Encoder-decoder stacks
  - Position encoding
  - Feed-forward networks

### Lab 4.1: Train Custom Transformer
**Duration**: 6-8 hours (depends on HW)  
**Prerequisites**: Lab 4, Lab 3.1  
**Deliverable**: Trained model checkpoint, training logs

**Model architecture:**
```
Input: Sentinel-2 patch (10 bands)
  ↓
Transformer (5 layers, 10 attention heads, 254 hidden dim)
  ↓
Classification head (12 classes)
  ↓
Output: Land cover prediction
```

**Key code:**
```python
model = TransformerModel()
trainer = pl.Trainer(accelerator="gpu", devices=4, max_epochs=150)
trainer.fit(model, train_loader, val_loader)
```

**Expected results:**
- OA: 75-80%
- Training time: 6 hours on 1 GPU
- Checkpoint size: ~50 MB

### Lab 5: Distributed Training
**Duration**: 2 hours  
**Prerequisites**: Lab 4.1  
**Deliverable**: Multi-GPU trained model

**Scaling improvements:**
```
1 GPU:  6 hours
2 GPU:  3.5 hours (1.7x speedup)
4 GPU:  2 hours (3x speedup)
8 GPU:  1 hour (6x speedup)
```

**Only code change:**
```python
trainer = pl.Trainer(
    accelerator="gpu",
    devices=8,         # Changed from 1
    strategy="ddp",    # Enable DDP
    num_nodes=2,       # Multi-node
    max_epochs=150
)
```

**Slurm script:**
```bash
#SBATCH --nodes=2
#SBATCH --gpus-per-node=4
#SBATCH --ntasks-per-node=4
srun python train_transformer.py
```

### Lab 6: Validation & Metrics
**Duration**: 2 hours  
**Prerequisites**: Lab 5  
**Deliverable**: Validation report, confusion matrix

**Accuracy metrics calculated:**

```python
from sklearn.metrics import confusion_matrix, classification_report

# Overall Accuracy
OA = (sum of diagonal) / (total samples)

# Per-class metrics
PA = True Positives / Ground Truth Total  (Producer's Accuracy)
UA = True Positives / Predicted Total    (User's Accuracy)

# Error rates
Omission Error = 1 - PA
Commission Error = 1 - UA
```

**Comparison with other products:**
- WorldCover 2021: 77% OA
- Esri Land Cover: 82% OA  
- Your custom model: 75-80% OA

### Lab 7: Foundation Models & TerraToRCH
**Duration**: 2-3 hours  
**Prerequisites**: Lab 6  
**Deliverable**: Production-ready model, comparison report

**Two strategies:**

1. **Frozen Backbone (Fast)**
   ```python
   model = TerraToRCHClassifier(backbone, freeze_backbone=True)
   trainer.fit(model, train_loader, val_loader)
   # Time: 30 min, Memory: 4 GB, Accuracy: 84-87%
   ```

2. **Fine-tuning (Best)**
   ```python
   model = TerraToRCHClassifier(backbone, freeze_backbone=False)
   trainer.fit(model, train_loader, val_loader)
   # Time: 2 hours, Memory: 8 GB, Accuracy: 87-92%
   ```

**Performance comparison:**
| Model | OA | Time | Memory | Data Need |
|-------|-------|------|--------|-----------|
| Custom (Lab 4.1) | 75-80% | 6h | 8GB | 10K samples |
| TerraToRCH (Frozen) | 84-87% | 30m | 4GB | 1K samples |
| TerraToRCH (Fine-tune) | 87-92% | 2h | 8GB | 1K samples |

---

## Essential Data Flow

### Input Data Format (Lab 3.1 Output)

**trainSet1_cleaned.csv:**
```
label,band1,band2,...,band10
5,0.123,0.456,...,0.789
3,0.234,0.567,...,0.890
...
```

- **Column 1**: CORINE label (0-11 for 12 classes)
- **Columns 2-11**: Normalized spectral values (0-1 range)
- **Size**: 10,000-100,000 rows (patches)

### File Structure on HPC

```
/p/project/training2328/
├── lab3_1/
│   ├── code/
│   │   ├── extract_s2.py           # Sentinel-2 extraction
│   │   ├── submit_extract_s2.sh    # SLURM script
│   │   └── ...
│   └── data/
│       ├── trainSet1_cleaned.csv    # Training data
│       └── valSet1_cleaned.csv      # Validation data
│
├── lab4_1/
│   ├── data/                        # Links to lab3_1/data
│   └── checkpoints/
│       ├── best_model.ckpt          # Best validation model
│       └── last.ckpt
│
├── lab5/                            # DDP training outputs
│   └── checkpoints/
│       └── ddp_model.ckpt
│
├── lab6/                            # Validation results
│   ├── confusion_matrix.npy
│   ├── predictions.npy
│   └── metrics.txt
│
└── lab7/
    ├── terratorch_model.pth         # Production model
    └── predictions_terratorch.tif   # Output predictions
```

---

## Timeline & Workload

### Recommended Schedule

| Week | Lab | Hours | Focus |
|------|-----|-------|-------|
| 1 | 1-2 | 3 | Setup and basics |
| 2 | 3.1-3.2 | 5 | Data acquisition & preprocessing |
| 3 | 4 | 2 | Learning (read, understand) |
| 4 | 4.1 | 8 | Training on single GPU |
| 5 | 5 | 2 | Multi-GPU scaling |
| 6 | 6 | 2 | Validation & analysis |
| 7 | 7 | 3 | Foundation models |

**Total**: ~25 hours of hands-on work

### Quick Start (Express Path)

If you have preprocessed data:

1. Lab 4 (2h): Learn transformers
2. Lab 4.1 (6h): Train custom model
3. Lab 7 (2h): Train TerraToRCH
4. Lab 6 (1h): Quick validation

**Total**: 11 hours to end-to-end classification

---

## Key Resources

### Documentation
- **GDAL**: https://gdal.org/
- **PyTorch Lightning**: https://lightning.ai/docs/pytorch/stable/
- **Sentinel-2**: https://sentinels.copernicus.eu/web/sentinel/missions/sentinel-2
- **Google Earth Engine**: https://earthengine.google.com/

### Code Repositories
- **TerraToRCH**: https://github.com/torchgeo/torchgeo
- **Prithvi**: https://github.com/ibm/prithvi-eomae
- **Course Materials**: https://github.com/iceland-ml-course

### Papers & Reading
- "Attention Is All You Need" (Transformers): https://arxiv.org/abs/1706.03762
- "TerraToRCH: Foundation Models for Remote Sensing": https://arxiv.org/abs/2404.nnnnn
- "Vision Transformers in Remote Sensing": https://arxiv.org/abs/2101.01169

---

## Common Issues & Solutions

### Data Preprocessing (Lab 3.1)

**Q: How to handle missing or corrupted Sentinel-2 bands?**
```python
# Replace NaN/invalid values
data[np.isnan(data)] = 0
data[data < 0] = 0
data[data > 10000] = 10000
```

**Q: How to align different resolution bands?**
```python
# 10m bands: B02, B03, B04, B08
# 20m bands: B05, B06, B07, B8A, B11, B12
# Resample 20m to 10m using gdal
gdal.Warp(output, input, xRes=10, yRes=10)
```

### Training (Lab 4.1/5)

**Q: How to debug training convergence issues?**
```python
# Check gradients
for name, param in model.named_parameters():
    if param.grad is None:
        print(f"No gradient: {name}")
    else:
        print(f"{name}: grad_norm={param.grad.norm()}")

# Reduce learning rate if training is unstable
optimizer = torch.optim.Adam(model.parameters(), lr=1e-5)
```

**Q: How to handle imbalanced classes?**
```python
# Use weighted loss
from sklearn.utils.class_weight import compute_class_weight
weights = compute_class_weight('balanced', classes=np.unique(y_train), y=y_train)
loss = nn.CrossEntropyLoss(weight=torch.FloatTensor(weights))
```

### Validation (Lab 6)

**Q: How to fix low accuracy?**
1. Check data quality (Lab 3.1)
2. Try different hyperparameters
3. Use foundation models (Lab 7)
4. Collect more training data
5. Use data augmentation

---

## Project Completion Checklist

### Data & Preprocessing
- [ ] Downloaded Sentinel-2 imagery for your ROI
- [ ] Extracted spectral bands and created patches
- [ ] Extracted CORINE labels and aligned to tiles
- [ ] Created train/validation CSV files
- [ ] Verified data shapes and value ranges

### Custom Model (Lab 4-5)
- [ ] Built transformer architecture
- [ ] Trained on single GPU (Lab 4.1)
- [ ] Scaled to multi-GPU (Lab 5)
- [ ] Achieved >70% validation accuracy
- [ ] Saved best checkpoint

### Validation (Lab 6)
- [ ] Loaded trained model
- [ ] Ran inference on validation set
- [ ] Calculated confusion matrix
- [ ] Computed OA, PA, UA per class
- [ ] Compared with WorldCover/Esri
- [ ] Created visualizations

### Foundation Models (Lab 7)
- [ ] Installed TerraToRCH
- [ ] Fine-tuned on your data
- [ ] Achieved >80% accuracy
- [ ] Compared with custom model
- [ ] Exported for production

### Final Deliverables
- [ ] Training metrics plot
- [ ] Confusion matrix visualization
- [ ] Accuracy comparison table
- [ ] Prediction maps (GeoTIFF format)
- [ ] Written summary report

---

## Project Report Template

Create a final report summarizing:

```markdown
# Land Cover Classification Report

## Executive Summary
- ROI: [Your region in Iceland]
- Model: Custom Transformer + TerraToRCH
- Best Accuracy: XX%

## Methodology
- Data: Sentinel-2 Level 2A, CORINE labels
- Approach: Transfer learning with vision transformers
- Training: Multi-GPU DDP on HPC

## Results
| Model | OA | PA (mean) | UA (mean) |
|-------|----|----|---|
| Custom Transformer | XX% | XX% | XX% |
| TerraToRCH (Frozen) | XX% | XX% | XX% |
| TerraToRCH (Fine-tune) | XX% | XX% | XX% |

## Comparison with Products
- WorldCover: XX% OA vs our XX%
- Esri: XX% OA vs our XX%
- Improvement: +X percentage points

## Recommendations
- Use TerraToRCH for production
- Fine-tuning recommended for best accuracy
- Consider multi-temporal approach for seasonal changes
- Explore other foundation models (Prithvi, MOSAIK)

## Code & Data
- All code: [GitHub link]
- Final model: [Download link]
- Training data: [HPC path]
```

---

## Going Further

### Advanced Topics
1. **Multi-temporal Classification**: Use Sentinel-2 time series
2. **Multi-modal Fusion**: Combine with Sentinel-1 SAR data
3. **Semantic Segmentation**: Pixel-level predictions instead of patches
4. **Active Learning**: Iteratively collect most informative samples
5. **Few-shot Learning**: Classify new regions with minimal data

### Production Deployment
1. **Model Serving**: Deploy with TensorFlow Serving or TorchServe
2. **Web API**: Create REST API for classification
3. **Batch Processing**: Process large mosaics on HPC
4. **Monitoring**: Track model performance over time

### Research Extensions
1. **Benchmark**: Compare multiple foundation models
2. **Uncertainty Quantification**: Estimate prediction confidence
3. **Class Imbalance**: Handle rare land cover types
4. **Domain Adaptation**: Transfer to other regions/sensors

---

## Support & Community

- **Course Forum**: [Link to discussion forum]
- **Office Hours**: Thursdays 2-3 PM (Iceland time)
- **Slack Channel**: #iceland-ml-course
- **GitHub Issues**: Report bugs and request features

---

## Citation

If you use this course material in research, please cite:

```bibtex
@course{iceland2024,
  title={Machine Learning for Earth Observation with Sentinel-2},
  author={Course Instructors},
  year={2024},
  school={University of Iceland}
}
```

---

**Happy learning! Good luck with your Sentinel-2 classification project! 🌍🛰️**
