from database.database_setup import Base
from sqlalchemy import Column, Integer, String, DateTime


class Game(Base):
    __tablename__ = "game"

    id = Column(Integer, primary_key=True)

    name = Column(String(100), nullable=False)

    description = Column(String, nullable=False)

    created_at = Column(DateTime, nullable=False)

    updated_at = Column(DateTime, nullable=True)