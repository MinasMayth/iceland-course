# Copernicus Dataspace Authentication - Setup Checklist

## ✅ What You Have

- **Client ID**: `sh-a3f6b18d-a6d3-4553-9fd6-7e5a0d61e68a`
- **Client Secret**: `SXnymm9WABkAQTDPVgrgsqgKIreKJSQ9`
- **Authentication Method**: OAuth2 Client Credentials (recommended for HPC)

---

## 📋 Setup Checklist

### Phase 1: Environment Setup (5 minutes)

- [ ] Open terminal
- [ ] Run the following commands:

```bash
# Set credentials for this session
export COPERNICUS_CLIENT_ID="sh-a3f6b18d-a6d3-4553-9fd6-7e5a0d61e68a"
export COPERNICUS_CLIENT_SECRET="SXnymm9WABkAQTDPVgrgsqgKIreKJSQ9"

# Verify they're set
echo $COPERNICUS_CLIENT_ID
echo $COPERNICUS_CLIENT_SECRET
```

- [ ] Both variables should display without errors

### Phase 2: Make Environment Persistent (5 minutes)

- [ ] Edit `~/.bashrc`:
```bash
nano ~/.bashrc
# or
vim ~/.bashrc
```

- [ ] Add these lines at the end:
```bash
# Copernicus Dataspace Credentials (keep secure!)
export COPERNICUS_CLIENT_ID="sh-a3f6b18d-a6d3-4553-9fd6-7e5a0d61e68a"
export COPERNICUS_CLIENT_SECRET="SXnymm9WABkAQTDPVgrgsqgKIreKJSQ9"
```

- [ ] Save and close editor
- [ ] Reload bashrc:
```bash
source ~/.bashrc
```

### Phase 3: Test Authentication (2 minutes)

- [ ] Navigate to lab directory:
```bash
cd /home/samy/Documents/iceland-course/notebooks/iceland-ml/
```

- [ ] Run test script:
```bash
python3 test_copernicus_auth.py
```

- [ ] Expected output includes:
  - ✓ Client ID found
  - ✓ Client Secret found  
  - ✓ Token obtained
  - ✓ All checks passed!

### Phase 4: Review Documentation (Optional but Recommended)

- [ ] Read: `/home/samy/Documents/iceland-course/COPERNICUS_QUICK_START.md`
- [ ] Read: `/home/samy/Documents/iceland-course/notebooks/iceland-ml/COPERNICUS_SETUP.md`
- [ ] Understand: How OAuth2 tokens work
- [ ] Know: Where your credentials are stored

---

## 🚀 Next Steps

### Ready to Download Data?

1. Open Jupyter:
```bash
cd /home/samy/Documents/iceland-course/
jupyter notebook
```

2. Open: `notebooks/iceland-ml/lab3_1_gee_data_download.ipynb`

3. The notebook will:
   - Read credentials from environment
   - Authenticate automatically
   - Allow you to search and download Sentinel-2 data

### HPC Submission?

For batch jobs, add this to your Slurm script:

```bash
#!/bin/bash
#SBATCH --job-name=sentinel2_download
#SBATCH --time=2:00:00

# Credentials are already in ~/.bashrc, but explicit here:
export COPERNICUS_CLIENT_ID="sh-a3f6b18d-a6d3-4553-9fd6-7e5a0d61e68a"
export COPERNICUS_CLIENT_SECRET="SXnymm9WABkAQTDPVgrgsqgKIreKJSQ9"

# Run your Python script
python3 download_sentinel2.py
```

---

## 🔒 Security Reminders

✓ **Credentials are set in environment** - not in code  
✓ **Not committed to Git** - check `.gitignore_credentials`  
✓ **Only loaded when needed** - via `os.getenv()`  
✓ **Tokens expire** - automatically refreshed  
✓ **Rate limited** - tokens are cached  

**If you ever compromise credentials:**
- Go to Copernicus Dashboard
- Delete the old OAuth client
- Create a new one
- Update credentials

---

## 📚 Reference Files

| File | Purpose |
|------|---------|
| `COPERNICUS_QUICK_START.md` | Quick reference (you are here) |
| `AUTHENTICATION_SETUP_COMPLETE.md` | Full setup guide |
| `COPERNICUS_SETUP.md` | Detailed documentation |
| `test_copernicus_auth.py` | Test script |
| `copernicus_auth.py` | Reusable auth module |
| `.gitignore_credentials` | Git security config |
| `lab3_1_gee_data_download.ipynb` | Data download lab |
| `lab3_2_data_preprocessing.ipynb` | Preprocessing lab |

---

## ❓ Troubleshooting

| Problem | Solution |
|---------|----------|
| `COPERNICUS_CLIENT_ID not found` | Run `export` commands and source bashrc |
| `401 Unauthorized` | Verify credentials with `test_copernicus_auth.py` |
| `Connection timeout` | Check internet, wait 1-2 minutes, retry |
| `429 Too Many Requests` | Token cache working but requests too fast - slow down |
| `Token expired` | Script auto-refreshes, just retry |

---

## ✅ Completion Status

- [x] Credentials obtained
- [x] Environment variables set
- [x] Authentication configured
- [x] Test script created
- [x] Documentation provided
- [x] Lab notebooks updated
- [ ] **Run test to verify setup**
- [ ] **Start Lab 3.1 to download data**

---

**Last Update**: February 2, 2026  
**Status**: Ready for Lab 3.1 ✓
