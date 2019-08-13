#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.org import relationship


association_table = Table('association', Base.metadata,
        Column(),
        Column()
        )


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """

    __tablename__ = "amenities"

    name = Column(String(128),
                  nullable=False)

    place_amenities = 
