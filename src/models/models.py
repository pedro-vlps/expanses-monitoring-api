"""Models for the API application."""

# pylint: disable=too-few-public-methods

import datetime
import decimal
import uuid
from typing import Optional

from sqlalchemy import (
    Date,
    DateTime,
    ForeignKeyConstraint,
    Numeric,
    PrimaryKeyConstraint,
    Text,
    UniqueConstraint,
    Uuid,
    text,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    """Base class for all models."""


class Users(Base):
    """Model representing a user in the system."""
    __tablename__ = "users"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="users_pkey"),
        UniqueConstraint("email", name="users_email_key"),
        UniqueConstraint("name", name="users_name_key"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid, primary_key=True, server_default=text("gen_random_uuid()")
    )
    name: Mapped[str] = mapped_column(Text, nullable=False)
    email: Mapped[str] = mapped_column(Text, nullable=False)
    password_hash: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    custom_expenses_groups: Mapped[list["CustomExpensesGroups"]] = relationship(
        "CustomExpensesGroups", back_populates="user"
    )
    expenses: Mapped[list["Expenses"]] = relationship("Expenses", back_populates="user")


class CustomExpensesGroups(Base):
    """Model representing a custom expense group for a user."""
    __tablename__ = "custom_expenses_groups"
    __table_args__ = (
        ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            ondelete="CASCADE",
            name="custom_expenses_groups_user_id_fkey",
        ),
        PrimaryKeyConstraint("id", name="custom_expenses_groups_pkey"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid, primary_key=True, server_default=text("gen_random_uuid()")
    )
    user_id: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)
    name: Mapped[str] = mapped_column(Text, nullable=False)

    user: Mapped["Users"] = relationship(
        "Users", back_populates="custom_expenses_groups"
    )


class Expenses(Base):
    """Model representing an expense entry for a user."""
    __tablename__ = "expenses"
    __table_args__ = (
        ForeignKeyConstraint(
            ["user_id"], ["users.id"], ondelete="CASCADE", name="expenses_user_id_fkey"
        ),
        PrimaryKeyConstraint("id", name="expenses_pkey"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid, primary_key=True, server_default=text("gen_random_uuid()")
    )
    user_id: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)
    amount: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    category: Mapped[Optional[str]] = mapped_column(Text)
    description: Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    user: Mapped["Users"] = relationship("Users", back_populates="expenses")
