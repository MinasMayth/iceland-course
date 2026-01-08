# Lab 7 — Model Evaluation (2 hours)

**Notebook:** [notebooks/iceland-ml/lab5.2_model_evaluation.ipynb](../../notebooks/iceland-ml/lab5.2_model_evaluation.ipynb)

## ⏱️ Time Allocation (2 hours)
- **10 min:** Introduction to evaluation metrics
- **20 min:** Load model and generate predictions
- **30 min:** Calculate metrics (accuracy, precision, recall, F1)
- **30 min:** Confusion matrix and visualization
- **20 min:** Error analysis and insights
- **10 min:** Report generation and next steps

## Goals
### Core (Essential)
- Load trained model and test data
- Generate predictions on test set
- Compute accuracy, precision, recall, F1 scores
- Create and analyze confusion matrix
- Identify misclassification patterns

### Optional (Time Permitting)
- Per-class performance deep dive
- ROC curves and AUC
- Precision-recall curves
- Spatial error analysis
- Model comparison (baseline vs alternatives)

## Outputs
### Required
- Evaluation report with all metrics
- Confusion matrix plot
- Per-class metrics table
- Sample predictions (correct and incorrect)
- Recommendations for improvements

### Bonus
- ROC/PR curves
- Spatial error map
- Class-specific analysis
- Comparative evaluation report

## 📚 Session Structure

### Part 1: Setup and Predictions (30 min)
1. **Evaluation Metrics Overview** (10 min)
   - Accuracy: when to use and limitations
   - Precision: false positive cost
   - Recall: false negative cost
   - F1-score: harmonic mean
   - Confusion matrix interpretation
   - **Demo:** Metrics on toy example

2. **Load Model and Data** (20 min)
   - Load trained checkpoint
   - Load test patches (NPZ)
   - Set model to eval mode
   - Generate predictions on test set
   - **Exercise:** Predict on your test data
   - **Troubleshooting:** CUDA/device issues

### Part 2: Metric Calculation (30 min)
3. **Compute Metrics** (15 min)
   - Overall accuracy
   - Per-class precision
   - Per-class recall
   - Per-class F1-score
   - Macro vs weighted averages
   - **Exercise:** Calculate using sklearn

4. **Interpretation** (15 min)
   - Which classes perform well?
   - Which classes are confused?
   - Class imbalance impact
   - Statistical significance
   - **Discussion:** Why these results?

### Part 3: Confusion Matrix (30 min)
5. **Create Confusion Matrix** (15 min)
   - Compute confusion matrix
   - Normalize (rows, columns, or all)
   - Visualize as heatmap
   - Annotate with counts/percentages
   - **Exercise:** Create your confusion matrix

6. **Analysis** (15 min)
   - Identify common confusions
   - Spectral similarity analysis
   - Spatial patterns in errors
   - Label quality issues
   - **Discussion:** Root causes

### Part 4: Error Analysis (30 min)
7. **Visualize Predictions** (15 min)
   - Show correctly classified samples
   - Show misclassified samples
   - Side-by-side: RGB, prediction, ground truth
   - Highlight problematic patches
   - **Exercise:** Create visualization grid

8. **Deep Dive** (15 min)
   - Focus on worst-performing classes
   - Analyze specific confusion pairs
   - Check for systematic biases
   - Review training data quality
   - **Discussion:** Improvement strategies

### Part 5: Reporting and Wrap-up (10+ min)
9. **Generate Report** (5 min)
   - Compile all metrics
   - Include visualizations
   - Add interpretation and recommendations
   - **Exercise:** Create summary table

10. **Q&A and Next Steps** (5 min)
    - Preview fine-tuning lab
    - Discuss potential improvements

## 🎯 If You Finish Early
- **Advanced Metrics:**
  - ROC curves for each class (one-vs-rest)
  - AUC (Area Under Curve)
  - Precision-Recall curves
  - Matthews Correlation Coefficient
  - Cohen's Kappa

- **Spatial Analysis:**
  - Map predictions back to geographic space
  - Create prediction maps
  - Identify spatial clusters of errors
  - Check for edge effects
  - Analyze per-scene performance

- **Class-Specific Deep Dive:**
  - Spectral signatures of confused classes
  - t-SNE visualization of embeddings
  - Sample difficult examples
  - Cross-reference with land cover definitions

- **Model Comparison:**
  - Compare baseline with pretrained model
  - Ensemble predictions
  - Compare different training runs
  - Ablation studies (remove augmentation, etc.)

- **Statistical Testing:**
  - Confidence intervals for metrics
  - McNemar's test for model comparison
  - Bootstrap resampling
  - Cross-validation consistency

- **Interactive Dashboard:**
  - Build Plotly/Streamlit dashboard
  - Interactive confusion matrix
  - Filter by confidence score
  - Explore predictions interactively

## ✂️ If Running Out of Time
**Priority 1 (Must Complete - 75 min):**
- Load model and predict (15 min)
- Calculate basic metrics (15 min)
- Create confusion matrix (15 min)
- Show sample predictions (15 min)
- Quick discussion (15 min)

**Can Skip:**
- Detailed per-class analysis (show summary only)
- Advanced metrics (ROC, PR curves)
- Spatial analysis
- Extensive error analysis

**Can Do Asynchronously:**
- Detailed report writing
- Advanced visualizations
- Statistical testing
- Model comparison

**Minimal Viable Lab (90 min):**
- Quick prediction (10 min)
- Calculate accuracy + F1 (10 min)
- Confusion matrix heatmap (15 min)
- Show 5-10 examples (10 min)
- Brief discussion (10 min)
- (45 min saved by skipping deep dives)

**Backup Plan:**
- If model not trained: Use provided pre-trained model
- If predictions fail: Use pre-computed predictions
- Focus on interpretation of given results
