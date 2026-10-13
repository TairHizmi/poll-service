from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Question(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(500), nullable=False)
    option_1: Mapped[str] = mapped_column(String(255), nullable=False)
    option_2: Mapped[str] = mapped_column(String(255), nullable=False)
    option_3: Mapped[str] = mapped_column(String(255), nullable=False)
    option_4: Mapped[str] = mapped_column(String(255), nullable=False)
