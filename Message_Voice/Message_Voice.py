import telebot

import const

bot = telebot.TeleBot(const.token)

print(bot.get_me())

@bot.message_handler(content_types=['text'])
def handle_text(message):
    
    if message.text == "User_Message":
        voice = open("ogg/Voice_Message.ogg", 'rb')
        bot.send_chat_action(message.chat.id, 'upload_audio')
        bot.send_voice(message.chat.id, voice)
        voice.close()
		
bot.polling(none_stop=True, interval=0)