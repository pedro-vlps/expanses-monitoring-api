# Schemas for user payloads and API responses.

import uuid
import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """Base schema for user fields used in payloads."""
    name: str
    email: EmailStr


class UserPost(UserBase):
    """Schema used when creating a new user."""
    password: str

    class Config:
        """Configure Pydantic to allow population from ORM objects and provide an example."""
        from_attributes = True
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john.doe@example.com",
                "created_at": "2024-06-01T10:00:00",
            }
        }


class UserUpdate(BaseModel):
    """Schema used when updating an existing user with optional fields."""
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

    class Config:
        """Configure Pydantic to allow population from ORM objects and provide an example."""
        from_attributes = True
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john.doe@example.com",
                "created_at": "2024-06-01T10:00:00",
            }
        }


class UserGet(UserBase):
    """Schema used when returning a user record from the API."""
    id: uuid.UUID
    created_at: Optional[datetime.datetime] = None

    class Config:
        """Configure Pydantic to allow population from ORM objects and provide an example."""
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "name": "John Doe",
                "email": "john.doe@example.com",
                "created_at": "2024-06-01T10:00:00",
            }
        }
