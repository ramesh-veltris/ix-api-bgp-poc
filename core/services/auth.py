import os
import requests

IX_API_BASE_URL = os.getenv("IX_API_BASE_URL")
API_KEY = os.getenv("IX_API_KEY")
API_SECRET = os.getenv("IX_API_SECRET")

def get_access_token():
    url = f"{IX_API_BASE_URL}/auth/token"
    payload = {"api_key": API_KEY, "api_secret": API_SECRET}
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()["access_token"]

def get_auth_headers():
    token = get_access_token()
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
