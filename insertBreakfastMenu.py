from eusoffweb import db, create_app
from eusoffweb.models import Breakfast

import pandas as pd

breakfastCSV = pd.read_csv("Data Files/Breakfast(1-4).csv")

app = create_app()
with app.app_context():
    for date, detail in breakfastCSV.iteritems():
        print(date + " added.")
        i = 1
        main = ""
        side = ""
        staple = ""
        special = ""
        drinks = ""

        for row in detail:
            # print(str(i) + ". " + row)
            if ( i < 5 ):
                staple += row
                staple += ", "
            elif ( i == 5 ):
                staple += row
            elif ( i > 5 and i < 10):
                main += row
                main += ", "
            elif ( i == 10 ):
                main += row
            elif ( i == 11 ):
                side += row
            elif ( i == 12 ):
                special += row
            elif ( i == 13 ):
                drinks += row
                drinks += ", "
            elif ( i == 14 ):
                drinks += row
            i += 1
        
        new_breakfast_entry = Breakfast(date=date,main=main,side=side,staple=staple,special=special,drinks=drinks)
        db.session.add(new_breakfast_entry)
        
    db.session.commit()





