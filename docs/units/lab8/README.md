# Lab 8 — TerraTorch Fine-tuning (2 hours)

**Notebook:** [notebooks/finetune.ipynb](../../notebooks/finetune.ipynb)

## ⏱️ Time Allocation (2 hours)
- **15 min:** Introduction to TerraTorch and foundation models
- **25 min:** Configure TerraTorch for Iceland dataset
- **30 min:** Prepare data and configuration files
- **30 min:** Run fine-tuning (SLURM submission)
- **15 min:** Monitor training and checkpoints
- **5 min:** Compare with baseline and wrap-up

## Goals
### Core (Essential)
- Understand TerraTorch framework and foundation models
- Configure TerraTorch for Sentinel-2 land cover fine-tuning
- Prepare configuration YAML file
- Run fine-tuning job on JURECA GPU
- Track experiments and checkpoints

### Optional (Time Permitting)
- Compare multiple foundation models (Prithvi, SatMAE, etc.)
- Hyperparameter tuning experiments
- Learning rate finder
- Feature extraction vs full fine-tuning
- Multi-GPU training

## Outputs
### Required
- TerraTorch config tailored to course dataset
- Fine-tuned model checkpoint
- Training logs and metrics
- Notes on hyperparameters and performance

### Bonus
- Multiple model comparisons
- Hyperparameter sweep results
- Performance vs baseline analysis
- Inference benchmarks

## 📚 Session Structure

### Part 1: Foundation Models (15 min)
1. **TerraTorch Overview** (15 min)
   - What are foundation models?
   - Pre-training on large-scale Earth observation data
   - Benefits: better features, less data needed, faster convergence
   - Available models: Prithvi, SatMAE, SSL4EO, others
   - **Demo:** TerraTorch architecture overview

### Part 2: Configuration (55 min)
2. **Dataset Preparation** (25 min)
   - Convert patches to TerraTorch format
   - Create data manifest/index
   - Configure data loader
   - Test data loading
   - **Exercise:** Prepare your dataset

3. **Configuration File** (30 min)
   - YAML structure overview
   - Model selection and settings
   - Training hyperparameters
   - Data augmentation
   - Logging and checkpointing
   - **Exercise:** Create config for Iceland dataset
   - **Demo:** Walk through sample config

### Part 3: Fine-tuning Execution (45 min)
4. **CLI and SLURM** (15 min)
   - TerraTorch CLI commands
   - SLURM script for GPU job
   - Resource allocation
   - Environment setup
   - **Demo:** Submit fine-tuning job

5. **Monitor Training** (20 min)
   - Check job status
   - View logs in real-time
   - TensorBoard (if available)
   - Identify issues
   - **Exercise:** Monitor your job

6. **Checkpoints and Artifacts** (10 min)
   - Locate saved checkpoints
   - Understand checkpoint contents
   - Best model selection
   - Export for inference
   - **Exercise:** Inspect checkpoint

### Part 4: Analysis and Comparison (5+ min)
7. **Compare with Baseline** (if time permits)
   - Convergence speed
   - Final accuracy
   - Training time
   - Generalization
   - **Discussion:** Benefits of fine-tuning

8. **Q&A and Course Wrap-up** (5 min)

## 🎯 If You Finish Early
- **Model Comparison:**
  - Fine-tune multiple foundation models (Prithvi vs SatMAE)
  - Compare convergence rates
  - Evaluate on test set
  - Ensemble predictions

- **Hyperparameter Tuning:**
  - Learning rate sweep
  - Batch size experiments
  - Augmentation strategies
  - Freezing strategies (freeze encoder, fine-tune head only)

- **Advanced Training:**
  - Multi-GPU distributed training
  - Mixed precision training
  - Gradient accumulation
  - Learning rate scheduling (cosine, warmup)

- **Inference Optimization:**
  - Model quantization
  - ONNX export
  - Batch inference on full scenes
  - Speed benchmarks

- **Domain Adaptation:**
  - Fine-tune on Iceland, test on other regions
  - Few-shot learning experiments
  - Transfer to different land cover schemes

- **Experiment Tracking:**
  - Set up Weights & Biases or MLflow
  - Log hyperparameters systematically
  - Compare multiple runs
  - Create experiment dashboard

## ✂️ If Running Out of Time
**Priority 1 (Must Complete - 75 min):**
- TerraTorch introduction (10 min)
- Prepare dataset (20 min)
- Create config file (20 min)
- Submit SLURM job (15 min)
- Verify job started (10 min)

**Can Skip:**
- Detailed foundation model theory
- Multiple model comparison
- Real-time monitoring (check later)
- Performance analysis

**Can Run Asynchronously:**
- Fine-tuning runs during/after class
- Students check results later
- Analysis in follow-up session or homework

**Minimal Viable Lab (90 min):**
- Quick intro (5 min saved)
- Use template config (10 min saved)
- Pre-prepared dataset (10 min saved)
- Submit and verify (15 min)
- (Total: 30 min saved)

**Backup Plan:**
- If TerraTorch issues: Focus on concepts, use demo
- If GPU unavailable: Submit job for later, analyze previous run
- If config errors: Provide working template
- If time critical: Demo-only session with provided results

## 🔧 TerraTorch Quick Reference

**Installation:**
```bash
pip install terratorch
```

**Basic Config Structure:**
```yaml
task: classification
model:
  name: prithvi
  pretrained: true
  num_classes: 5
data:
  train_path: /path/to/train
  val_path: /path/to/val
  batch_size: 32
training:
  epochs: 20
  learning_rate: 1e-4
  optimizer: adamw
```

**CLI Commands:**
```bash
# Fine-tune
terratorch fit --config config.yaml

# Evaluate
terratorch test --config config.yaml --ckpt best.ckpt

# Predict
terratorch predict --config config.yaml --ckpt best.ckpt --input data/
```
