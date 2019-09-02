#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
import os


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'

    name = Column(String(128),
                  nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City",
                              backref="state",
                              cascade="all, delete-orphan")
        #     _list = []
        #     print ('hello')
        #     # for city in self.cities:
        #     #     if city.state_id == self.id:
        #     #         _list.append(city)
        #     return(_list)

    else:
        @property
        def cities(self):
            _list = []
            print("hello")
            for _id, city in models.storage.all('City').items():
                print(city.state_id)
                print(self.id)
                if city.state_id == self.id:
                        _list.append(city)
            return(_list)
