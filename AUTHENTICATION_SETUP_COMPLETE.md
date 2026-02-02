# Authentication Setup Complete ✓

## Summary

You've successfully obtained OAuth2 credentials for Copernicus Dataspace. Here's what you need to do:

### Your Credentials
```
Client ID:     sh-a3f6b18d-a6d3-4553-9fd6-7e5a0d61e68a
Client Secret: SXnymm9WABkAQTDPVgrgsqgKIreKJSQ9
```

⚠️ **IMPORTANT**: Never commit these to Git or public repositories!

---

## Quick Setup (5 minutes)

### 1. Add to Environment (Recommended)

**Copy-paste into your terminal:**

```bash
# Set environment variables
export COPERNICUS_CLIENT_ID="sh-a3f6b18d-a6d3-4553-9fd6-7e5a0d61e68a"
export COPERNICUS_CLIENT_SECRET="SXnymm9WABkAQTDPVgrgsqgKIreKJSQ9"

# Verify they're set
echo "Client ID: $COPERNICUS_CLIENT_ID"
echo "Secret: ${COPERNICUS_CLIENT_SECRET:0:10}..."
```

### 2. Make it Permanent (HPC)

Add these lines to `~/.bashrc`:

```bash
# Copernicus Dataspace Credentials
export COPERNICUS_CLIENT_ID="sh-a3f6b18d-a6d3-4553-9fd6-7e5a0d61e68a"
export COPERNICUS_CLIENT_SECRET="SXnymm9WABkAQTDPVgrgsqgKIreKJSQ9"
```

Then:
```bash
source ~/.bashrc
```

### 3. Test Authentication

```bash
cd /home/samy/Documents/iceland-course/notebooks/iceland-ml/
python3 test_copernicus_auth.py
```

**Expected output**: ✓ All checks passed!

---

## How Authentication Works

### OAuth2 Client Credentials Flow

```
Your Notebook
    ↓
Sends: Client ID + Secret
    ↓
Copernicus Authentication Server
    ↓
Returns: Access Token (valid for 1 hour)
    ↓
Use Token for API Requests
```

### Token Lifecycle

- **Requested**: When you run `get_access_token()`
- **Valid for**: 3600 seconds (1 hour)
- **Cached**: Automatically reused until expiration
- **Expired?**: Automatically request a new one

---

## Using in Lab 3.1

Lab 3.1 automatically handles authentication:

```python
# Lab 3.1 does this:
client_id = os.getenv('COPERNICUS_CLIENT_ID')
client_secret = os.getenv('COPERNICUS_CLIENT_SECRET')

token = get_access_token(client_id, client_secret)
headers = {"Authorization": f"Bearer {token}"}

# Now use headers in API requests
response = requests.get(url, headers=headers)
```

---

## Common Tasks

### Search for Sentinel-2 Products

```python
params = {
    "$filter": "Collection/Name eq 'SENTINEL-2' and ...",
    "$top": 100
}
response = requests.get(SEARCH_URL, params=params, headers=headers)
```

### Download Products

```python
download_url = f"https://zipper.dataspace.copernicus.eu/odata/v1/Products({product_id})/$value"
response = requests.get(download_url, headers=headers, stream=True)
```

---

## File Reference

You have 3 helper files:

1. **`COPERNICUS_QUICK_START.md`** (this file)
   - Quick reference and setup instructions

2. **`COPERNICUS_SETUP.md`**
   - Detailed authentication guide
   - Troubleshooting tips
   - Best practices

3. **`test_copernicus_auth.py`**
   - Standalone test script
   - Verifies your credentials work

4. **`copernicus_auth.py`** (optional utility)
   - Reusable authentication module
   - Token caching and management

---

## Running Lab 3.1

Once authentication is set up:

```bash
# Start Jupyter
jupyter notebook

# Open: lab3_1_gee_data_download.ipynb
# The notebook will automatically use your credentials
```

---

## What If It Doesn't Work?

### "401 Unauthorized"
```bash
# Check your credentials are set
echo $COPERNICUS_CLIENT_ID
echo $COPERNICUS_CLIENT_SECRET

# Verify they match what you copied
# Note: Secret should NOT be truncated
```

### "429 Too Many Requests"
- You're requesting tokens too frequently
- Tokens are cached - they should be reused
- Slow down API requests

### "Connection Timeout"
- Check internet connection
- Copernicus servers might be down
- Try again in a few minutes

---

## Best Practices

✓ Store credentials in environment variables  
✓ Never hardcode credentials  
✓ Don't commit credentials to Git  
✓ Rotate credentials periodically  
✓ Use `.gitignore` to protect any `.env` files  
✓ Test with `test_copernicus_auth.py` before running Lab 3.1  

---

## Next Steps

1. ✓ Set environment variables (done)
2. ✓ Verify with test script (do this now)
3. Run Lab 3.1 to download Sentinel-2 data
4. Run Lab 3.2 to preprocess and extract patches
5. Train models in Lab 4+

---

## References

- **Copernicus Dataspace**: https://dataspace.copernicus.eu/
- **Documentation**: https://documentation.dataspace.copernicus.eu/APIs.html
- **OAuth2 Standard**: https://tools.ietf.org/html/rfc6749
- **JWT Tokens**: https://jwt.io/

---

**Setup Date**: February 2, 2026  
**Last Updated**: February 2, 2026
