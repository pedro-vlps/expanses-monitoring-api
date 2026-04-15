from src.services.ai_service import AIService

class AIController:
    @staticmethod
    async def process_expense_data():
        # Processa os dados de despesas usando o serviço de IA
        response = await AIService.generate_response()
        return response
