import os
import requests
from .auth import get_auth_headers

IX_API_BASE_URL = os.getenv("IX_API_BASE_URL")

def get_macs():
    url = f"{IX_API_BASE_URL}/macs"
    headers = get_auth_headers()
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def create_mac(payload):
    url = f"{IX_API_BASE_URL}/macs"
    headers = get_auth_headers()
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()
