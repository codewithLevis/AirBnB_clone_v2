#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import environ

storage_form = environ.get('HBNB_TYPE_STORAGE', 'file')


if storage_form == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
