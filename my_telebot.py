import telebot
import random 
bot = telebot.TeleBot("6041895272:AAEakSLfayVJWDE4u1RRBxQZ4eC1wGy89-k")
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard = False)
list_buttons = []
for i in range(9):
    button = telebot.types.KeyboardButton(f"{i}")
    list_buttons.append(button)
# keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard = False)

for count in range(3):
    keyboard.add(list_buttons[count * 3], list_buttons[count * 3 + 1], list_buttons[count * 3 + 2])


@bot.message_handler(commands = ['start'])

def start(message):
    bot.send_message(message.chat.id, "Hello User! Enter 0-8", reply_markup = keyboard)
    bot.register_next_step_handler(message, random2)

random_numbers = random.randint(0, 8)
def random2(message):
    if message.text == str(random_numbers):
        bot.send_message(message.chat.id, "That's right! You win, good job. Game over", reply_markup = telebot.types.ReplyKeyboardRemove())
    else:
        bot.send_message(message.chat.id, "Nice try, but no! Try again")
        bot.register_next_step_handler(message, random2)


bot.polling()