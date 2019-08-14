#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
import os

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id',
                             String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id',
                             String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """

    __tablename__ = 'places'

    city_id = Column(String(60),
                     ForeignKey('cities.id'),
                     nullable=False)

    user_id = Column(String(60),
                     ForeignKey('users.id'),
                     nullable=False)

    name = Column(String(128),
                  nullable=False)

    description = Column(String(1024),
                         nullable=True)

    number_rooms = Column(Integer,
                          nullable=False,
                          default=0)

    number_bathrooms = Column(Integer,
                              nullable=False,
                              default=0)

    max_guest = Column(Integer,
                       nullable=False,
                       default=0)

    price_by_night = Column(Integer,
                            nullable=False,
                            default=0)

    latitude = Column(Float,
                      nullable=True)

    longitude = Column(Float,
                       nullable=True)

    reviews = relationship("Review",
                           backref="place",
                           cascade="all, delete-orphan")

    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') == 'file':
        @property
        def amenities(self):
            """Returns the list of Amenity instances"""
            _list = []
            for obj in amenity_ids:
                if obj.id == self.id:
                    _list.append(obj)
            return _list

        @amenities.setter
        def amenities(self, obj):
            """Adds an Amenity.id to the attribute amenity_ids"""
            if type(obj).__name__ == 'Amenity':
                self.amenity_ids.append(obj)

    elif os.getenv('HBNB_TYPE_STORAGE') == 'db':
        @property
        def reviews(self):
            _list = []
            for review in self.reviews:
                if review.place_id == self.id:
                    _list.append(review)
            return(_list)

        amenities = relationship("Amenity",
                                 secondary=place_amenity)
