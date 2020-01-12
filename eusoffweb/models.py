from eusoffweb import db

class Breakfast(db.Model):
    __tablename__ = 'breakfast'
    __table_args__ = {'extend_existing': True}

    """ 
    SQL FORMAT:
    1, 2020-01-01, 'Special Menu', 'Staple Menu', 'Drink Menu'

    INSERT INTO breakfast VALUES ( 1, '2020-01-01', 'Special Menu', 'Staple Menu', 'Drink Menu' );
    """

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    staple = db.Column(db.String(100), nullable=False)
    special = db.Column(db.String(100), nullable=False)
    drinks = db.Column(db.String(100), nullable=False)

    def getDatabaseFormat(self):
        """ 
        Returns a string which describes the database format. 
        """
        return "id:1, date:2020-01-01, staple:'Staple Menu', specail:'Special Menu', drink'Drink Menu'"

    def toString(self):
        """
        Returns a descriptive string for today's breakfast
        """
        descriptiveString = (
            "Main - " + self.staple + "\n" +
            "Special - " + self.special + "\n" +
            "drinks - " + self.drinks + "\n" 
        )

        return descriptiveString

        

class Dinner(db.Model):
    __tablename__ = 'dinner'
    __table_args__ = {'extend_existing': True}

    """ 
    SQL FORMAT:
    1, '2020-01-01', 'Main Menu', 'Side Menu', 'Soup Menu', 'Dessert Menu' 

    INSERT INTO dinner VALUES ( 1, '2020-01-01', 'Main Menu', 'Side Menu', 'Soup Menu', 'Special Menu','Dessert Menu' );
    """

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    main = db.Column(db.String(100), nullable=False)
    side = db.Column(db.String(100), nullable=False)
    soup = db.Column(db.String(100), nullable=False)
    special = db.Column(db.String(100), nullable=False)
    dessert = db.Column(db.String(100), nullable=False)

    def getDatabaseFormat(self):
        """ 
        Returns a string which describes the database format. 
        """
        return "( id:1, date:'2020-01-01', main:'Main Menu', side:'Side Menu', soup:'Soup Menu', special:'Special Menu', dessert:'Dessert Menu' )"

    def toString(self):
        """
        Returns a descriptive string for today's dinner
        """

        descriptiveString = (
            "Main - " + self.main + "\n" +
            "Side - " + self.side + "\n" +
            "Soup - " + self.soup + "\n" +
            "Special - " + self.special + "\n" +
            "Dessert - " + self.dessert 
        )

        return descriptiveString
