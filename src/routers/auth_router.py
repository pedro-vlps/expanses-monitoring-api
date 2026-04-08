from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api_crud_generate_libary.schemas.pattern_schema import PatternSchema

from src.configs.db_connection import get_db
from src.controllers.auth_controller import AuthController
from src.schemas.auth_schemas import LoginSchema
from src.schemas.users_schema import UserGet

auth_router = APIRouter()

@auth_router.post("/login", response_model=PatternSchema[UserGet])
async def login(body: LoginSchema, db: AsyncSession = Depends(get_db)):
    return await AuthController.login(body, db)
