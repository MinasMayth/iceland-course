# Iceland ML Labs - Quick Reference Guide

## 📋 Overview

This document provides a quick reference for all 6 lab sessions in the TÖV606M Machine Learning for Earth Observation course. Each lab is designed for a 40-minute session and builds progressively toward a complete ML pipeline.

---

## 🗓️ Lab Schedule

| Week | Lab | Topic | Duration | Deliverables |
|------|-----|-------|----------|--------------|
| 1 | Lab 1 | Judoor & HPC Access | 40 min | Judoor account, SSH access to JURECA |
| 3 | Lab 2 | Jupyter-JSC & Git | 40 min | Jupyter session, Git repo clone, Python kernel |
| 6 | Lab 3 | GEE & Sentinel-2 | 40 min | 4 Sentinel-2 scenes, metadata |
| 8 | Lab 4 | Data Preprocessing | 40 min | ML-ready dataset (train/val/test splits) |
| 11 | Lab 5.1 | Model Training | 40 min | Trained CNN model, checkpoints |
| 12 | Lab 5.2 | Model Evaluation | 40 min | Evaluation report, confusion matrix |

---

## 📚 Lab Details

### Lab 1: Judoor Account and Access to HPC
**Location:** [`notebooks/iceland-ml/lab1_judoor_hpc_access.ipynb`](../../notebooks/iceland-ml/lab1_judoor_hpc_access.ipynb)

**Before Lab:**
- Prepare your university email address
- Ensure you have SSH client installed

**During Lab:**
1. Create Judoor account (https://judoor.fz-juelich.de)
2. Join `training2600` project
3. Generate SSH key pair
4. Connect to JURECA
5. Explore filesystem structure

**After Lab:**
- Verify you can SSH into JURECA
- Create workspace directory structure
- Test basic SLURM commands

**Key Commands:**
```bash
ssh-keygen -t ed25519 -C "your_email@hi.is"
ssh jureca
cd $PROJECT_training2600
mkdir -p my_workspace/{data,notebooks,scripts,models,results}
```

---

### Lab 2: Jupyter-JSC and Git Basics
**Location:** [`notebooks/iceland-ml/lab2_jupyter_jsc_git.ipynb`](../../notebooks/iceland-ml/lab2_jupyter_jsc_git.ipynb)

**Before Lab:**
- Ensure Lab 1 is complete (working SSH access)
- Install Git locally (if working from personal machine)

**During Lab:**
1. Launch Jupyter-JSC session
2. Learn Git basics (clone, commit, push, pull)
3. Clone the Iceland ML course repository
4. Create Python virtual environment
5. Register custom Jupyter kernel
6. Run first analysis notebook

**After Lab:**
- Practice Git workflow
- Explore JupyterLab interface
- Install additional packages in venv

**Key Commands:**
```bash
# In Jupyter-JSC terminal
git clone https://github.com/YOUR_ORG/iceland-ml-course.git
python -m venv ~/envs/ml_eo_course
source ~/envs/ml_eo_course/bin/activate
python -m ipykernel install --user --name=ml_eo_course
```

---

### Lab 3: Google Earth Engine - Sentinel-2 Data Acquisition
**Location:** [`notebooks/iceland-ml/lab3_gee_sentinel2_acquisition.ipynb`](../../notebooks/iceland-ml/lab3_gee_sentinel2_acquisition.ipynb)

**Before Lab:**
- Create GEE account (https://earthengine.google.com/signup)
- May take 1-2 days for approval

**During Lab:**
1. Authenticate GEE in notebook
2. Define AOI in Iceland (Þingvellir region)
3. Query Sentinel-2 image collection
4. Filter by cloud cover (<20%)
5. Visualize scenes (RGB, false color)
6. Export/download 4 scenes

**After Lab:**
- Verify downloaded imagery
- Explore different AOIs
- Experiment with date ranges

**Key Sentinel-2 Bands:**
- B2 (Blue), B3 (Green), B4 (Red)
- B8 (NIR), B11 (SWIR1), B12 (SWIR2)

---

### Lab 4: Data Preprocessing and Patch Extraction
**Location:** [`notebooks/iceland-ml/lab4_preprocessing_patches.ipynb`](../../notebooks/iceland-ml/lab4_preprocessing_patches.ipynb)

**Before Lab:**
- Ensure Lab 3 is complete (downloaded imagery)
- Review NumPy basics

**During Lab:**
1. Load GeoTIFF imagery with rasterio
2. Extract 224×224 patches
3. Apply normalization (standardization)
4. Generate/match CORINE labels
5. Create train/val/test split (70/15/15)
6. Save as NumPy arrays

**After Lab:**
- Inspect saved dataset shapes
- Verify normalization parameters
- Check class balance

**Output Files:**
- `X_train.npy`, `y_train.npy`
- `X_val.npy`, `y_val.npy`
- `X_test.npy`, `y_test.npy`
- `dataset_metadata.json`
- `normalization_params.json`

---

### Lab 5.1: Baseline Model Training
**Location:** [`notebooks/iceland-ml/lab5.1_baseline_training.ipynb`](../../notebooks/iceland-ml/lab5.1_baseline_training.ipynb)

**Before Lab:**
- Ensure Lab 4 is complete (preprocessed data)
- Familiarize with PyTorch basics

**During Lab:**
1. Build CNN architecture (4 conv layers)
2. Create PyTorch DataLoaders
3. Define loss function and optimizer
4. Implement training loop
5. Train for 20 epochs with early stopping
6. Save best model checkpoint

**After Lab:**
- Analyze training curves
- Experiment with hyperparameters
- Try different architectures

**Key Hyperparameters:**
- Batch size: 32
- Learning rate: 0.001
- Optimizer: Adam
- Scheduler: ReduceLROnPlateau

---

### Lab 5.2: Model Evaluation Metrics
**Location:** [`notebooks/iceland-ml/lab5.2_model_evaluation.ipynb`](../../notebooks/iceland-ml/lab5.2_model_evaluation.ipynb)

**Before Lab:**
- Ensure Lab 5.1 is complete (trained model)
- Review confusion matrix concepts

**During Lab:**
1. Load trained model and test data
2. Generate predictions
3. Calculate metrics (accuracy, precision, recall, F1)
4. Create confusion matrix
5. Visualize correct/incorrect predictions
6. Generate comprehensive report

**After Lab:**
- Identify model weaknesses
- Plan improvements
- Document findings

**Key Metrics:**
- **Accuracy:** Overall correctness
- **Precision:** Of predicted positives, how many are correct?
- **Recall:** Of actual positives, how many did we find?
- **F1-Score:** Harmonic mean of precision and recall

---

## 🔧 Common Issues & Solutions

### Issue: Jupyter-JSC job pending
**Solution:** System may be busy. Wait 5-10 min or request fewer resources.

### Issue: GEE authentication fails
**Solution:** Clear browser cache, use incognito mode, re-authenticate.

### Issue: Out of memory during training
**Solution:** Reduce batch size, use CPU if GPU full, submit batch job.

### Issue: Git conflicts when pulling
**Solution:** Commit or stash changes first: `git stash`, `git pull`, `git stash pop`

### Issue: SLURM job fails immediately
**Solution:** Check project membership, verify partition name, review error logs.

---

## 📊 Expected Results

By the end of all labs, you should have:

✅ **Infrastructure:**
- Working HPC access (Judoor + JURECA)
- Jupyter-JSC sessions
- Git-managed repository

✅ **Data:**
- 4 Sentinel-2 scenes (Iceland, summer 2024)
- ~100-500 preprocessed patches
- Train/val/test splits

✅ **Models:**
- Trained baseline CNN (~1-2M parameters)
- Model checkpoints
- Training curves

✅ **Evaluation:**
- Accuracy: 60-85% (depends on data quality)
- Confusion matrix
- Per-class performance metrics
- Evaluation report

---

## 🚀 Next Steps After Labs

### Improve Performance
1. **Data Augmentation:** Random flips, rotations, color jittering
2. **Pre-trained Models:** ResNet, EfficientNet from torchvision
3. **Foundation Models:** TerraTorch, Prithvi (covered in Rocco's lessons)
4. **Ensemble Methods:** Combine multiple models

### Expand Scope
1. **More Data:** Acquire 10-20 scenes, multiple seasons
2. **Temporal Analysis:** Time series classification
3. **Semantic Segmentation:** Pixel-level predictions
4. **Change Detection:** Compare scenes across years

### Deploy for Production
1. **Optimize Inference:** ONNX export, TensorRT
2. **Scale Up:** Distributed inference with Dask
3. **Web Interface:** Flask/FastAPI + Leaflet map
4. **Monitoring:** Track model drift over time

---

## 📖 Additional Resources

### Documentation
- [JSC JURECA Docs](https://apps.fz-juelich.de/jsc/hps/jureca/)
- [Jupyter-JSC Guide](https://apps.fz-juelich.de/jsc/hps/jupyter/)
- [Google Earth Engine Docs](https://developers.google.com/earth-engine)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [Rasterio Docs](https://rasterio.readthedocs.io)

### Datasets
- [Sentinel-2 L2A](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED)
- [CORINE Land Cover](https://land.copernicus.eu/pan-european/corine-land-cover)
- [EO Benchmark Datasets](https://github.com/satellite-image-deep-learning/datasets)

### Research Papers
- [Prithvi: Foundation Model for Geospatial Data](https://arxiv.org/abs/2310.18660)
- [TerraTorch: Geospatial Foundation Models](https://github.com/IBM/terratorch)
- [ResNet for Remote Sensing](https://arxiv.org/abs/1512.03385)

---

## 💬 Getting Help

### During Lab Sessions
- Ask questions directly in Zoom/Teams
- Use Slack for quick questions
- Screen share if troubleshooting needed

### Outside Lab Sessions
- **Slack Channel:** Post questions with error messages and screenshots
- **Email:** s.hashim@fz-juelich.de (response within 24-48 hours)
- **Office Hours:** Schedule via email (3 days advance)

### Tips for Effective Questions
1. Include error message (full traceback)
2. Describe what you tried
3. Share relevant code snippet
4. Mention which lab/section

---

## ✅ Lab Completion Checklist

Use this to track your progress:

- [ ] Lab 1: Successfully SSH into JURECA
- [ ] Lab 1: Created workspace directory structure
- [ ] Lab 2: Launched Jupyter-JSC session
- [ ] Lab 2: Cloned course repository with Git
- [ ] Lab 3: Authenticated Google Earth Engine
- [ ] Lab 3: Downloaded 4 Sentinel-2 scenes
- [ ] Lab 4: Generated preprocessed dataset (train/val/test)
- [ ] Lab 4: Saved normalization parameters
- [ ] Lab 5.1: Trained baseline CNN model
- [ ] Lab 5.1: Saved model checkpoint
- [ ] Lab 5.2: Calculated evaluation metrics
- [ ] Lab 5.2: Generated confusion matrix
- [ ] Lab 5.2: Created evaluation report

---

## 🎓 Final Project Ideas

Apply what you learned:

1. **Urban Growth Detection:** Compare Reykjavik area across multiple years
2. **Glacier Monitoring:** Track Vatnajökull ice coverage changes
3. **Vegetation Mapping:** Classify Iceland's unique flora
4. **Coastal Analysis:** Map coastline and wetland changes
5. **Volcanic Activity:** Detect lava fields and bare rock

---

**Good luck with your labs! Remember: The best way to learn is by doing. Don't hesitate to experiment and make mistakes!** 🚀

**Questions?** Contact Samy at s.hashim@fz-juelich.de
