#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from os import getenv
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(
            String(128),
            nullable=False
        )
        state_id = Column(
            String(60),
            ForeignKey('states.id'),
            nullable=False
        )
    else:
        name = ''
        state_id = ''

    def __init__(self, *args, **kwargs):
        """ initializes obj city """
        super().__init__(*args, **kwargs)
