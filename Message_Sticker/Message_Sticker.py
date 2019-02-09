import telebot

import const

bot = telebot.TeleBot(const.token)

print(bot.get_me())

@bot.message_handler(content_types=['text'])
def handle_text(message):
    
    if message.text == "User_Message":
        bot.send_sticker(message.chat.id, const.Sticker_id)
		
bot.polling(none_stop=True, interval=0)