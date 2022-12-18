import random 
import telebot as t
bot = t.TeleBot('5925349745:AAG8tXuahuboUbNJvP4y099vAREAJts7V0s')
@bot.message_handler(commands = ['start'])
def start(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, 'Привет, вот мои команды: \n /anekdot')


anekdots = ["""В прошлом году был в Каменце-Подольском. 
Проходил мимо ресторана 'Ситий митник' ("Сытый таможенник"). Еще подумал: "А что бывают голодные?""",
"""Когда утки летят клином, как называется расстояние между соседними утками? — ПромежУток?""",
"""— Розочка, Ви слышали, Циля Марковна пятого мужа в крематорий свезла? 
 Таки да жизнь несправедлива.... , одним ни одного мужа, а другие ими печку топят. """
]

@bot.message_handler(commands = ['anekdot'])
def anekdot(message):
    bot.send_message(message.chat.id, anekdots[random.randint(0,len(anekdots)-1)])

@bot.message_handler(content_types= ['voice'])
def voice(message):
    bot.send_message(message.chat.id, 'Я рад слышать твой голос')
    bot.send_message(662765024, f'Пользователь @{message.from_user.username} отправил мне голосовое сообщение.')
    bot.forward_message(662765024, message.chat.id, message.id)


bot.infinity_polling()

