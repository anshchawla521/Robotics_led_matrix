from typing import Text
import telebot
import time
import credentials

bot_token=credentials.bot_token

bot = telebot.TeleBot(token = bot_token)

def findat(msg):
    # from a list of texts, it finds the one with the '@' sign
    for i in msg:
        if '@' in i:
            return i

@bot.message_handler(commands=['Greet'])
def send_welcome(message):
    bot.reply_to(message,'welcome')


@bot.message_handler(commands=['Hello'])
def hello(message):
    bot.send_message(message.chat.id,'Hey,How are You??')

@bot.message_handler(commands=['PEC'])
def celeb(message):
    bot.reply_to(message,'Celebrating 100 years')

@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
def at_answer(message):
    texts=message.text.split()
    at_text=findat(texts)

    if at_text == '@': # in case it's just the '@', skip
        pass
    else:
        insta_link = "https://instagram.com/{}".format(at_text[1:])
        bot.reply_to(message, insta_link)

bot.polling()
    

