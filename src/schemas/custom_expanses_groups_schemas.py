"""Schemas for custom expense group payloads and API responses."""

import uuid
from typing import Optional

from pydantic import BaseModel


class CustomExpensesGroupBase(BaseModel):
    """Base schema for custom expense group fields."""
    user_id: uuid.UUID
    name: str


class CustomExpensesGroupPost(CustomExpensesGroupBase):
    """Schema used when creating a new custom expense group."""
    class Config:
        """Configure Pydantic to allow population from ORM objects and provide an example."""
        from_attributes = True
        json_schema_extra = {
            "example": {
                "user_id": "123e4567-e89b-12d3-a456-426614174000",
                "name": "Travel Expenses"
            }
        }


class CustomExpensesGroupUpdate(BaseModel):
    """Schema used when updating a custom expense group with optional fields."""
    user_id: Optional[uuid.UUID] = None
    name: Optional[str] = None

    class Config:
        """Configure Pydantic to allow population from ORM objects and provide an example."""
        from_attributes = True
        json_schema_extra = {
            "example": {
                "user_id": "123e4567-e89b-12d3-a456-426614174000",
                "name": "Travel Expenses"
            }
        }


class CustomExpensesGroupGet(CustomExpensesGroupBase):
    """Schema used when returning a custom expense group from the API."""
    id: uuid.UUID

    class Config:
        """Configure Pydantic to allow population from ORM objects and provide an example."""
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "user_id": "123e4567-e89b-12d3-a456-426614174000",
                "name": "Travel Expenses"
            }
        }
