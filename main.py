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
    user_markup.row('Музыка')
    user_markup.row('Гадза', 'Слава Украине!')
    bot.send_message(message.from_user.id, "Greetings my friend!!! \n You just gonna scroll past without saying howdy?", reply_markup = user_markup)
    answer = "Command list"
    info(message, answer)

@bot.message_handler(commands=['help'])
def handle_text(message):
    answer = "no"
    bot.send_message(message.chat.id, " no : (")
    info(message, answer)

@bot.message_handler(content_types=['text'])
def handle_text(message):

    answer =  "KABO!"   
    
    if message.text == "Howdy" or message.text == "howdy":
        answer =  "HOWDY PARTNER!" 
        bot.send_message(message.chat.id, "HOWDY PARTNER!")
        bot.send_sticker(message.from_user.id, const.Howdy_id)
        info(message, answer)
        
    elif message.text == "Назад" or message.text == "Меню":
        answer = "Command list"
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Музыка')
        user_markup.row('Гадза', 'Слава Украине!')
        bot.send_message(message.from_user.id, "Меню" , reply_markup = user_markup)
        info(message, answer)

    elif message.text == "Музыка":
        answer = "Music list"
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Енотик полоскун')
        user_markup.row('Тупа Отдыхаю')
        user_markup.row('Опа нихуёвая зигота')
        user_markup.row('Назад')
        bot.send_message(message.from_user.id, "Доступные Треки: \n ", reply_markup = user_markup)
        info(message, answer)

    elif message.text == "Енотик полоскун":
        answer =  "Енотик полоскун.mp3"
        audio = open(".../Глад Валакас – Енотик полоскун.mp3", 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id, audio)
        audio.close()
        info(message, answer)

    elif message.text == "Тупа Отдыхаю":
        answer =  "Тупа Отдыхаю.mp3"
        audio = open(".../Глад Валакас – Тупа Отдыхаю.mp3", 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id, audio)
        audio.close()
        info(message, answer)

    elif message.text == "Опа нихуёвая зигота":
        answer =  "Опа нихуёвая зигота.mp3"
        audio = open(".../Глад Валакас – Опа нихуёвая зигота.mp3", 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id, audio)
        audio.close()
        info(message, answer)

    elif message.text == "Слава Украине!":
        answer =  "Героям слава!"
        bot.send_message(message.chat.id, "Героям слава!")
        voice = open(".../Глад Валакас – Гимн Украины.ogg", 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_voice(message.from_user.id, voice)
        voice.close()
        info(message, answer)

    elif message.text == "Гадза" or message.text == "гадза":
        answer =  "Гадза"
        voice = open(".../Глад Валакас – Годзила 3 4 5 0 Д.ogg", 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_voice(message.from_user.id, voice)
        voice.close()
        info(message, answer)
        
    else:
        if const.counter == 1:
            voice = open(".../Глад Валакас – КАВО.ogg", 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_audio')
            bot.send_voice(message.from_user.id, voice)
            voice.close()

            const.counter = 2

            info(message, answer)

        elif const.counter == 2:
            answer =  "Шо"
            voice = open(".../Валакас – Шо.ogg", 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_audio')
            bot.send_voice(message.from_user.id, voice)
            voice.close()

            const.counter = 3
        
        elif const.counter == 3:
            answer =  "СЛОЖНА"
            voice = open(".../Папич – СЛОЖНА.ogg", 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_audio')
            bot.send_voice(message.from_user.id, voice)
            voice.close()

            const.counter = 4

            info(message, answer)

        elif const.counter == 4:
            answer =  "Завали ебало"
            voice = open(".../Папич – Завали ебало.ogg", 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_audio')
            bot.send_voice(message.from_user.id, voice)
            voice.close()

            const.counter = 1

            info(message, answer)


bot.polling(none_stop=True, interval=0)