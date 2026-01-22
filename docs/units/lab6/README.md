# Lab 6 — Baseline Model Training (2 hours)

**Notebook:** [notebooks/iceland-ml/lab5.1_baseline_training.ipynb](../../notebooks/iceland-ml/lab5.1_baseline_training.ipynb)

## ⏱️ Time Allocation (2 hours)
- **15 min:** Introduction to CNN architectures
- **25 min:** Build CNN model with PyTorch
- **30 min:** Implement DataLoaders and training loop
- **25 min:** Training on GPU with SLURM
- **20 min:** Monitor training and checkpointing
- **5 min:** Wrap-up and next steps

## Goals
### Core (Essential)
- Build a CNN classifier with PyTorch (4-5 conv layers)
- Implement DataLoaders for patch datasets
- Create training loop with loss and optimizer
- Submit GPU job via SLURM
- Capture checkpoints and training logs

### Optional (Time Permitting)
- Experiment with architectures (ResNet, EfficientNet)
- Learning rate scheduling strategies
- Early stopping and model selection
- Mixed precision training
- Hyperparameter tuning

## Outputs
### Required
- Trained baseline model checkpoint
- Training curves (loss/accuracy) plotted
- Training logs and configuration
- SLURM script for reproducibility

### Bonus
- Multiple architecture comparisons
- Hyperparameter sweep results
- TensorBoard logs
- Model performance analysis

## 📚 Session Structure

### Part 1: Model Architecture (40 min)
1. **CNN Fundamentals** (15 min)
   - Convolutional layers
   - Pooling and downsampling
   - Fully connected layers
   - Activation functions
   - **Demo:** CNN visualization

2. **Build PyTorch Model** (25 min)
   - Define CNN architecture
   - Input: (B, 6, 224, 224) - 6 Sentinel-2 bands
   - Output: (B, num_classes)
   - Count parameters
   - Test forward pass
   - **Exercise:** Modify architecture

### Part 2: Data Loading and Training (55 min)
3. **PyTorch DataLoader** (20 min)
   - Create Dataset class
   - Load NPZ patches
   - Implement `__getitem__` and `__len__`
   - Configure DataLoader (batch_size, shuffle, num_workers)
   - **Exercise:** Test data loading speed

4. **Training Loop** (20 min)
   - Define loss function (CrossEntropyLoss)
   - Choose optimizer (Adam, SGD)
   - Learning rate scheduling
   - Training iteration logic
   - Validation loop
   - **Demo:** Train for 2-3 epochs locally

5. **Checkpointing** (15 min)
   - Save model state_dict
   - Save optimizer state
   - Best model selection
   - Resume training
   - **Exercise:** Implement checkpoint saving

### Part 3: GPU Training with SLURM (25 min)
6. **SLURM Job Submission** (15 min)
   - GPU partition overview
   - SLURM script structure
   - Resource allocation (GPU, CPU, memory)
   - Module loading
   - **Demo:** Submit training job

7. **Monitor Training** (10 min)
   - Check job status (`squeue`)
   - View logs in real-time
   - Identify errors
   - Cancel/resubmit if needed
   - **Exercise:** Monitor your job

### Part 4: Analysis and Wrap-up (10+ min)
8. **Training Curves** (5+ min)
   - Plot loss over epochs
   - Plot accuracy over epochs
   - Identify overfitting
   - **Exercise:** Interpret curves

9. **Q&A and Next Steps** (5 min)

## 🎯 If You Finish Early
- **Advanced Architectures:**
  - Implement ResNet-18 or ResNet-34
  - Try EfficientNet-B0
  - Use pretrained ImageNet weights (transfer learning)
  - Compare with U-Net for segmentation
  - Multi-scale input fusion

- **Training Enhancements:**
  - Implement early stopping
  - Cyclic learning rate
  - Learning rate finder
  - Gradient clipping
  - Weight decay and regularization

- **Experiment Tracking:**
  - Set up TensorBoard
  - Log hyperparameters
  - Track additional metrics (F1, precision, recall)
  - Save best N models
  - Experiment versioning

- **Hyperparameter Tuning:**
  - Grid search over learning rates
  - Batch size experiments
  - Optimizer comparison (Adam vs SGD vs AdamW)
  - Augmentation impact
  - Architecture depth/width

- **Advanced Techniques:**
  - Mixed precision training (FP16)
  - Gradient accumulation for larger batch sizes
  - Label smoothing
  - Focal loss for imbalanced classes
  - Weighted sampling

## ✂️ If Running Out of Time
**Priority 1 (Must Complete - 75 min):**
- Build simple CNN (20 min)
- Create DataLoader (15 min)
- Basic training loop (20 min)
- Submit SLURM job (15 min)
- Verify job started (5 min)

**Can Skip:**
- Learning rate scheduling (use fixed LR)
- Advanced checkpointing (save final model only)
- Detailed architecture exploration
- Early stopping implementation

**Can Run Asynchronously:**
- Full training (20 epochs) runs during/after class
- Students check results later
- Analysis in next lab

**Minimal Viable Lab (90 min):**
- Pre-built CNN class (10 min saved)
- Train 5 epochs instead of 20 (15 min saved)
- Simple SLURM template (5 min saved)
- Skip live monitoring
- (30 min saved total)

**Backup Plan:**
- If GPU unavailable: Train on CPU for 2-3 epochs (slower but works)
- If SLURM issues: Train interactively in Jupyter (less efficient)
- If time critical: Provide pre-trained model, focus on understanding architecture
