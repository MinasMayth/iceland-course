# Iceland ML Course - Complete Lab Index

**Machine Learning for Earth Observation: Sentinel-2 Classification with Foundation Models**

---

## 📚 Lab Curriculum

### Foundation (Prerequisites)
- [Lab 1: Judoor HPC Access](lab1_judoor_hpc_access.ipynb) - 30 min
- [Lab 2: Jupyter-JSC & Git](lab2_jupyter_jsc_git.ipynb) - 2 hours

### Data Pipeline
- [Lab 3.1: Data Download (GEE)](lab3_1_gee_data_download.ipynb) - 2 hours
- [Lab 3.2: Data Preprocessing](lab3_2_data_preprocessing.ipynb) - 3 hours

### Deep Learning Fundamentals
- [Lab 4: Understanding Transformers](lab4_data_classification.ipynb) - 2 hours

### Model Training
- [Lab 4.1: Training Transformers](lab4_1_transformer_training.ipynb) - 6-8 hours
- [Lab 5: Distributed Deep Learning](lab5_distributed_deep_learning.ipynb) - 2 hours

### Evaluation & Production
- [Lab 6: Performance Metrics](lab6_performance_metrics_validation.ipynb) - 2 hours
- [Lab 7: Foundation Models & TerraToRCH](lab7_foundation_models_terratorch.ipynb) - 2-3 hours

---

## 🎯 Quick Navigation

### I want to...

**...understand the complete project**
- Read [PROJECT_GUIDE.md](PROJECT_GUIDE.md) first
- Then [LAB_COHERENCE.md](LAB_COHERENCE.md) for visual workflows

**...get started quickly (11 hours)**
1. Use existing preprocessed data
2. Jump to Lab 4.1
3. Skip to Lab 7 for foundation models
4. Quick validation in Lab 6

**...learn from scratch (25 hours)**
1. Start with Labs 1-2 for setup
2. Do Labs 3.1-3.2 for data
3. Learn theory in Lab 4
4. Train model in Labs 4.1-5
5. Validate in Lab 6
6. Deploy in Lab 7

**...download my own satellite data**
→ [Lab 3.1: Data Download](lab3_1_gee_data_download.ipynb)

**...preprocess geospatial data with GDAL**
→ [Lab 3.2: Data Preprocessing](lab3_2_data_preprocessing.ipynb)

**...skip to foundation models**
- Prerequisite: Preprocessed Sentinel-2 data + CORINE labels
- Go directly to Lab 7
- 2-3 hours to 85-92% accuracy

---

## 📊 Project Metrics

### Accuracy Progression
```
Custom Transformer (Lab 4.1):    75-80% OA
TerraToRCH Frozen (Lab 7):       84-87% OA
TerraToRCH Fine-tuned (Lab 7):   87-92% OA
```

### Time & Resource Summary

| Lab | Duration | GPU | Output | Key Skill |
|-----|----------|-----|--------|----------|
| 1-2 | 3h | - | Environment | HPC basics |
| 3.1 | 2h | - | S2 + CORINE GeoTIFF | GEE API |
| 3.2 | 3h | - | Training CSVs | GDAL/Geospatial |
| 4 | 2h | - | Knowledge | DL theory |
| 4.1 | 6-8h | 1x V100 | 75% model | PyTorch |
| 5 | 2h | 8x V100 | Optimized | DDP |
| 6 | 2h | 1x GPU | Report | Metrics |
| 7 | 3h | 1x V100 | 90% model | Transfer learning |

---

## 🔗 Lab Dependencies

```
Lab 1 ──→ Lab 2 ──→ Lab 3.1 ──┐
                   ↓           │
              Lab 3.2        Lab 4 ──→ Lab 4.1 ──→ Lab 5 ──┐
                                       ↓                    ↓
                                    Lab 6 ←─────────────────┘
                                       ↓
                                    Lab 7 (Foundation Models)
```

**Critical Path** (must follow): 1 → 2 → 3.1 → 3.2 → 4.1 → 7  
**Parallel** (can do anytime): Lab 4 while data processes  
**Optional Enhancement** (recommended): Lab 5 for faster iteration

---

## 📁 File Structure

```
notebooks/iceland-ml/
├── README.md (this file)
├── PROJECT_GUIDE.md (complete project overview)
├── LAB_COHERENCE.md (visual workflows and timelines)
├── LAB_3_RESTRUCTURING_SUMMARY.md (what changed)
│
├── Lab 1: Setup
│   └── lab1_judoor_hpc_access.ipynb
│
├── Lab 2: Development Environment
│   └── lab2_jupyter_jsc_git.ipynb
│
├── Lab 3: Data Acquisition & Preprocessing
│   ├── lab3_1_gee_data_download.ipynb (NEW - download from GEE)
│   ├── lab3_2_data_preprocessing.ipynb (GDAL processing)
│   └── lab3_1/ (code folder)
│       ├── extract_corinemap.ipynb
│       ├── openRaster.ipynb
│       ├── extract_s2.py
│       ├── submit_extract_s2.sh
│       └── data/
│           ├── trainSet1_cleaned.csv
│           └── valSet1_cleaned.csv
│
├── Lab 4: Learning
│   └── lab4_data_classification.ipynb
│
├── Lab 4.1: Custom Transformer Training
│   ├── lab4_1_transformer_training.ipynb
│   └── lab4_1/ (code folder)
│       ├── train_transformer.py
│       ├── submit_training.sh
│       └── data/ (links to lab3_1/data)
│
├── Lab 5: Distributed Training
│   └── lab5_distributed_deep_learning.ipynb
│
├── Lab 6: Validation
│   └── lab6_performance_metrics_validation.ipynb
│
└── Lab 7: Foundation Models
    └── lab7_foundation_models_terratorch.ipynb
```

---

## 🚀 Getting Started

### Option 1: Complete Course (Recommended)

```bash
# 1. Start with foundation labs
jupyter lab lab1_judoor_hpc_access.ipynb
jupyter lab lab2_jupyter_jsc_git.ipynb

# 2. Acquire and preprocess data
jupyter lab lab3_1_gee_data_download.ipynb  # Download from GEE
jupyter lab lab3_2_data_preprocessing.ipynb  # Prepare with GDAL

# 3. Learn theory
jupyter lab lab4_data_classification.ipynb

# 4. Train models
jupyter lab lab4_1_transformer_training.ipynb  # Custom transformer
jupyter lab lab5_distributed_deep_learning.ipynb  # Scale up

# 5. Validate
jupyter lab lab6_performance_metrics_validation.ipynb

# 6. Production
jupyter lab lab7_foundation_models_terratorch.ipynb  # Foundation models
```

**Total Time**: 25 hours  
**Final Accuracy**: 85-92%

### Option 2: Fast Track (Skip Theory)

```bash
# Assuming you have preprocessed Sentinel-2 data

# 1. Train custom transformer (6-8 hours)
jupyter lab lab4_1_transformer_training.ipynb

# 2. Validate (1 hour)
jupyter lab lab6_performance_metrics_validation.ipynb

# 3. Deploy foundation model (2 hours)
jupyter lab lab7_foundation_models_terratorch.ipynb
```

**Total Time**: 11 hours  
**Final Accuracy**: 85-90%

### Option 3: Foundation Models Only

```bash
# Production-oriented approach
# Requires: preprocessed Sentinel-2 data

jupyter lab lab7_foundation_models_terratorch.ipynb
```

**Total Time**: 3 hours  
**Final Accuracy**: 85-92%

---

## 📖 Learning Paths

### Path A: Complete Understanding
**Target**: Master all aspects of ML for Earth Observation

```
Labs: 1 → 2 → 4 → 3.1 → 3.2 → 4.1 → 5 → 6 → 7
Focus: Theory → Data → Implementation → Optimization → Production
Time: 25 hours
Best for: Students, researchers wanting deep knowledge
```

### Path B: Practical Application
**Target**: Build a working classifier quickly

```
Labs: 2 → 3.1 → 3.2 → 4.1 → 6 → 7
Focus: Data → Training → Validation → Production
Time: 18 hours
Best for: Practitioners, geospatial professionals
```

### Path C: Rapid Deployment
**Target**: Get production model in minimal time

```
Labs: 7 (with preprocessed data)
Focus: Transfer learning → Deployment
Time: 3 hours
Best for: Production teams, quick prototyping
```

---

## 💡 Key Concepts by Lab

### Lab 1-2: Infrastructure
- HPC job scheduling (Slurm)
- Version control (Git)
- Python virtual environments
- Jupyter notebooks on HPC

### Lab 3.1-3.2: Data
- Sentinel-2 imagery structure
- Google Earth Engine API (Lab 3.1)
- GDAL geospatial operations (Lab 3.2)
- Coordinate Reference Systems (CRS)
- Raster reprojection & resampling
- CORINE land cover labels

### Lab 4: Theory
- PyTorch tensors
- Automatic differentiation (autograd)
- Self-attention mechanisms
- Multi-head attention
- Transformer architecture
- Vision transformers

### Lab 4.1: Implementation
- Custom model architecture
- PyTorch Lightning training
- Data loading pipelines
- Loss functions & optimization
- Model checkpointing
- Single-GPU training

### Lab 5: Scaling
- Distributed Data Parallel (DDP)
- Multi-GPU synchronization
- Gradient averaging
- NCCL communication backend
- Training at scale
- Performance monitoring

### Lab 6: Validation
- Confusion matrices
- Overall accuracy (OA)
- Producer's accuracy (PA)
- User's accuracy (UA)
- Errors of omission/commission
- Cross-product comparisons
- Metric visualization

### Lab 7: Production
- Transfer learning
- Foundation models
- Pre-trained backbones
- Fine-tuning strategies
- Model export & deployment
- Large-scale inference
- Production optimization

---

## 🎓 Learning Outcomes

After completing this course, you will be able to:

✅ **Acquire satellite imagery** from Google Earth Engine  
✅ **Preprocess geospatial data** with GDAL  
✅ **Build deep learning models** with PyTorch  
✅ **Train transformers** for image classification  
✅ **Scale training** across multiple GPUs  
✅ **Validate models** with comprehensive metrics  
✅ **Leverage foundation models** for production systems  
✅ **Deploy classifiers** for large-scale inference  

---

## 🔗 Important Resources

### Documentation
- [Google Earth Engine API](https://developers.google.com/earth-engine)
- [GDAL Documentation](https://gdal.org/)
- [PyTorch Documentation](https://pytorch.org/docs/stable/index.html)
- [PyTorch Lightning Docs](https://lightning.ai/docs/pytorch/stable/)
- [Sentinel-2 Product Specification](https://sentinels.copernicus.eu/)

### Related Materials
- [LAB_3_RESTRUCTURING_SUMMARY.md](LAB_3_RESTRUCTURING_SUMMARY.md) - What changed in Lab 3
- [PROJECT_GUIDE.md](PROJECT_GUIDE.md) - Detailed project overview
- [LAB_COHERENCE.md](LAB_COHERENCE.md) - Visual workflows
- Original Lab 3 code: `lab3_1/code/`
- Original Lab 4.1 code: `lab4_1/code/`

### Research Papers
- "Attention Is All You Need" (Transformers): https://arxiv.org/abs/1706.03762
- "An Image is Worth 16x16 Words" (ViT): https://arxiv.org/abs/2010.11929
- "TerraToRCH: Foundation Models for Remote Sensing"
- "Prithvi: A Foundation Model for Earth Observation": https://github.com/ibm/prithvi-eomae

---

## ❓ FAQ

**Q: What's different about Lab 3 now?**  
A: Lab 3.1 now focuses on downloading data from Google Earth Engine (instead of preprocessing), and Lab 3.2 handles preprocessing. See [LAB_3_RESTRUCTURING_SUMMARY.md](LAB_3_RESTRUCTURING_SUMMARY.md).

**Q: Do I need to do all labs?**  
A: No. You can skip Lab 4 (theory) if you already understand transformers. Lab 5 is optional. Labs 1, 3, and 7 are essential.

**Q: Can I use different satellite data?**  
A: Yes! The methods work for any multi-spectral satellite data. Adjust band selections and preprocessing accordingly.

**Q: What if my accuracy is too low?**  
A: Check data quality (Lab 3.1), try different hyperparameters, use foundation models (Lab 7), or collect more training data.

**Q: How do I deploy my model?**  
A: Lab 7 includes export to ONNX and PyTorch formats. Wrap in a web API or inference server for production.

**Q: Can I run this on my laptop?**  
A: No. GPU is essential. Use the HPC cluster provided in Labs 1-2. You need at least a GPU with 8GB memory.

---

## 📞 Support

- **Course Forum**: [Link]
- **Office Hours**: Thursdays 2-3 PM (Iceland time)
- **Slack Channel**: #iceland-ml-course
- **GitHub Issues**: Report bugs and request features

---

## 📝 Citation

If you use this course material in research:

```bibtex
@course{iceland2024,
  title={Machine Learning for Earth Observation with Sentinel-2},
  author={Course Instructors},
  year={2024},
  school={University of Iceland},
  url={https://github.com/iceland-ml-course}
}
```

---

## ✨ Next Steps

1. **Read**: [PROJECT_GUIDE.md](PROJECT_GUIDE.md) for complete overview
2. **Check**: [LAB_3_RESTRUCTURING_SUMMARY.md](LAB_3_RESTRUCTURING_SUMMARY.md) to understand Lab 3 changes
3. **Choose**: Your learning path (A, B, or C)
4. **Start**: With the first recommended lab
5. **Ask**: Questions on the course forum
6. **Share**: Your results and improvements!

---

**Welcome to the Iceland ML Course! Happy learning! 🌍🛰️**
