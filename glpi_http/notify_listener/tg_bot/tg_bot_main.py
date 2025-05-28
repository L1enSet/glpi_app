#import logging
import time
import telebot
#from telebot import types




#logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w")
#logging.debug("A DEBUG Message")
#logging.info("An INFO")
#logging.warning("A WARNING")
#logging.error("An ERROR")
#logging.critical("A message of CRITICAL severity")
#logging.exception(except)


#logging.basicConfig(level=logging.INFO, filename="bot_log.log", filemode="a", format="%(asctime)s %(levelname)s %(message)s")


TOKEN = '5724389208:AAHaWn0yrph6lGE19yZMLedvxFhEg8-lGG4'
tb = telebot.TeleBot(TOKEN)


@tb.message_handler(commands=['get_message', 'go', 'get_image', 'get_cat'])
def start_func(message):
    try:
        functions = {
            '/get_message':get_message
            }

        user = "{}-{}".format(message.chat.id, message.chat.username)
        #logging.info("user {} input command {}".format(user, message.text))

        return functions[message.text](message)

    except KeyError as exc:
        #logging.info("KeyError No command {}".format(message.text))
        
        tb.send_message(message.chat.id, "Нет такой команды.")




#def bot_info(message):
#
#    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
#    item_1 = types.KeyboardButton("Анекдот")
#    item_2 = types.KeyboardButton("Погода")
#    item_3 = types.KeyboardButton("Пробки")
#    markup.add(item_1, item_2, item_3)
#
#    tb.send_message(message.chat.id, "Select Func", reply_markup = markup)
#    return 0


    
def get_message(message):
    user = "{}-{}".format(message.chat.id, message.chat.username)
    tb.send_message(message.chat.id, user)

    
    #logging.info("user {} use func get_message".format(user))

    return 0



def main():
    global tb

    while True:
        try:
            #logging.info("BoT starting!")
            tb.infinity_polling()

        except ConnectionResetError as conn_err:
            #logging.info("Bot stop polling exc - ConnectionResetError")
            time.sleep(3)

        except Exception as exc:
            #logging.exception(exc)
            #logging.info("Bot stop polling HTTPSConnectionPool")
            time.sleep(3)


if __name__ == '__main__':
    main()