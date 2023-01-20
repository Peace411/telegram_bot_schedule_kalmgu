from items import items
from mysql import client_mysql
import re
import time
import datetime
import telebot
from threading import Thread
import schedule

import Parser

bot = telebot.TeleBot('key')
responce = Parser
menu_items = items.MenuItems


@bot.message_handler(commands=['start'])
def start(message):
    if client_mysql.get_id(int(message.from_user.id)) != None:

        if client_mysql.get_notification(message.from_user.id) == 0 or client_mysql.get_notification(
                message.from_user.id) == None:
            markup_inline = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup_inline.add(menu_items.item_yes, menu_items.item_no, menu_items.item_tomorrow,
                              menu_items.item_notification_on)
            bot.send_message(message.chat.id, 'Сделайте выбор', reply_markup=markup_inline)
        else:
            markup_inline = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup_inline.add(menu_items.item_yes, menu_items.item_no, menu_items.item_tomorrow,
                              menu_items.item_notification_off)
            bot.send_message(message.chat.id, 'Сделайте выбор', reply_markup=markup_inline)
    else:
        bot.send_message(message.chat.id,
                         'напишите ваш факултет и  группу как на сайте kalmsu.ru, пример:ФМФИТ-ФИЗИКА3bоф')
        bot.register_next_step_handler(message, get_name_gruop)


@bot.message_handler(commands=['reset'])
def resret(message):
    client_mysql.reset(message.from_user.id)
    bot.send_message(message.chat.id, 'Настройки сброшены, выполнитите команду /start')


def get_name_gruop(message):
    name_group = message.text.lower()
    id_group = Parser.search_by_group(name_group)
    if id_group == None:
        bot.send_message(message.chat.id, "Неправильное название факульета и группы! Повторите: ")
        res = Parser.search_by_group_if_nothing_found(name_group)
        if res !=None:
            bot.send_message(message.chat.id,f'Возможно это ваша группа- {res[0]}')
        bot.register_next_step_handler(message, get_name_gruop)
    else:
        client_mysql.post_id(message.from_user.id, id_group)
        start(message)
        #bot.register_next_step_handler(message, start)


@bot.message_handler(content_types='text')
def callback_inline(message):
    if message.text == 'на 3 дня':
        now = datetime.datetime.now()
        n = datetime.date.today() + datetime.timedelta(days=2)
        a = responce.get_schedule(f'{now.day}-{now.month}-{now.year}', f'{n.day}-{n.month}-{n.year}',
                                  str(client_mysql.get_id(int(message.from_user.id))))
        bot.send_message(chat_id=message.chat.id, text=a)

    elif message.text == 'Сегодня':

        now = datetime.datetime.now()
        a = responce.get_schedule(f'{now.day}-{now.month}-{now.year}', f'{now.day}-{now.month}-{now.year}',
                                  str(client_mysql.get_id(int(message.from_user.id))))
        bot.send_message(chat_id=message.chat.id, text=a)

    elif message.text == 'Завтра':
        now = datetime.datetime.now()
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        now = now.today()
        a = responce.get_schedule(f'{tomorrow.day}-{tomorrow.month}-{tomorrow.year}',
                                  f'{tomorrow.day}-{tomorrow.month}-{tomorrow.year}',
                                  str(client_mysql.get_id(int(message.from_user.id))))
        bot.send_message(chat_id=message.chat.id, text=a)

    elif message.text == 'вкл уведомления':
        client_mysql.post_notification(message.from_user.id, 1)
        markup_inline = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_inline.add(menu_items.item_yes, menu_items.item_no, menu_items.item_tomorrow,
                          menu_items.item_notification_off)
        bot.send_message(message.chat.id, 'Уведомления включены', reply_markup=markup_inline)

    elif message.text == 'выкл уведомления':
        client_mysql.post_notification(message.from_user.id, 0)
        markup_inline = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_inline.add(menu_items.item_yes, menu_items.item_no, menu_items.item_tomorrow,
                          menu_items.item_notification_on)
        bot.send_message(message.chat.id, 'Уведомления выключены ', reply_markup=markup_inline)





def function_to_run():
    chatid = client_mysql.get_all_on_notifaction()
    for id in chatid:
        now = datetime.datetime.now()
        a = responce.get_schedule(f'{now.day}-{now.month}-{now.year}', f'{now.day}-{now.month}-{now.year}', id[0])
        bot.send_message(id[0], a)



bot.polling(none_stop=True, interval=0)
