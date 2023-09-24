#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, orm
from os import environ
from models.city import City

storage_form = environ.get('HBNB_TYPE_STORAGE', 'file')


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if storage_form == 'db':
        name = Column(String(128), nullable=False)
        cities = orm.relationship('City',
                                  cascade='all, delete-orphan',
                                  backref='state')
    else:   
        name = ""

        @property
        def cities(self):
            """
            Retrive cities related to a state
            """
            from models import storage
            storage.reload()
            cities_dict = storage.all(City)
            cities = cities_dict.values()
            return [city for city in cities if city.state_id == self.id]
