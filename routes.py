#!/usr/bin/python3
from flask import Flask, render_template, request, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)

app.config['SECRET_KEY'] = ''
db = SQLAlchemy(app)
