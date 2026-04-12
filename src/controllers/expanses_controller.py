from src.services.expanses_service import ExpansesService


class ExpansesController:
    @staticmethod
    async def get_expanses_by_user_id(user_id, db):
        """Controller method to get all expanses for a specific user."""

        expanses = await ExpansesService.get_expanses_by_user_id(user_id, db)
        return expanses
