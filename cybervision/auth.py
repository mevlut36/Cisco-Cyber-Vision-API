
from .config import AUTH_TOKEN

def get_headers():
    """Required headers for auth"""
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AUTH_TOKEN}"
    }
