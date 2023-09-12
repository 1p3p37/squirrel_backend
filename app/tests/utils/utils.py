import random
import string
from typing import Dict

from fastapi.testclient import TestClient

from app.core.config import settings

def random_lower_string() -> str:
    """
    Generate a random lowercase string of length 32.
    """
    return "".join(random.choices(string.ascii_lowercase, k=32))

def random_email() -> str:
    """
    Generate a random email-like string.
    """
    return f"{random_lower_string()}@{random_lower_string()}.com"

async def get_superuser_token_headers(client: TestClient) -> Dict[str, str]:
    """
    Get superuser token headers by making an async request to the authentication endpoint.

    Args:
        client (TestClient): The FastAPI test client.

    Returns:
        Dict[str, str]: A dictionary containing the authorization headers.
    """
    login_data = {
        "username": settings.FIRST_SUPERUSER,
        "password": settings.FIRST_SUPERUSER_PASSWORD,
    }
    r = await client.post(f"{settings.api_key}/login/access-token", data=login_data)
    tokens = r.json()
    a_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {a_token}"}
    return headers
