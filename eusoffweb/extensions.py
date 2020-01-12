from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin

#initialize db, SQLAlchemy is a convenient python extension to help manage database
db = SQLAlchemy()