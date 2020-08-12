#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from sqlalchemy import (create_engine)
from models.base_model import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models import classes
import os


class DBStorage:
    """This class manages storage of hbnb models in db"""
    __engine = None
    __session = None

    def __init__(self):
        """ create engine """
        self.__engine = create_engine(
            'mysql+mysqldb:://{}:{}@{}/{}'.format(
                os.environ['HBNB_MYSQL_USER'],
                os.environ['HBNB_MYSQL_PWD'],
                os.environ['HBNB_MYSQL_HOST'],
                os.environ['HBNB_MYSQL_DB']
            ),
            pool_pre_ping=True
        )

        if os.environ['HBNB_ENV'] == 'test':
            print("##### HBNB_ENV == test #####")
            """ Base.metadata = MetaData()
            Base.metadata.drop(self.__engine) """

    def all(self, cls=None):
        """ query on the current database session - optional, filter by cls"""
        dict_ = {}

        if cls:
            query = self.__session.query(cls).all()
            for obj in query:
                delattr(obj, '_sa_instance_state')
                dict_[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            for key, value in classes:
                query = self.__session.query(key).all()
                for obj in query:
                    delattr(obj, '_sa_instance_state')
                    dict_[obj.__class__.__name__ + '.' + obj.id] = obj
        return dict_

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """  """
        self.__session = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )()
        Session = scoped_session(self.__session)
