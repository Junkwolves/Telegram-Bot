import telebot

import const

bot = telebot.TeleBot(const.token)

print(bot.get_me())

@bot.message_handler(content_types=['text'])
def handle_text(message):
    
    if message.text == "User_Message":
        audio = open("mp3/Audio_Message.mp3", 'rb')
        bot.send_chat_action(message.chat.id, 'upload_audio')
        bot.send_audio(message.chat.id, audio)
        audio.close()
		
bot.polling(none_stop=True, interval=0)