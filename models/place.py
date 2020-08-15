#!/usr/bin/python3
""" Imports """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, Table
from sqlalchemy import ForeignKey
from sqlalchemy import Table
from sqlalchemy.orm import relationship
from os import getenv


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

    __tablename__ = "places"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column(
            String(60),
            ForeignKey("cities.id"),
            nullable=False)

        user_id = Column(
            String(60),
            ForeignKey("users.id"),
            nullable=False)

        name = Column(
            String(128),
            nullable=False)

        description = Column(
            String(1024),
            nullable=True)

        number_rooms = Column(
            Integer,
            default=0,
            nullable=False)

        number_bathrooms = Column(
            Integer,
            default=0,
            nullable=False)

        max_guest = Column(
            Integer,
            default=0,
            nullable=False)

        price_by_night = Column(
            Integer,
            default=0,
            nullable=False)

        latitude = Column(
            Float,
            nullable=True)

        longitude = Column(
            Float,
            nullable=True)

        reviews = relationship(
            "Review",
            cascade="all, delete",
            backref="place")

        amenities = relationship(
            "Amenity",
            secondary="place_amenity",
            viewonly=False,
            back_populates="place_amenities")

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

    @property
    def reviews(self):
        """Method getter setter for return Cities
        instance of current state_id"""
        reviews = []
        objs = models.storage.all(models.review.Review)
        for val in objs:
            if objs[key].place_id is self.id:
                cities.append(objs[key])
        return reviews

    def __init__(self, *args, **kwargs):
        """ initializes obj place """
        super().__init__(*args, **kwargs)
