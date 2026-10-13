import httpx
from fastapi import HTTPException

from app.config import settings


class UserClient:
    def get_user(self, user_id: int) -> dict:
        try:
            response = httpx.get(f"{settings.user_service_url}/users/{user_id}", timeout=5)
        except httpx.RequestError:
            raise HTTPException(status_code=503, detail="User service is unavailable")

        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="User not found")
        if response.status_code != 200:
            raise HTTPException(status_code=502, detail="Unexpected response from user service")
        return response.json()
