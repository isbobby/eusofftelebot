
import json
import sqlalchemy

from flask import Blueprint, render_template, url_for, redirect, request, flash

from datetime import datetime, timedelta
from eusoffweb import db
from eusoffweb.models import Dinner,Breakfast,Event

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():

    # entry = Dinner(date='2020-01-01',main='Main',side='Side',soup='Soup',dessert='Dessert', special="special")
    # db.session.add(entry)
    # db.session.commit()

    return render_template('/index.html')