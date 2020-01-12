from eusoffweb import db, create_app
from eusoffweb.models import Breakfast, Dinner, Event

app = create_app()

with app.app_context():
    """ 
    Create all tables 
    """
    db.create_all()
