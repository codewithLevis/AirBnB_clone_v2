#!/usr/bin/python3
"""
DBStorage engine
"""
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from os import getenv
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = [User, State, City, Amenity, Place, Review]


class DBStorage:
    """
    class for connection with MySQL Database
    """
    __engine = None
    __session = None

    def __init__(self):
        uname = getenv("HBNB_MYSQL_USER")
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        uri = f'mysql+mysqldb://{uname}:{password}@{host}/{db}'
        self.__engine = create_engine(uri, pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        dictionary = {}
        if cls:
            objects_list = self.__session.query(cls).all()
            for obj in objects_list:
                key = f'{cls.__name__}.{obj.id}'
                dictionary.update({key: obj})
        else:
            for cls in classes:
                objects_list = self.__session.query(cls).all()
                for obj in objects_list:
                    key = f'{cls.__name__}.{obj.id}'
                    dictionary.update({key: obj})

        return dictionary

    def new(self, obj):
        '''
        add the object to the current database session
        '''
        self.__session.add(obj)

    def save(self):
        '''
        commit all changes of the current database session
        '''
        self.__session.commit()

    def delete(self, obj=None):
        '''
        delete from the current database session obj if not None
        '''
        from sqlalchemy.orm.exc import ObjectDeletedError
        if obj:
            try:
                self.__session.delete(obj)
            except ObjectDeletedError:
                pass

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """
        method to close sessions
        """
        self.__session.close()
