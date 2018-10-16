from database_setup import Base
from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship
from user import User
import datetime


class Game(Base):
    """
    Represents game entity on database
    """
    __tablename__ = "game"

    id = Column(Integer, primary_key=True)

    id_user = Column(ForeignKey("users.id"))

    name = Column(String(100), nullable=False)

    description = Column(String, nullable=False)

    release_date = Column(Date, nullable=True)

    created_at = Column(DateTime, nullable=False,
                        default=datetime.datetime.now())

    updated_at = Column(DateTime, nullable=True)

    characters = relationship('Character',
                              cascade="save-update, merge, delete")

    user = relationship(User, lazy='subquery')

    def is_same_user(self, auth_user):
        self.user.email == auth_user

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'release_date': self.release_date.strftime("%m-%d-%Y")
        }