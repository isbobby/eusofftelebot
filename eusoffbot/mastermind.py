from eusoffbot import markup
from eusoffbot import replies

class Response:
    def __init__(self,text,markup,hasmarkup):
        self.text=text
        self.markup=markup
        self.hasMarkup=hasmarkup

def get_response(msg):
    if msg == "/start":
        new_response = Response(text="Hi",hasmarkup=True,markup="markup.ResponseMarkup")
        return new_response
    else:
        new_response = Response(text="nah",hasmarkup=False,markup="")
        return new_response