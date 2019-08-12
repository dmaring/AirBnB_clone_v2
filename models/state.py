#!/usr/bin/python3
"""This is the state class"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import os


Base = declarative_base()

class State(Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'

    id = Column(Integer,
                unique=True,
                primary_key=True,
                autoincrement=True,
                nullable=False)

    name = Column(String(128),
                  nullable=False)

    cities = relationship("City",
                          backref="state",
                          cascade="all, delete-orphan")

    @property
    def cities():
        _list = []
        for city in self.cities:
            if city.state_id == self.id:
                _list.append(city)
        return(_list)
