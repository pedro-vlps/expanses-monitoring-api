from sqlalchemy import select

from src.models import Expenses

class ExpansesService:
    """Service class for handling expanses-related operations."""
    @staticmethod
    async def get_expanses_by_user_id(user_id, db):
        """Get all expanses for a specific user."""
        async with db as session:
            query = select(Expenses).where(Expenses.user_id == user_id)

            result = await session.execute(query)
            expanses = result.scalars().all()

            return expanses
