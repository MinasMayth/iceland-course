#!/usr/bin/env python3
"""
Copernicus Dataspace Authentication Utility

Usage:
    from copernicus_auth import get_token
    
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}
"""

import os
import requests
from datetime import datetime, timedelta

# Cache tokens to avoid excessive requests
_token_cache = {}


def get_token(client_id=None, client_secret=None, force_refresh=False):
    """
    Get a valid OAuth2 access token from Copernicus Dataspace.
    
    Tokens are cached and reused until expiration to avoid rate limiting.
    
    Parameters:
    -----------
    client_id : str, optional
        OAuth2 Client ID. If not provided, reads from COPERNICUS_CLIENT_ID env var
    client_secret : str, optional
        OAuth2 Client Secret. If not provided, reads from COPERNICUS_CLIENT_SECRET env var
    force_refresh : bool
        If True, request a new token even if one is cached
    
    Returns:
    --------
    str : Access token, or None if authentication failed
    
    Raises:
    -------
    ValueError : If credentials are not provided or found in environment
    """
    
    # Get credentials
    if client_id is None:
        client_id = os.getenv('COPERNICUS_CLIENT_ID')
    if client_secret is None:
        client_secret = os.getenv('COPERNICUS_CLIENT_SECRET')
    
    if not client_id or not client_secret:
        raise ValueError(
            "Credentials not found. Set environment variables:\n"
            "  export COPERNICUS_CLIENT_ID='sh-...'\n"
            "  export COPERNICUS_CLIENT_SECRET='...'"
        )
    
    # Check cache
    cache_key = client_id
    if not force_refresh and cache_key in _token_cache:
        token_info = _token_cache[cache_key]
        if datetime.now() < token_info['expires_at']:
            return token_info['token']
    
    # Request new token
    print("🔄 Requesting new access token...")
    
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }
    
    try:
        response = requests.post(
            "https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token",
            data=data,
            timeout=30
        )
        response.raise_for_status()
        
        token_data = response.json()
        access_token = token_data['access_token']
        expires_in = token_data.get('expires_in', 3600)
        
        # Cache the token
        _token_cache[cache_key] = {
            'token': access_token,
            'expires_at': datetime.now() + timedelta(seconds=expires_in - 60)  # Refresh 1 min before expiry
        }
        
        print(f"✓ Token obtained (valid for {expires_in} seconds)")
        return access_token
        
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            print("❌ Authentication failed: Invalid credentials")
            print("   - Check COPERNICUS_CLIENT_ID and COPERNICUS_CLIENT_SECRET")
            print(f"   - Client ID provided: {client_id[:15]}...")
        else:
            print(f"❌ HTTP {e.response.status_code}: {e.response.text}")
        return None
        
    except requests.exceptions.Timeout:
        print("❌ Connection timeout - check your internet connection")
        return None
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None


def get_auth_headers(client_id=None, client_secret=None):
    """
    Convenience function to get authorization headers.
    
    Returns:
    --------
    dict : Headers dict with Bearer token, or None if authentication failed
    """
    token = get_token(client_id, client_secret)
    if token:
        return {"Authorization": f"Bearer {token}"}
    return None


def verify_credentials(client_id=None, client_secret=None):
    """
    Test credentials without caching the token.
    
    Returns:
    --------
    bool : True if credentials are valid, False otherwise
    """
    try:
        token = get_token(client_id, client_secret, force_refresh=True)
        return token is not None
    except ValueError as e:
        print(f"⚠ {e}")
        return False


if __name__ == "__main__":
    # Test script
    print("Copernicus Dataspace Authentication Test\n")
    
    try:
        token = get_token()
        if token:
            print(f"\n✓ Success! Token: {token[:50]}...")
        else:
            print("\n❌ Failed to obtain token")
    except ValueError as e:
        print(f"❌ Error: {e}")
