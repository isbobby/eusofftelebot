from eusoffweb import db, create_app
from eusoffweb.models import Breakfast, Dinner, Event

app = create_app()

with app.app_context():
    """ 
    Drops all and create all tables 
    """
    Breakfast.__table__.drop(db.engine)
    Dinner.__table__.drop(db.engine)
    Event.__table__.drop(db.engine)

    db.create_all()
