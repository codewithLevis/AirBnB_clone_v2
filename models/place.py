#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey, Integer, Float
from sqlalchemy import Table
from sqlalchemy.orm import relationship
from os import environ

storage_form = environ.get('HBNB_TYPE_STORAGE', 'file')

place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column('place_id', String(60),
               ForeignKey('places.id'),
               primary_key=True),
        Column('amenity_id', String(60),
               ForeignKey('amenities.id'),
               primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    if storage_form == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True, default=0)
        longitude = Column(Float, nullable=True, default=0)
        reviews = relationship('Review',
                               backref='place',
                               cascade='all, delete-orphan')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False,
                                 backref='place_amenities')
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
            from models.__init__ import storage
            from models.review import Review
            query = storage.all(Review).values()
            return [review for review in query if review.place_id == self.id]
