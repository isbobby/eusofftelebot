from eusoffweb import db, create_app
from eusoffweb.models import Dinner

import pandas as pd
dinnerCSV = pd.read_csv("Data Files/Dinner(1-4).csv")

app = create_app()
with app.app_context():
    for date, detail in dinnerCSV.iteritems():
        print(date + " added.")
        i = 1
        main = ""
        side = ""
        soup = ""
        special = ""
        dessert = ""

        for row in detail:
            if ( i < 3 ):
                main += row
                main += ", "
            elif ( i == 3 ):
                main += row
            elif ( i > 3 and i < 6  ):
                side += row 
                side += ", "
            elif ( i == 6 ):
                side += row
            elif ( i == 7 ):
                soup += row
            elif ( i == 8 ):
                special += row
            elif ( i == 9 ):
                dessert += row
            i += 1
        
        new_dinner_entry = Dinner(date=date,main=main,side=side,soup=soup,special=special,dessert=dessert)
        db.session.add(new_dinner_entry)
        
    db.session.commit()





