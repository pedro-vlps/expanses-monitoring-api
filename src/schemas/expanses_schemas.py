"""Schemas for expense payloads and API responses."""

import uuid
import decimal
import datetime
from typing import Optional

from pydantic import BaseModel


class ExpenseBase(BaseModel):
    """Base schema for expense creation and shared expense fields."""
    user_id: uuid.UUID
    amount: decimal.Decimal
    category: Optional[str] = None
    description: Optional[str] = None
    date: datetime.date


class ExpensePost(ExpenseBase):
    """Schema used when creating a new expense."""
    class Config:
        """Configure Pydantic to allow population from ORM objects and provide an example."""
        from_attributes = True
        json_schema_extra = {
            "example": {
                "user_id": "123e4567-e89b-12d3-a456-426614174000",
                "amount": "99.99",
                "category": "Travel",
                "description": "Flight to NYC",
                "date": "2024-06-01",
            }
        }


class ExpenseUpdate(BaseModel):
    """Schema used when updating an existing expense with optional fields."""
    user_id: Optional[uuid.UUID] = None
    amount: Optional[decimal.Decimal] = None
    category: Optional[str] = None
    description: Optional[str] = None
    date: Optional[datetime.date] = None

    class Config:
        """Configure Pydantic to allow population from ORM objects and provide an example."""
        from_attributes = True
        json_schema_extra = {
            "example": {
                "user_id": "123e4567-e89b-12d3-a456-426614174000",
                "amount": "99.99",
                "category": "Travel",
                "description": "Flight to NYC",
                "date": "2024-06-01",
            }
        }


class ExpenseGet(ExpenseBase):
    """Schema used when returning an expense record from the API."""
    id: uuid.UUID
    created_at: Optional[datetime.datetime] = None

    class Config:
        """Configure Pydantic to allow population from ORM objects and provide an example."""
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "user_id": "123e4567-e89b-12d3-a456-426614174000",
                "amount": "99.99",
                "category": "Travel",
                "description": "Flight to NYC",
                "date": "2024-06-01",
            }
        }

