import os

from flask import Flask
from eusoffweb.config import Config
from eusoffweb.extensions import db

from eusoffweb.models import Breakfast

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    #pass our web app to the extension packages
    db.init_app(app)
    
    #initialize admin
    # admin = Admin(app, name='JerseyBidding', template_mode='bootstrap3')
    
    #import the routes as classes and register these blueprints into the flask app
    from eusoffweb.main.routes import main

    app.register_blueprint(main)

    #initialize admin view pages so we can view things in the admin interface
    # admin.add_view(ModelView(User, db.session))
    # admin.add_view(ModelView(Choice, db.session))
    # admin.add_view(ModelView(JerseyNumber, db.session))
    # admin.add_view(ModelView(Gender, db.session))
    # admin.add_view(ModelView(UserSports, db.session))
    # admin.add_view(ModelView(Sport, db.session))
    # admin.add_view(ModelView(FlaskUser, db.session))
    # admin.add_view(ModelView(Role, db.session))
    # admin.add_view(ModelView(FlaskUserRoles, db.session))


    return app