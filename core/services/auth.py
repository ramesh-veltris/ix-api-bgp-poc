import os
import requests
from django.utils.timezone import now
from datetime import timedelta
from core.models.token import IXAPIToken

IX_API_BASE_URL = os.getenv("IX_API_BASE_URL")
API_KEY = os.getenv("IX_API_KEY")
API_SECRET = os.getenv("IX_API_SECRET")

def get_access_token():
    existing = IXAPIToken.objects.first()
    
    if existing and not existing.is_expired():
        return existing.access_token

    # If expired or missing, request new token
    url = f"{IX_API_BASE_URL}/auth/token"
    payload = {"api_key": API_KEY, "api_secret": API_SECRET}
    response = requests.post(url, json=payload)
    response.raise_for_status()

    data = response.json()
    access_token = data["access_token"]
    refresh_token = data["refresh_token"]
    expires_at = now() + timedelta(minutes=29)  # 30 min minus 1 buffer

    # Clear old and save new token
    IXAPIToken.objects.all().delete()
    IXAPIToken.objects.create(
        access_token=access_token,
        refresh_token=refresh_token,
        expires_at=expires_at
    )

    return access_token

def get_auth_headers():
    token = get_access_token()
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
