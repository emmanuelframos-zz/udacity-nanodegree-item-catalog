from database.database_setup import Base

from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Date
from sqlalchemy.orm import  relationship

from model.game import Game


class GameCharacter(Base):
    __tablename__ = "game_character"

    id = Column(Integer, primary_key=True)

    id_game = Column(ForeignKey("game.id"))

    name = Column(String(100), nullable=False)

    description = Column(String, nullable=False)

    release_date = Column(Date, nullable=True)

    created_at = Column(DateTime, nullable=False)

    updated_at = Column(DateTime, nullable=True)

    game = relationship(Game)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'release_date': self.release_date
        }