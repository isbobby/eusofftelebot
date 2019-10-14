from src.main import bot, logger, time

while True:
    try:
        bot.polling()
    # ConnectionError and ReadTimeout because of possible timout of the requests library
    # TypeError for moviepy errors
    # maybe there are others, therefore Exception
    except Exception as e:
        logger.error(e)
        time.sleep(15)

