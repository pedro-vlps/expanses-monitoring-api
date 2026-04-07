from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

async def set_current_user_id(session: AsyncSession, user_id: int | None) -> None:
    """Set the current user ID in the session for auditing purposes."""
    if not user_id:
        return
    
    await session.execute(
        text(f"SET SESSION app.current_user_id = '{user_id}'")
    )