# -*- coding: utf-8 -*-
import telebot
import requests
import json
from telebot import types

bot = telebot.TeleBot("1784199672:AAGu0vsDdzrxBoEiK_4lDG9lGKZtc3QDmQg")


def main():
    markup = types.ReplyKeyboardMarkup(True)
    key1 = types.KeyboardButton('It-сайты')
    key2 = types.KeyboardButton('Онлайн-курсы')
    key3 = types.KeyboardButton('Музыка')
    key4 = types.KeyboardButton('Закрыть')
    key5 = types.KeyboardButton('EPIC')
    markup.add(key1)
    markup.add(key2)
    markup.add(key3)
    markup.add(key4)
    markup.add(key5)
    return markup


# 2
@bot.message_handler(content_types=['voice'])
def voice(message):
    if message.content_type == 'voice':
        bot.send_message(message.chat.id, "Включи автор в меня нейросети может и получится)")


@bot.message_handler(content_types=['text'])
def cont(message):
    if message.text == 'It-сайты':
        bot.send_message(message.chat.id, 'https://ru.stackoverflow.com/ Списывать работы', reply_markup=main())
        bot.send_message(message.chat.id,
                         'https://metanit.com/ Понимать,что всё невозможно изучить,но попытаться стоит',
                         reply_markup=main())
    elif message.text == 'Онлайн-курсы':
        bot.send_message(message.chat.id, 'https://www.udemy.com/ Хороший повод поучиться', reply_markup=main())
        bot.send_message(message.chat.id,
                         'https://welcome.stepik.org/ru Есть курсы и леции от наших вузов с хорошей подачей ',
                         reply_markup=main())
    elif message.text == 'Музыка':
        bot.send_message(message.chat.id,
                         'https://www.youtube.com/watch?v=tiV1XSdW-x4/ cover lovely один из лучщих в мире',
                         reply_markup=main())
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=YykjpeuMNEk/ ', reply_markup=main())
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=0-7IHOXkiV8/ ', reply_markup=main())

    elif message.text == "EPIC":
        response = requests.get("https://api.nasa.gov/planetary/apod?api_key=AVqwbKdbgZo8e3gCrlhJKOc2a3303sh5lDEYdDLs")
        apod = response.json()["url"]
        apodtext = response.json()["explanation"]
        bot.send_message(message.chat.id, apod )
        bot.send_message(message.chat.id, apodtext)

    elif message.text == 'Закрыть':
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, 'Выполнено,хотите заново кнопки,напишите /start', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю', reply_markup=main())


@bot.message_handler(commands=['start'])
# 3
def start(message):
    bot.send_message(message.from_user.id, "Как вас зовут?");
    bot.register_next_step_handler(message, name);


def name(message):
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Привет, ' + name + '. Какая у ва фамилия?');
    bot.register_next_step_handler(message, surname);


def surname(message):
    global surname;
    surname = message.text;
    bot.send_message(message.from_user.id, 'А сколько тебе лет то?');
    bot.register_next_step_handler(message, age);


def age(message):
    global age;
    while age == 0:
        try:
            age = int(message.text)  # проверяем, что возраст введен корректно
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    bot.send_message(message.from_user.id,
                     'Понял, ' + name + ', тебе ' + str(
                         age) + ' лет. Смотри, не теряй жизнь без оглядки,ну и не стоит злоупотреблять работой, ведь чем большего ты добьёшься '
                                ',чем меньше потом надо тратить время на работу.')
    bot.send_message(message.from_user.id, 'Кстати, вы дисциплинированный человек?');
    bot.register_next_step_handler(message, dic);


def dic(message):
    global dic;
    dic = message.text;
    if message.text == 'Да':
        bot.send_message(message.from_user.id,
                         'Я бы немного переосмыслил, ' + name + '. Ведь дисциплина это скучно,и нудно');
    else:
        bot.send_message(message.from_user.id, 'Ну тогда вы довольно хороши, ' + name + '.Продолжайте в том же духе')


# 4
def zar(message):
    if message.chat.type == 'private':
        if message.text == 'Закрыть':
            markup = types.ReplyKeyboardRemove(selective=False)


# 5
response = requests.get("https://reqres.in/api/users/2")
mail = response.json()
print(mail["data"]["email"])
bot.polling()
