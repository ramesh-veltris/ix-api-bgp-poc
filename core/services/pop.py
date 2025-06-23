import os
import requests
from .auth import get_auth_headers

IX_API_BASE_URL = os.getenv("IX_API_BASE_URL")

def get_pops():
    url = f"{IX_API_BASE_URL}/pops"
    headers = get_auth_headers()
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
