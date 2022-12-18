import telebot as t
from telebot import types
import random as r
from gtts import gTTS
import os


bot = t.TeleBot('5931069298:AAEXfbRSe8iHMhFz7BQE7oHIsQPlf22BzmM')
mems =[]

@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    item = types.KeyboardButton('/mem')
    markup.add(item)
    bot.send_message(message.chat.id, f'Привет {message.chat.first_name} \U0001F63A', reply_markup= markup)
    # bot.send_photo(message.chat.id, open(r"C:\Users\User\Pictures\Camera Roll\15_main-v1658903024.jpg", 'rb'))

@bot.message_handler(commands = ['mem'])
def send_mem(message):
    mems.append(r"C:\Users\User\Pictures\Camera Roll\15_main-v1658903024.jpg")
    mems.append(r"C:\Users\User\Pictures\Camera Roll\36e5bfa73c887015ec759be094566be9192df9cf9f1da244e283b7762da4e080.jpg")
    mems.append(r"C:\Users\User\Pictures\Camera Roll\1648333203_1-kartinkof-club-p-30-let-mem-1.jpg")
    mems.append(r"C:\Users\User\Pictures\Camera Roll\Без названия.jfif")
    bot.send_photo(message.chat.id, open(r.choice(mems), 'rb'))
    
@bot.message_handler(content_types = ['sticker'])
def get_sticker(message):
    bot.send_message(message.chat.id, f'{message.chat.first_name}, мне все равно на твои эмоции')

@bot.message_handler(content_types = ['text'])
def got_text(message):
    mytext = message.text
    audio = gTTS(text = mytext , lang='ru', slow = False)
    PATH = os.path.abspath(__file__+'/..')

    audio.save(os.path.join(PATH,"example.mp3"))
    # aud = "example.mp3", 'rb'
    # bot.send_audio(message.chat.id, open(aud))
    file = open(os.path.join(PATH,'example.mp3'), 'rb')
    bot.send_voice(message.chat.id, file)

 




bot.infinity_polling()


