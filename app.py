#!/usr/bin/python3
""" Firing up Flask"""
from models.base import app


if __name__ == "__main__":
    app.run(debug=True)

