from eusoffbot.response import Response

from telegram import KeyboardButton, ReplyKeyboardMarkup


class PublicationBot():

    def getPubsResponse(self):
        """
        This provides users with a few recognizable inputs:
        Eusoff Wordpress, Eusoffworks Facebook, Home
        """
        CustomReplyArray = [
            [KeyboardButton("Eusoff Wordpress")],
            [KeyboardButton("Eusoffworks Facebook")],
            [KeyboardButton("Home")]
        ]
        CustomReply = ReplyKeyboardMarkup(keyboard=CustomReplyArray)
        response = Response(text="Check out the latest photos and articles here",
                            has_markup=True, reply_markup=CustomReply)
        return response

    def getEusoffWordpress(self):
        return Response(text="https://eusoffhall.wordpress.com", has_markup=True, reply_markup=None)

    def getEusoffWorksFB(self):
        return Response(text="https://www.facebook.com/pg/EHeusoffworks/photos", has_markup=True, reply_markup=None)

    def getNCOVAnnonucement(self):
        return Response(text="URGENT: Please click on https://emergency.nus.edu.sg/circulars to access an important NUS advisory regarding the Novel Coronavirus Pneumonia.", has_markup=True, reply_markup=None)

    def getOperationHoursMenu(self):
        CustomReplyArray = [
            [KeyboardButton("Dining Hall"), KeyboardButton("Hall Office")],
            [KeyboardButton("Central Library"), KeyboardButton("NUS Buses")],
            [KeyboardButton("Home")]
        ]
        CustomReply = ReplyKeyboardMarkup(keyboard=CustomReplyArray)
        response = Response(text="Choose to view the respective operation timing",
                            has_markup=True, reply_markup=CustomReply)
        return response

    def getDiningHallTime(self):
        return Response(text="Breakfast \n7:00 AM - 10:00 AM\n\nDinner \n5:30 PM - 9:00 PM", has_markup=True, reply_markup=None)

    def getHallOfficeTime(self):
        return Response(text="Mon - Thur\n8:30 AM - 6:00 PM\n\nFriday\n8:30 AM - 5:30 PM\n\nLunch Break\n1:00 PM - 2:00 PM\n\nClosed on weekends and public holidays.", has_markup=True, reply_markup=None)

    def getCentralLibraryTime(self):
        return Response(text="Mon - Fri\n8:30 AM - 9:00 PM\n\nSat 10:00 AM - 5:00 PM\nClosed on Sunday", has_markup=True, reply_markup=None)

    def getNUSBus(self):
        textReply = """
        A1/A2
    Mon - Sat
    7:15 AM - 11:00 PM
    Sunday/Public Holidays
    9:00 AM - 11:00 PM
        
    B1/B2
    Mon - Fri 
    7:15 AM - 11:00 PM
    Sat 
    9:00 AM - 7:00 PM
    No service on Sunday/Public Holidays

    C:
    Mon - Fri 
    7:20 AM - 11:00 PM
    Sat 
    7:40 AM - 7:00 PM
    No service on Sunday/Public Holidays

    D1/D2:
    Mon - Sat 
    7:15 AM - 11:00 PM
    Sunday/Public Holidays 
    9:15 AM - 11:00 PM

    BTC:
    Mon - Fri
    7:20 AM - 9:30 PM
    Sat
    8:30 AM - 12:30 PM
    No service on Sunday/Public Holidays
        """
        return Response(text=textReply, has_markup=True, reply_markup=None)