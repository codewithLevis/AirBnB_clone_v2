#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from os import environ
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

storage_form = environ.get('HBNB_TYPE_STORAGE', 'file')


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    if storage_form == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place',
                              backref='cities',
                              cascade='all, delete-orphan')
    else:
        state_id = ""
        name = ""
