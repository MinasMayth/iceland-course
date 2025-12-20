# Instructor Notes

## Roles
- Gabriele: course lead, context, and HPC access (JUDOOR).
- Rocco: technical lead (data, TerraTorch, fine‑tuning, troubleshooting).
- Stefano: consult existing material and slides; align narrative.
- **Samy: Lab instructor for 6 hands-on sessions (40 min each, online)**

## Timeline
- Jan (wk 2): Lesson 1 + environment checks and AOI/data prep.
- Feb: Lesson 2 (fine‑tuning) + async practice.
- Mar: Lesson 3 (inference/benchmark) + project wrap‑up.
- Apr (mid): submissions, optional presentations.

**Lab Schedule (Samy's sessions):**
- Week 1: Lab 1 - Judoor & HPC Access
- Week 3: Lab 2 - Jupyter-JSC & Git
- Week 6: Lab 3 - GEE & Sentinel-2 Acquisition
- Week 8: Lab 4 - Data Preprocessing & Patches
- Week 11: Lab 5.1 - Baseline Model Training
- Week 12: Lab 5.2 - Model Evaluation Metrics

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

## 📋 Session Structure (40 min)
- **5 min:** Recap + objectives
- **25 min:** Live demo + student coding (interactive)
- **5 min:** Hands-on exercise
- **5 min:** Q&A + next lab preview

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

**Demo:** SSH key generation → login → directory creation

**Common Issues:**
- Permission denied → Check SSH key in Judoor
- Can't join project → Verify Judoor login first

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

### Lab 4: Preprocessing & Patches
**Pre-Lab:**
- Verify students have downloaded scenes
- Prepare synthetic data as backup

**Key Points:**
- Why patches? Fixed-size inputs for CNNs
- Normalization: better training
- Train/val/test: prevent overfitting

**Demo:** Load GeoTIFF → extract patches → normalize → show before/after stats

**Common Issues:**
- Memory error → process one scene at a time
- All patches rejected → lower threshold

### Lab 5.1: Model Training
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

### Lab 5.2: Model Evaluation
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
- Lab 4: Smaller patches (128), fewer samples
- Lab 5.1: Train 5 epochs, submit rest as batch
- Lab 5.2: Focus on confusion matrix

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

---

## Resources Created

All lab materials are in `/notebooks/iceland-ml/`:
1. `lab1_judoor_hpc_access.ipynb` - HPC setup
2. `lab2_jupyter_jsc_git.ipynb` - Jupyter & Git
3. `lab3_gee_sentinel2_acquisition.ipynb` - Data acquisition
4. `lab4_preprocessing_patches.ipynb` - Preprocessing
5. `lab5.1_baseline_training.ipynb` - Model training
6. `lab5.2_model_evaluation.ipynb` - Evaluation

**Student guides:**
- `docs/iceland-ml/README.md` - Course overview
- `docs/iceland-ml/LAB_SUMMARY.md` - Quick reference

---

**Good luck with teaching! 🚀**

## Communication
- Set up Slack/Mattermost channels: #announcements, #help, #share-results.
- Office hours after each lesson.
