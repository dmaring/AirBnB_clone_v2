#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import os
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = 'users'

    email = Column(String(128),
                   nullable=False,
                   default="")

    password = Column(String(128),
                      nullable=False,
                      default="")

    first_name = Column(String(128),
                        nullable=False,
                        default="")

    last_name =  Column(String(128),
                        nullable=False,
                        default="")
