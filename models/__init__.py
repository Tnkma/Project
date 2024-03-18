#!/usr/bin/python3
""" initialize the data storage models """

storage_db = 'db'

if storage_db == 'db':
    from models.engine.data_storage import DataStorage
    storage = DataStorage
storage.reload()