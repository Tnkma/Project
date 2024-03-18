#!/usr/bin/python3
""" Storage Class for the database """
from models.base import BaseUser, JobOffer, Base
from models.users_cls import Client, Plumber
import sqlalchemy
import models
from sqlalchmey import create_engine
from sqlalchmey.orm import scoped_session, sessionmaker

class DataStorage:
    """ Interacts with our mysql database """
    __engine = None
    __session = None
    
    def __init__(self):
        """ instatiate the datastorage object """
        MYSQL_USER = MYSQL_USER
        MYSQL_PWD = MYSQL_PWD
        MYSQL_HOST = MYSQL_HOST
        DB_NAME = DB_NAME
        self.__engine = create_engine('mysql+pymysql://{}:{}@{}/{}'.
                                      format(MYSQL_USER = 'jobatuser',
                                             MYSQL_PWD = 'Jobat@password',
                                             MYSQL_HOST = 'localhost',
                                             DB_NAME = 'jobat_base'
                                             ))
        Base.metadata.drop_all(self.__engine)
        
    
    def add_new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)
    
    def commit_db(self):
        """ commit the changes to the database """
        self.__session.commit()
        
    def delete(self, obj=None):
        """ Deletes from the current database seesion """
        if obj is not None:
            self.__session.delete()
            
    def reload(self):
        """ Reloads data from the database """
        Base.metadata.create_all(self.__engine)
        sessions = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sessions)
        self.__session = Session
        
    def close(self):
        """ calls remove method on the private session """
        self.__session.remove()
        
    def get(self, cls, id):
        """ Gets the object based on class name and id or None if not found """
        if cls not in classes.values():
            return None
        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value
        return None