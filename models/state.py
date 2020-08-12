#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Colum
from sqlalchemy import String
from sqlalchemy import ForeignKey
from os import getenv


class State(BaseModel, Base):
    """ State class """

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Colum(
            String(128),
            nullable=False
        )
    else:
        name = ''
