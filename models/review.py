#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import environ

storage_form = environ.get('HBNB_TYPE_STORAGE', 'file')


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'

    if storage_form == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
