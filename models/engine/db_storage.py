#!/usr/bin/python3

"""This is the db storage class for AirBnB"""

from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

import os


class DBStorage:
    """DB Storage class"""

    __engine = None
    __session = None

    def __init__(self):
        """Constructor for DBStorage"""
        username = os.getenv('HBNB_MYSQL_USER')
        psw = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db_name = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(username, psw, host, db_name),
                                      pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()
        if os.getenv('HBNB_ENV') == 'test':
            # drop tables
            pass

    def all(self, cls=None):
        """Retrieve all objects from database"""
        _dict = {}
        if cls == None:
            objs = self.__session.query('User',
                                        'State',
                                        'City',
                                        'Amenity',
                                        'Place').all()
        else:
            objs = self.__session.query(cls).all()
        for obj in objs:
            key = obj.name + "." + str(obj.id)
            _dict[key] = obj.to_dict()
        return _dict

    def new(self, obj):
        """Add object to current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)
            self.__session.flush()

    def reload(self):
        """Creates all tables in the database"""
        username = os.getenv('HBNB_MYSQL_USER')
        psw = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db_name = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(username, psw, host, db_name),
                                      pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()
