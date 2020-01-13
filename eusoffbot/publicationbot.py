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
        response = Response(text="ChecK out the latest photos and articles here",
                            has_markup=True, reply_markup=CustomReply)
        return response

    def getEusoffWordpress(self):
        return Response(text="https://eusoffhall.wordpress.com", has_markup=True, reply_markup=None)

    def getEusoffWorksFB(self):
        return Response(text="https://www.facebook.com/pg/EHeusoffworks/photos", has_markup=True, reply_markup=None)    

