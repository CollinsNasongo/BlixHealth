from __future__ import annotations

from typing import Optional

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class PracticeRoleType(Base):
    __tablename__ = "practice_role_type"
    __table_args__ = {"schema": "silver"}

    practice_role_type_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True,)
    practice_role_type_name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True,)
    practice_role_type_description: Mapped[Optional[str]] = mapped_column(String(500),)