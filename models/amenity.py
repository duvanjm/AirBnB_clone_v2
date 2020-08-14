#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Representation of Amenity """
    __tablename__ = 'amenities'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(
            String(128),
            nullable=False
        )
        from models.place import place_amenity
        place_amenities = relationship(
            'Place', secondary=place_amenity,
            back_populates='amenities'
        )
    else:
        name = ''

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
