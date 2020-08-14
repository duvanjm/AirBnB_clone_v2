#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, String, Float, ForeignKey


if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column(
            'place_id',
            String(60),
            ForeignKey(
                'places.id',
                onupdate='CASCADE',
                ondelete='CASCADE'),
            primary_key=True
        ),
        Column(
            'amenity_id',
            String(60),
            ForeignKey(
                'amenities.id',
                onupdate='CASCADE',
                ondelete='CASCADE'),
            primary_key=True
        )
    )


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(
            String(60),
            ForeignKey('cities.id'),
            nullable=False
        )
        user_id = Column(
            String(60),
            ForeignKey('users.id'),
            nullable=False
        )
        name = Column(
            String(128),
            nullable=False
        )
        description = Column(String(1024))
        number_rooms = Column(
            Integer,
            nullable=False,
            default=0
        )
        number_bathrooms = Column(
            Integer,
            nullable=False,
            default=0
        )
        max_guest = Column(
            Integer,
            nullable=False,
            default=0
        )
        price_by_night = Column(
            Integer,
            nullable=False,
            default=0
        )
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship('Review', backref='place')
        amenities = relationship(
            'Amenity', secondary='place_amenity',
            backref='place_amenities', viewonly=False
        )

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    """ @property
    def reviews(self):
        """Method getter setter for return Cities
        instance of current state_id"""
        reviews = []
        objs = models.storage.all(models.review.Review)
        for val in objs:
            if objs[key].place_id is self.id:
                cities.append(objs[key])
        return reviews """

    def __init__(self, *args, **kwargs):
        """ initializes obj place """
        super().__init__(*args, **kwargs)
