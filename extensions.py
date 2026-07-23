from flask_bcrypt import Bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_blueprint import Blueprint


db = SQLAlchemy()
bcrypt = Bcrypt()
blueprint = Blueprint


