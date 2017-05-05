from database.database_setup import Base

from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import  relationship

from model.game import Game


class GameCharacter(Base):
    __tablename__ = "game_character"

    id = Column(Integer, primary_key=True)

    id_game = Column(ForeignKey("game.id"))

    name = Column(String(100), nullable=False)

    created_at = Column(DateTime, nullable=False)

    updated_at = Column(DateTime, nullable=True)

    game = relationship(Game)
