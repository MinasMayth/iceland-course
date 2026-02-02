# Copernicus Dataspace Authentication Setup

## Quick Reference

You have two credentials:
- **Client ID**: `sh-a3f6b18d-a6d3-4553-9fd6-7e5a0d61e68a`
- **Client Secret**: `SXnymm9WABkAQTDPVgrgsqgKIreKJSQ9`

⚠️ **SECURITY WARNING**: Never commit these credentials to Git or any public repository!

---

## Setup on HPC Systems (Recommended)

### 1. Add to Your HPC Startup Script

Add to `~/.bashrc` or `~/.bash_profile`:

```bash
# Copernicus Dataspace Credentials (keep secure!)
export COPERNICUS_CLIENT_ID="sh-a3f6b18d-a6d3-4553-9fd6-7e5a0d61e68a"
export COPERNICUS_CLIENT_SECRET="SXnymm9WABkAQTDPVgrgsqgKIreKJSQ9"
```

Then reload:
```bash
source ~/.bashrc
```

### 2. Verify Setup

Test authentication:
```bash
python3 << 'EOF'
import os
import requests

client_id = os.getenv('COPERNICUS_CLIENT_ID')
client_secret = os.getenv('COPERNICUS_CLIENT_SECRET')

if not client_id or not client_secret:
    print("❌ Credentials not found in environment")
else:
    print(f"✓ Client ID found: {client_id[:10]}...")
    
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }
    
    response = requests.post(
        "https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token",
        data=data
    )
    
    if response.status_code == 200:
        print("✓ Authentication successful!")
    else:
        print(f"❌ Authentication failed: {response.status_code}")
        print(response.text)
EOF
```

---

## Setup for Jupyter Notebooks

### Option 1: Load from Environment (Recommended)

In your notebook (as done in Lab 3.1):

```python
import os
import requests

client_id = os.getenv('COPERNICUS_CLIENT_ID')
client_secret = os.getenv('COPERNICUS_CLIENT_SECRET')

if not client_id:
    print("⚠ Credentials not found. Set environment variables:")
    print("  export COPERNICUS_CLIENT_ID='sh-...'")
    print("  export COPERNICUS_CLIENT_SECRET='...'")
```

### Option 2: Temporary (Testing Only)

For quick testing in Jupyter, you can set inline (but don't save/commit):

```python
import os

os.environ['COPERNICUS_CLIENT_ID'] = 'sh-a3f6b18d-a6d3-4553-9fd6-7e5a0d61e68a'
os.environ['COPERNICUS_CLIENT_SECRET'] = 'SXnymm9WABkAQTDPVgrgsqgKIreKJSQ9'

# Now authenticate...
```

---

## Submitting HPC Jobs with Credentials

### Slurm Job Script Example

```bash
#!/bin/bash
#SBATCH --job-name=download_sentinel2
#SBATCH --time=2:00:00
#SBATCH --account=training2600

# Load modules
module load Python/3.10

# Set credentials (already in .bashrc, but explicit here)
export COPERNICUS_CLIENT_ID="sh-a3f6b18d-a6d3-4553-9fd6-7e5a0d61e68a"
export COPERNICUS_CLIENT_SECRET="SXnymm9WABkAQTDPVgrgsqgKIreKJSQ9"

# Run Python script
python3 download_script.py
```

---

## Understanding OAuth2 Tokens

When you authenticate, you receive a **JWT token** that looks like:
```
eyJhbGciOiJSUzI1NiIsInR5cC...
```

- **Lifetime**: 3600 seconds (1 hour) by default
- **Reusable**: Use the same token for multiple API requests
- **Don't refresh too often**: Token requests are rate-limited (HTTP 429 if exceeded)

### Token Claims

You can decode the token (without verification) to see its contents:

```python
import json
import base64

token = "your_token_here"
parts = token.split('.')
payload = parts[1]

# Add padding if needed
padding = 4 - len(payload) % 4
if padding != 4:
    payload += '=' * padding

decoded = json.loads(base64.urlsafe_b64decode(payload))
print(json.dumps(decoded, indent=2))
```

---

## Troubleshooting

### "401 Unauthorized" Error

**Cause**: Invalid credentials
**Solution**: 
- Check that CLIENT_ID starts with `sh-`
- Verify you copied the entire SECRET (no truncation)
- Check for extra spaces

```bash
# Verify env variables
echo $COPERNICUS_CLIENT_ID
echo $COPERNICUS_CLIENT_SECRET
```

### "429 Too Many Requests" Error

**Cause**: Requesting tokens too frequently
**Solution**:
- Reuse tokens instead of requesting new ones per request
- Wait 1 hour for token to expire naturally
- Space out requests

### Token Expired

**Symptoms**: "401 Unauthorized" on API requests
**Solution**: Automatically handled by requesting a new token:

```python
def get_fresh_token(client_id, client_secret):
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }
    response = requests.post(
        "https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token",
        data=data,
        timeout=30
    )
    return response.json()["access_token"]
```

---

## Best Practices

1. **Never hardcode credentials** in Python files
2. **Use environment variables** for all deployments
3. **Add `.env` to `.gitignore`** if using a `.env` file
4. **Rotate credentials regularly** through the Dashboard
5. **Use different clients** for different applications if possible
6. **Monitor token usage** in your Dashboard logs

---

## References

- **Copernicus Documentation**: https://documentation.dataspace.copernicus.eu/APIs.html
- **OAuth2 Spec**: https://tools.ietf.org/html/rfc6749
- **JWT Tokens**: https://jwt.io/

---

**Last Updated**: February 2026
