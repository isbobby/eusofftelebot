# Python3 Telegram Bot 
> Telegram Bot which shows users of Eusoff Hall their meal menus for the current and next day.

### server.py  
> Contains server logic and delivers telegram updates to bot logic.  

### bot.py  
> Holds bot logic isolated from server code, can be expanded without touching server.

#### You'll need to create a .env file

`.env` file should look sth like this:
```
# Environment Config

# store your secrets and config variables in here

SECRET=<anything, was testing>
MADE_WITH=<anything, was testing>
TELEGRAM_TOKEN=<your token>
PROJECT_NAME=<truth-mine>
GROUP_CHAT_ID=<anything, was testing>
```

### Room for Improvements
1. Write unit tests (https://github.com/python-telegram-bot/python-telegram-bot/wiki/Writing-Tests)
