from fastapi import HTTPException
from sqlalchemy import select

from src.models.models import Users

class AuthService:
    @staticmethod
    async def login(email: str, password: str, db):
        async with db as session:
            query = select(
                Users
            )

            result = await session.execute(query)
            users = result.scalars().all()

            for user in users:
                if user.email == email and user.password == password:
                    return user

            raise HTTPException(status_code=401, detail="Invalid email or password")
