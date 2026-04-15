from fastapi import APIRouter

from src.controllers.ai_controller import AIController

ai_router = APIRouter()

@ai_router.post("/process-expenses")
async def process_expenses():
    response = await AIController.process_expense_data()
    return response
