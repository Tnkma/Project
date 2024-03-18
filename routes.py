#!/usr/bin/python3
from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class BaseUser(db.Model):
    """The Base User for clients and plumbers"""
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    image_file = Column(String(20), nullable=False, default='default.jpg')
    password_hash = Column(String(60), nullable=False)
    date_joined = Column(DateTime, nullable=False, default=datetime.utcnow)
    phone_no = Column(Integer, unique=True, nullable=False)
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
    
class JobOffer(db.Model):
    """This model will contain job_offers posted by clients"""
    id = Column(Integer, primary_key=True)
    job_title = Column(String(100), nullable=False)
    content = Column(String(1000), nullable=False)
    date_posted = Column(DateTime, nullable=False, default=datetime.utcnow)
    client_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    
    def __repr__(self):
        """Returns the string representation of JobOffer"""
        return f"JobOffer('{self.job_title}', '{self.date_posted}')"

if __name__ == "__main__":
    app.run(debug=True)
