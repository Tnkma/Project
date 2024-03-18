#!/usr/bin/python3
"""Base models for other models"""

from datetime import datetime
import models
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

if models.storage_db == "db":
    Base = declarative_base()


class BaseUser(db.model, UserMixin):
    """The Base User for clients and plumbers"""
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    image_file = Column(String(20), nullable=False, default='default.jpg')
    password_hash = Column(String(60), nullable=False)
    date_joined = Column(DateTime, nullable=False, default=datetime.utcnow)
    phone_no = Column(Integer(15), unique=True, nullable=False)
    state = Column(String(20), nullable=False)
    
    def __repr__(self):
        """Returns the string representation of our BaseUser"""
        return f"BaseUser('{self.username}', '{self.email}', '{self.image_file}')"
    
    def set_password(self, password):
        """ Generate a password hash """
        self.password_hash = generate_password_hash(password)
    
    
    def check_password(self, password):
        """ Checks the password hash """
        return check_password_hash(self.password_hash, password)   
    
class JobOffer(db.model):
    """This model will contain job_offers posted by clients"""
    id = Column(Integer, primary_key=True)
    job_title = Column(String(100), nullable=False)
    content = Column(String(1000), nullable=False)
    date_posted = Column(DateTime, nullable=False, default=datetime.utcnow)
    client_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    
    def __repr__(self):
        """Returns the string representation of JobOffer"""
        return f"JobOffer('{self.job_title}', '{self.content}', '{self.date_posted}')"