#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import environ
from sqlalchemy.orm import relationship

storage_form = environ.get("HBNB_STORAGE_TYPE", 'file')


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'

    if storage_form == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
