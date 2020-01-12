
import json
import sqlalchemy

from flask import Blueprint, render_template, url_for, redirect, request, flash

from datetime import datetime, timedelta

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template('/index.html')
    