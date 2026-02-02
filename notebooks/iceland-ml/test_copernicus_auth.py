#!/usr/bin/env python3
"""
Quick test script to verify Copernicus Dataspace authentication

Run this before starting Lab 3.1 to ensure your credentials work.

Usage:
    python3 test_copernicus_auth.py
"""

import os
import sys
import requests
from datetime import datetime


def main():
    print("=" * 60)
    print("Copernicus Dataspace Authentication Test")
    print("=" * 60)
    
    # Check environment variables
    print("\n1. Checking environment variables...")
    client_id = os.getenv('COPERNICUS_CLIENT_ID')
    client_secret = os.getenv('COPERNICUS_CLIENT_SECRET')
    
    if not client_id:
        print("   ❌ COPERNICUS_CLIENT_ID not found")
        print("   Run: export COPERNICUS_CLIENT_ID='sh-...'")
        return False
    else:
        print(f"   ✓ Client ID: {client_id[:20]}...")
    
    if not client_secret:
        print("   ❌ COPERNICUS_CLIENT_SECRET not found")
        print("   Run: export COPERNICUS_CLIENT_SECRET='...'")
        return False
    else:
        print(f"   ✓ Client Secret: {client_secret[:20]}...")
    
    # Test authentication
    print("\n2. Testing authentication...")
    
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }
    
    try:
        response = requests.post(
            "https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token",
            data=data,
            timeout=10
        )
        
        if response.status_code == 200:
            token_data = response.json()
            token = token_data['access_token']
            expires_in = token_data.get('expires_in', 3600)
            
            print(f"   ✓ Authentication successful!")
            print(f"   ✓ Token: {token[:50]}...")
            print(f"   ✓ Expires in: {expires_in // 60} minutes")
            
            # Decode token to show expiration
            import json
            import base64
            parts = token.split('.')
            payload = parts[1]
            padding = 4 - len(payload) % 4
            if padding != 4:
                payload += '=' * padding
            
            try:
                decoded = json.loads(base64.urlsafe_b64decode(payload))
                exp_timestamp = decoded.get('exp')
                if exp_timestamp:
                    exp_time = datetime.fromtimestamp(exp_timestamp)
                    print(f"   ✓ Token expires at: {exp_time}")
            except:
                pass
            
            return True
        
        elif response.status_code == 401:
            print(f"   ❌ Authentication failed (401 Unauthorized)")
            print(f"   Check your CLIENT_ID and CLIENT_SECRET")
            print(f"   Response: {response.text}")
            return False
        
        else:
            print(f"   ❌ HTTP {response.status_code}: {response.text}")
            return False
    
    except requests.exceptions.Timeout:
        print("   ❌ Connection timeout")
        print("   Check your internet connection")
        return False
    
    except requests.exceptions.ConnectionError:
        print("   ❌ Connection error")
        print("   Check your internet connection")
        return False
    
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False


if __name__ == "__main__":
    success = main()
    
    print("\n" + "=" * 60)
    if success:
        print("✓ All checks passed! You're ready to use Lab 3.1")
        print("=" * 60)
        sys.exit(0)
    else:
        print("❌ Some checks failed. See COPERNICUS_SETUP.md for help")
        print("=" * 60)
        sys.exit(1)
