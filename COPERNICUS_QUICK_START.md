# Copernicus Dataspace - Quick Start Guide

## Your Credentials

✓ **Client ID**: `sh-a3f6b18d-a6d3-4553-9fd6-7e5a0d61e68a`  
✓ **Client Secret**: `SXnymm9WABkAQTDPVgrgsqgKIreKJSQ9`

---

## Step 1: Set Environment Variables (HPC or Local)

Add these lines to your `~/.bashrc` or run them in your terminal:

```bash
export COPERNICUS_CLIENT_ID="sh-a3f6b18d-a6d3-4553-9fd6-7e5a0d61e68a"
export COPERNICUS_CLIENT_SECRET="SXnymm9WABkAQTDPVgrgsqgKIreKJSQ9"
```

Then reload:
```bash
source ~/.bashrc
```

---

## Step 2: Verify Your Setup

Run the test script:

```bash
cd /home/samy/Documents/iceland-course/notebooks/iceland-ml/
python3 test_copernicus_auth.py
```

**Expected output**:
```
✓ Authentication successful!
✓ Token obtained (valid for 60 minutes)
✓ All checks passed! You're ready to use Lab 3.1
```

---

## Step 3: Use in Lab 3.1

When you run Lab 3.1, the notebook will automatically:

1. Read credentials from environment variables
2. Request an OAuth2 token
3. Use token to search and download Sentinel-2 data

**In the notebook:**
```python
import os

client_id = os.getenv('COPERNICUS_CLIENT_ID')
client_secret = os.getenv('COPERNICUS_CLIENT_SECRET')

# Authenticate...
token = get_access_token(client_id, client_secret)
```

---

## Optional: Use Authentication Utility

You can import the authentication module in your own scripts:

```python
from copernicus_auth import get_token, get_auth_headers

# Get token
token = get_token()

# Or get headers directly
headers = get_auth_headers()

# Use in requests
import requests
response = requests.get(url, headers=headers)
```

---

## What's Next?

- Run Lab 3.1 to download Sentinel-2 data
- Use Lab 3.2 to preprocess and extract patches
- Train models in Lab 4+

---

## Troubleshooting

**"401 Unauthorized"?**
- Check credentials are set: `echo $COPERNICUS_CLIENT_ID`
- Run the test script: `python3 test_copernicus_auth.py`

**Still having issues?**
- See `COPERNICUS_SETUP.md` for detailed instructions
- Check token hasn't expired (max 1 hour)

---

For complete documentation, see:
- [COPERNICUS_SETUP.md](./COPERNICUS_SETUP.md) - Detailed setup guide
- Lab 3.1 Notebook - Full authentication walkthrough
