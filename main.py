import telebot

import const

bot = telebot.TeleBot(const.token)

print(bot.get_me())

def info(message, answer):
    from datetime import datetime
    print("   ----------------------------------------------------------------------------------------------" + "\n")
    print("   | - Date  |  =  " + str(datetime.now()) + " \n")
    print("   | - User  |  =  {0}.      |  {1}. ".format(message.from_user.first_name,message.from_user.last_name) + "\n")
    print("   | UserID  |  =  {0}. ".format(str(message.from_user.id)) + "\n")
    print("   | Message |  =  {0}. ".format(message.text) + "   | Answer |  =  " + answer + "\n")
    print("   ----------------------------------------------------------------------------------------------" + "\n")

@bot.message_handler(commands=['start'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Music')
    bot.send_message(message.from_user.id, "Greetings my friend!!!", reply_markup = user_markup)
    answer = "Command list"
    info(message, answer)

@bot.message_handler(commands=['help'])
def handle_text(message):
    answer = "Доступные Треки: ..."
    bot.send_message(message.chat.id, "  Доступные Треки: \n   1.  Енотик полоскун \n   2.   \n   3.   ")
    info(message, answer)

@bot.message_handler(content_types=['text'])
def handle_text(message):

    answer =  "KABO!"   
    
    if message.text == "Howdy" or message.text == "howdy":
        answer =  "HOWDY PARTNER!" 
        bot.send_message(message.chat.id, "HOWDY PARTNER!")
        info(message, answer)

    elif message.text == "Music":
        answer =  "Доступные Треки: ..."
        bot.send_message(message.chat.id, "  Доступные Треки: \n   1.  Енотик полоскун \n   2.   \n   3.   ")
        info(message, answer)

    elif message.text == "Енотик полоскун" or message.text == "1":
        answer =  "Енотик полоскун.mp3"
        audio = open("...", 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id, audio)
        audio.close()
        info(message, answer)

    else:
        bot.send_message(message.chat.id, answer)
        info(message, answer)

bot.polling(none_stop=True, interval=0)