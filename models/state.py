#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Colum
from sqlalchemy import String
from sqlalchemy import ForeignKey


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Colum(
        String(128),
        nullable=False
    )
