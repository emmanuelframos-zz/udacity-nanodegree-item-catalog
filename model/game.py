from database.database_setup import Base
from sqlalchemy import Column, Integer, String, DateTime, Date
from sqlalchemy.orm import relationship
import datetime

class Game(Base):
    __tablename__ = "game"

    id = Column(Integer, primary_key=True)

    name = Column(String(100), nullable=False)

    description = Column(String, nullable=False)

    release_date = Column(Date, nullable=True)

    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now())

    updated_at = Column(DateTime, nullable=True)

    characters = relationship("Character", cascade="save-update, merge, delete")

    @property
    def serialize(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'description' : self.description,
            'release_date' : self.release_date.strftime("%m-%d-%Y")
        }