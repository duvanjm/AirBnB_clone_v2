#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(
            String(128),
            nullable=False
        )
    else:
        name = ''

    @property
    def cities(self):
        """return the list of City objects
        from storage linked to the current State"""
        list_ = []
        sta = models.storage.all(City)
        for k, v in sta:
            if v.state_id == self.id:
                list_.append(v)
        return list_
