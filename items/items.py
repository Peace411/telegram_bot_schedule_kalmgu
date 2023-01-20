import telebot


class MenuItems():
    item_yes = telebot.types.InlineKeyboardButton(text='на 3 дня', )#callback_data='расписание')
    item_no = telebot.types.InlineKeyboardButton(text='Сегодня')#, callback_data='Сегодня')
    item_tomorrow = telebot.types.InlineKeyboardButton(text='Завтра')#, callback_data='Завтра')
    item_notification_on = telebot.types.InlineKeyboardButton(text='вкл уведомления')#,callback_data='not_on')
    item_notification_off = telebot.types.InlineKeyboardButton(text='выкл уведомления')#,callback_data='not_off')


