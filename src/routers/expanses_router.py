from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.controllers.expanses_controller import ExpansesController
from src.configs.db_connection import get_db

expanses_router = APIRouter()

@expanses_router.get("/{user_id}/user")
async def get_expanses_by_user_id(user_id, db: AsyncSession = Depends(get_db)):
    """Endpoint to get all expanses for a specific user."""
    response = await ExpansesController.get_expanses_by_user_id(user_id, db)
    return response
