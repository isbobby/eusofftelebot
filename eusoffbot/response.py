class Response:
    def __init__(self,text,has_markup,reply_markup):
        self.text=text
        self.has_markup=has_markup
        self.reply_markup=reply_markup
        self.forward_messsage = False 
    
    def getTextDescription(self):
        return self.text

    def setForwardMessage(self):
        self.forward_messsage = True
    
    def hasForwardMessage(self):
        return self.forward_messsage