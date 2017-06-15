from database.database_setup import Base
from sqlalchemy import Column, Integer, String, DateTime, Date
from sqlalchemy.orm import relationship
import datetime


class User(Base):
    """
    Represents user entity on database
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    email = Column(String(30), nullable=False)

    created_at = Column(DateTime, nullable=False,
                        default=datetime.datetime.now())

    games = relationship('Game', cascade="save-update, merge, delete")