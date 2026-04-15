from openai import OpenAI

client = OpenAI()

class AIService:
    @staticmethod
    async def generate_response():
        # Use the AI model to generate a response based on the prompt
        response = client.responses.create(
            model="gpt-4.1-mini",
            input="Testando a integração da API de IA com o FastAPI"
        )
        return response
