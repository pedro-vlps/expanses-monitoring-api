from fastapi import HTTPException

from src.services.auth_service import AuthService

class AuthController:
    @staticmethod
    async def login(body, db):
        if not body.email or not body.password:
            raise HTTPException(status_code=400, detail="Email and password are required")

        user = await AuthService.login(body.email, body.password, db)
        return {"data": user}
