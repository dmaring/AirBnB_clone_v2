#!/usr/bin/python3

"""This is the db storage class for AirBnB"""

from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
# from models import storage

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

import os


class DBStorage:
    """DB Storage class"""

    __engine = None
    __session = None
    __classes = {'User': User,
                 'State': State,
                 'City': City,
                 'Place': Place,
                 'Review': Review,
                 'Amenity': Amenity}

    def __init__(self):
        """Constructor for DBStorage"""
        username = os.getenv('HBNB_MYSQL_USER')
        psw = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db_name = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(username, psw, host, db_name),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Retrieve all objects from database"""
        _dict = {}
        if cls is None:
            objs = []
            for c in self.__classes.keys():
                results = self.__session.query(self.__classes[c])
                for res in results:
                    objs.append(res)
        else:
            if type(cls) == str:
                objs = self.__session.query(self.__classes[cls]).all()
            else:
                objs = self.__session.query(cls).all()
        for obj in objs:
            key = type(obj).__name__ + "." + str(obj.id)
            _dict[key] = obj
        return _dict

    def new(self, obj):
        """Add object to current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def reset(self):
        """Reset session"""
        self.__session.close()
        Base.metadata.drop_all(self.__engine)
        self.reload()

    def close(self):
        """Method to close out, implicity calls Session.close()"""
        self.__session.close()
