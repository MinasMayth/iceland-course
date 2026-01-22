# Instructor Notes

## Roles
- Gabriele: course lead, context, and HPC access (JUDOOR).
- Rocco: technical lead (data, TerraTorch, fine‑tuning, troubleshooting).
- Stefano: consult existing material and slides; align narrative.
- **Samy: Lab instructor for 8 hands-on sessions (120 min each)**

## Timeline
- Jan (wk 2): Lesson 1 + environment checks and AOI/data prep.
- Feb: Lesson 2 (fine‑tuning) + async practice.
- Mar: Lesson 3 (inference/benchmark) + project wrap‑up.
- Apr (mid): submissions, optional presentations.

**Lab Schedule (Samy's sessions – 120 min each):**
- Lab 1: Judoor & HPC Access
- Lab 2: Jupyter-JSC & Git
- Lab 3: GEE & Sentinel-2 Acquisition
- Lab 4: Data Preprocessing
- Lab 5: Patch Extraction & Dataset Prep
- Lab 6: Baseline Model Training
- Lab 7: Model Evaluation & Error Analysis
- Lab 8: Fine‑tuning & Benchmarking Wrap‑Up

## Cohort & Modality
- 5–20 students; elective → higher engagement.
- In-person preferred; for virtual, shorten lectures, add checkpoints and recorded demos; maintain active Slack/Mattermost for support.

## Environments
- Pin critical libs; provide a `requirements.txt` and a lockfile (e.g., `uv.lock`).
- Test on JupyterLab; for heavy runs, offer HPC/JSC job templates.
- Provide a fallback dataset to bypass downloads when APIs are flaky.

## Assessment
- Milestones: data prepared (L1), FT checkpoint + notes (L2), inference map + comparison (L3).
- Encourage reflection on model limits, class confusion, and AOI bias.

## Benchmarking
- Provide a reference prediction on a fixed AOI with reported metrics.
- Students compare maps and metrics; discuss reasons for gaps.

---

# Lab Teaching Guide (Samy)

## 📋 Session Structure (120 min)
- **10 min:** Recap + objectives + success criteria
- **35 min:** Guided demo (live, step-by-step)
- **45 min:** Hands-on build (students implement with checkpoints)
- **20 min:** Exercise/mini‑challenge + wrap artifacts
- **10 min:** Q&A + next lab preview + take‑home tasks

## 🎯 Teaching Philosophy
- **80% hands-on, 20% lecture** - Learn by doing
- **Fail forward** - Errors are learning opportunities
- **Real-world focus** - Every lab produces tangible output
- **Record sessions** - Students can review at their own pace

## 🗓️ Lab-by-Lab Notes

### Lab 1: Judoor & HPC Access
**Pre-Lab (1 week before):**
- Send Judoor registration link
- Share training2600 project join link
- Remind: Use university email

**Key Points:**
- Why HPC? (scale, GPU, storage)
- SSH keys: public vs private
- Filesystem: home/project/scratch

**Usage Guidelines & Compute Budget (say this explicitly):**
- Do not submit unlimited jobs or run unrelated workloads (e.g., crypto/bitcoin).
- Activity is auditable: what runs and when can be monitored.
- Compute budget is shared across users; be considerate and coordinate heavy runs.
- Prefer small, bounded test jobs first; scale up after validation.
- Clean up large files; use scratch appropriately.

**Demo:** SSH key generation → login → directory creation

**Common Issues:**
- Permission denied → Check SSH key in Judoor
- Can't join project → Verify Judoor login first

**Instructor Notes (add more here):**
- We should explain that once they have access, they must not submit jobs without limits or run prohibited workloads (e.g., crypto/bitcoin). Provide clear guardrails and consequences.
- Emphasize we can monitor execution and see resource usage to help, not to police—yet misuse affects others.
- Discuss shared compute budget and fairness; encourage scheduling etiquette and using appropriate partitions.
- [Add your notes…]

### Lab 2: Jupyter-JSC & Git
**Pre-Lab:**
- Verify all students have SSH access
- Test Jupyter-JSC availability

**Key Points:**
- Jupyter-JSC vs local (no data transfer!)
- Git basics: clone, pull, commit, push
- Virtual environments: isolate dependencies

**Demo:** Launch Jupyter → create venv → register kernel → Git workflow

**Common Issues:**
- Wrong kernel selected → import errors
- Git push without commit → explain staging

**Instructor Notes (add more here):**
- [Add your notes…]

### Lab 3: GEE & Sentinel-2
**Pre-Lab (1 week before!):**
- Reminder: Apply for GEE account (takes 2 days)
- Have backup scenes ready

**Key Points:**
- GEE power: server-side processing
- Sentinel-2 bands: spectral signatures
- Cloud filtering: why 20%?

**Demo:** Authenticate GEE → define AOI → query scenes → visualize RGB vs false color

**Common Issues:**
- GEE auth popup blocked → allow popups
- No scenes found → relax cloud cover, expand dates

**Instructor Notes (add more here):**
- [Add your notes…]

### Lab 4: Preprocessing
**Pre-Lab:**
- Verify students have downloaded scenes
- Prepare synthetic data as backup

**Key Points:**
- Why patches? Fixed-size inputs for CNNs
- Normalization: better training
- Train/val/test: prevent overfitting

**Demo:** Load GeoTIFF → normalize → show before/after stats

**Common Issues:**
- Memory error → process one scene at a time
- All patches rejected → lower threshold

**Instructor Notes (add more here):**
- [Add your notes…]

### Lab 5: Patch Extraction & Dataset Prep
**Pre-Lab:**
- Confirm disk space and I/O limits
- Provide sample AOI to standardize patching

**Key Points:**
- Patch tiling strategy (stride, overlap)
- Filtering rules and thresholds
- Dataset manifest and reproducibility

**Demo:** Extract patches → filter by QC → assemble dataset splits

**Common Issues:**
- Too few patches → adjust stride/thresholds
- Class leakage → re-check split logic

**Instructor Notes (add more here):**
- [Add your notes…]

### Lab 6: Baseline Model Training
**Pre-Lab:**
- Test GPU partition availability
- Review PyTorch on JURECA

**Key Points:**
- CNN architecture walkthrough
- Loss functions & optimizers
- Early stopping to prevent overfitting

**Demo:** Build model → count parameters → train 2-3 epochs live → show progress

**Common Issues:**
- Out of memory → reduce batch size
- NaN loss → lower learning rate

**Instructor Notes (add more here):**
- [Add your notes…]

### Lab 7: Model Evaluation & Error Analysis
**Pre-Lab:**
- Ensure students have trained models
- Prepare pre-trained model as backup

**Key Points:**
- Metrics beyond accuracy
- Confusion matrix interpretation
- Error analysis

**Demo:** Load model → predict → calculate metrics → visualize confusion matrix

**Discussion:**
- Why is class X harder?
- What data would help?
- How to improve?

**Instructor Notes (add more here):**
- [Add your notes…]

### Lab 8: Fine‑tuning & Benchmarking Wrap‑Up
**Pre-Lab:**
- Provide small FT-ready subset and base checkpoint
- Define target metrics for comparison

**Key Points:**
- Transfer learning choices (what to freeze)
- LR schedules and regularization
- Reproducibility and logging

**Demo:** Load base → fine‑tune for few epochs → run benchmark → compare with reference

**Common Issues:**
- Overfitting on small AOI → stronger regularization/early stopping
- Unstable metrics → fix seeds/augmentations

**Instructor Notes (add more here):**
- [Add your notes…]

---

## 🔧 Quick Troubleshooting

### HPC
- Job pending → reduce resources or wait
- Connection timeout → check JSC status page

### Software
- Import error → wrong kernel
- CUDA OOM → reduce batch size
- Pickle error → version mismatch

### Data
- NaN in data → apply masking
- All patches rejected → lower threshold
- Class imbalance → weighted loss

---

## 📊 Time Management

**If behind schedule:**
- Lab 1: Skip detailed SLURM (provide cheat sheet)
- Lab 2: Simplify Git to clone/pull only
- Lab 3: Use pre-downloaded scenes
- Lab 4–5: Smaller patches (128), fewer samples
- Lab 6: Train 2–3 epochs live; submit longer runs as batch
- Lab 7: Focus on confusion matrix + 1–2 key metrics
- Lab 8: Demo fine‑tune on a tiny subset, compare once

**If ahead:**
- Demonstrate extra features
- Compare alternatives
- Encourage experimentation

---

## 💡 Engagement Tips

- **Poll every 10 min:** Check progress
- **Code challenges:** Make it fun
- **Celebrate wins:** Positive reinforcement
- **Take breaks:** 2-min stretch every 20 min

---

## 📝 Post-Lab Checklist
- [ ] Upload recording
- [ ] Share summary in Slack
- [ ] Update FAQ with common issues
- [ ] Prepare next lab materials
- [ ] Send reminder 2 days before next lab

## 🧾 General Instructor Notes
- [Add any cross-cutting notes, decisions, or follow-ups here]

---

## Resources Created

All lab materials are in `/notebooks/iceland-ml/`:
1. `lab1_judoor_hpc_access.ipynb` - HPC setup
2. `lab2_jupyter_jsc_git.ipynb` - Jupyter & Git
3. `lab3_gee_sentinel2_acquisition.ipynb` - Data acquisition
4. `lab4.1_preprocessing.ipynb` - Preprocessing
5. `lab4.2_preprocessing_patches.ipynb` - Patch extraction
6. `lab5.1_baseline_training.ipynb` - Baseline training
7. `lab5.2_model_evaluation.ipynb` - Evaluation
8. `lab6_finetune.ipynb` - Fine‑tuning (reference)

**Student guides:**
- `docs/iceland-ml/README.md` - Course overview
- `docs/iceland-ml/LAB_SUMMARY.md` - Quick reference

---

**Good luck with teaching! 🚀**

## Communication
- Set up Slack/Mattermost channels: #announcements, #help, #share-results.
- Office hours after each lesson.
