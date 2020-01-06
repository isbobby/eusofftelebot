from flask import Flask, request
import telegram
from eusoffbot.credentials import bot_token, bot_user_name, URL
from eusoffbot.mastermind import get_response

global bot
global TOKEN

TOKEN = bot_token

bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    # retrieve the message in JSON and then transform it to the Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    msg_id = update.message.message_id
    text = update.message.text.encode('utf-8').decode()
    
    #Print to terminal
    print("got text message :", text)
    response = get_response(text)
    
    if (response.hasMarkup):
        bot.sendMessage(chat_id=chat_id, text=response.text, reply_to_message_id=msg_id, reply_markup=response.markup)
    else:
        bot.sendMessage(chat_id=chat_id, text=response.text, reply_to_message_id=msg_id)
    return 'ok'

@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    # we use the bot object to link the bot to our app which live
    # in the link provided by URL
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    # something to let us know things work
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"

@app.route('/')
def index():
    return '.'

if __name__ == '__main__':
    # note the threaded arg which allow
    # your app to have more than one thread
    app.run(threaded=True)
