from flask import Flask, request
import telegram
from eusoffbot.credentials import bot_token, bot_user_name, URL
from eusoffbot.mastermind import getResponse
from eusoffweb import create_app
global bot
global TOKEN

TOKEN = bot_token

bot = telegram.Bot(token=TOKEN)

app = create_app()

@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    # retrieve the message in JSON and then transform it to the Telegram object
    
    # for overwhelming updates, clear the update attemp (this line below)
    # and have the method return 1 to clear all pending updates
    try:
        update = telegram.Update.de_json(request.get_json(force=True), bot)
    except:
        print("some error has occured internally")

    if update.message:
        chat_id = update.message.chat.id
        msg_id = update.message.message_id
        user = update.message.from_user 
        text = update.message.text.encode('utf-8').decode()
        info = "got text message: " + text + " from " + user.username
        print(info)
        response = getResponse(update.message)
        
        if response.has_markup:
            try:
                bot.sendMessage(chat_id=chat_id, text=response.text, reply_to_message_id=msg_id, reply_markup=response.reply_markup)
            except:
                print("message is lost, bot has no target to reply")
        else:
            try:
                bot.sendMessage(chat_id=chat_id, text=response.text, reply_to_message_id=msg_id)
            except:
                print("message is lost, bot has no target to reply")

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

if __name__ == '__main__':
    # note the threaded arg which allow
    # your app to have more than one thread
    app.run(threaded=True, debug=True)
