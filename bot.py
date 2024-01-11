#библиотеки, которые загружаем из вне
import telebot
TOKEN = 'вставьте свой токен'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	
	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("😁 Happy")
	item2 = types.KeyboardButton("😭 Sad")
	item3 = types.KeyboardButton("😎 Cool")

	markup.add(item1, item2, item3)

	bot.send_message(message.chat.id, "Привет, {0.first_name}! Какой ты котик сегодня?".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	sti1 = open('happy.webp', 'rb')
	sti2 = open('sad.webp', 'rb')
	sti3 = open('cool.webp', 'rb')
	
	if message.chat.type == 'private':
		if message.text == '😁 Happy':
			bot.send_sticker(message.chat.id, sti1)
		elif message.text == '😭 Sad':
			bot.send_sticker(message.chat.id, sti2)
		elif message.text == '😎 Cool':
			bot.send_sticker(message.chat.id, sti3)
		else:
			bot.send_message(message.chat.id, 'Не знаю что ответить😢')


bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods
