from eusoffweb import db

class Breakfast(db.Model):
    """ 
    Attributes (date, staple, main, side, special, drinks)
    SQL FORMAT:
    1, 2020-01-01, 'Special Menu', 'Staple Menu', 'Drink Menu'

    INSERT INTO breakfast VALUES ( 1, '2020-01-01', 'Staple Menu', 'Main Menu', 'Side Menu', 'Special Menu', 'Drinks Menu' );
    """
    __tablename__ = 'breakfast'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    staple = db.Column(db.String(300), nullable=False)
    main = db.Column(db.String(300), nullable=False)
    side =  db.Column(db.String(100), nullable=False)
    special =  db.Column(db.String(100), nullable=False)
    drinks = db.Column(db.String(100), nullable=False)

    def getDatabaseFormat(self):
        """ 
        Returns a string which describes the database format. 
        """
        return "INT, DATE, STR(300), STR(300), STR(100), STR(100), STR(100)"

    def toString(self):
        """
        Returns a descriptive string for today's breakfast
        """
        descriptiveString = (
            "Staple - " + self.staple + "\n" + "\n" +
            "Main - " + self.main + "\n" + "\n" +
            "Side - " + self.side + "\n" + "\n" +
            "Special - " + self.special + "\n" + "\n" +
            "drinks - " + self.drinks + "\n" 
        )

        return descriptiveString

class Dinner(db.Model):
    """ 
    Attributes (date (db.Date), main, side, soup, special, dessert)
    SQL FORMAT:
    1, '2020-01-01', 'Main Menu', 'Side Menu', 'Soup Menu', 'Dessert Menu' 

    INSERT INTO dinner VALUES ( 1, '2020-01-01', 'Main Menu', 'Side Menu', 'Soup Menu', 'Special Menu','Dessert Menu' );
    """
    __tablename__ = 'dinner'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    main = db.Column(db.String(300), nullable=False)
    side = db.Column(db.String(300), nullable=False)
    soup = db.Column(db.String(100), nullable=False)
    special = db.Column(db.String(100), nullable=False)
    dessert = db.Column(db.String(100), nullable=False)        

    def getDatabaseFormat(self):
        """ 
        Returns a string which describes the database format. 
        """
        return "INT, DATE, STR(300), STR(300), STR(100), STR(100), STR(100)"

    def toString(self):
        """
        Returns a descriptive string for today's dinner
        """

        descriptiveString = (
            "Main - " + self.main + "\n" + "\n" +
            "Side - " + self.side + "\n" + "\n" +
            "Soup - " + self.soup + "\n" + "\n" +
            "Special - " + self.special + "\n" + "\n" +
            "Dessert - " + self.dessert 
        )

        return descriptiveString

class Event(db.Model):
    """
    SQL FORMAT
    1, '2020-01-01 00:00:00', 'Description', 'Venue', 
    """
    __tablename__ = 'event'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, nullable=False)
    venue = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000))

    