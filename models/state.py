#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey
import models
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if models.storage == 'db':
        name = Column(
            String(128),
            nullable=False
        )
    else:
        name = ''

    if models.storage != 'db':
        @property
        def cities(self):
            """return the list of City objects
            from storage linked to the current State"""
            list_ = []
            sta = models.storage.all(City)

            for v in sta.values():
                if v.state_id == self.id:
                    list_.append(v)
            return list_
