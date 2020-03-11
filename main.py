import telebot
import config
from telebot import types

bot = telebot.AsyncTeleBot(config.TOKEN)

#Обрабатываем старт
@bot.message_handler(commands=["start"])
def welcome(message):
    #cоздаем инлайновые кнопки
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("🤩Раздеть", callback_data='photo')
    item2 = types.InlineKeyboardButton("🗄Баланс", callback_data='balance')
    item3 = types.InlineKeyboardButton("🎁Бесплатные монеты", callback_data='free')
    item4 = types.InlineKeyboardButton("Улучшить результат", callback_data='result')

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id,'✋<b>Добро пожаловать</b>, {0.first_name}!\n Я помогу тебе раздеть любую девушку \n\n Выбери действие'.format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)


#обработчик кнопок
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            #Обрабатываем кнопку "раздеть"
            if call.data == 'photo':
                #Это удаляет предыдущее сообщение, дальше там везде это есть
                bot.delete_message(call.message.chat.id, call.message.message_id)

                #кнопка назад
                markup = types.InlineKeyboardMarkup(row_width=1)
                back = types.InlineKeyboardButton("⬅️Назад", callback_data='back')
                markup.add(back)

                bot.send_message(call.message.chat.id, '🔔Раздеваю...'.format(call.message.from_user, bot.get_me()),
                    parse_mode='html', reply_markup=markup)

            ################################################################################
            #ТУТ ДОЛЖНА БЫТЬ НЕЙРОНКА И ВСЕ ЕЕ ВЫТЕКАЮЩИЕ
            ################################################################################

            #Обрабатываем кнопку"баланс"
            elif call.data == 'balance':

                bot.delete_message(call.message.chat.id, call.message.message_id)

                markup = types.InlineKeyboardMarkup(row_width=1)
                back = types.InlineKeyboardButton("⬅️Назад", callback_data ='back')
                pay = types.InlineKeyboardButton("Пополнить баланс", callback_data = "pay")
                markup.add(pay , back)

                bot.send_message(call.message.chat.id, '🔔Вы выбрали баланс'.format(call.message.from_user, bot.get_me()),
                    parse_mode='html', reply_markup=markup)

            #Обрабатываем кнопку "бесплатные монеты"
            elif call.data == "free":

                bot.delete_message(call.message.chat.id, call.message.message_id)

                markup = types.InlineKeyboardMarkup(row_width=1)
                back = types.InlineKeyboardButton("⬅️Назад", callback_data ='back')
                markup.add(back)

                bot.send_message(call.message.chat.id, 'За подписку на эти каналы вы получите 2 премиум монеты'.format(call.message.from_user, bot.get_me()),
                    parse_mode='html', reply_markup=markup)

            #Обрабатываем кнопку улучшить результат
            elif call.data == "result":

                bot.delete_message(call.message.chat.id, call.message.message_id)

                #кнопка назад
                markup = types.InlineKeyboardMarkup(row_width=1)
                back = types.InlineKeyboardButton("⬅️Назад", callback_data='back')
                markup.add(back)

                bot.send_message(call.message.chat.id, "Скоро".format(call.message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

            #Обарбатываем кнопку "назад"
            elif call.data == "back":

                bot.delete_message(call.message.chat.id, call.message.message_id)

                #cоздаем инлайновые кнопки
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("🤩Раздеть", callback_data='photo')
                item2 = types.InlineKeyboardButton("🗄Баланс", callback_data='balance')
                item3 = types.InlineKeyboardButton("🎁Бесплатные монеты", callback_data='free')
                item4 = types.InlineKeyboardButton("Улучшить результат", callback_data='result')

                markup.add(item1, item2, item3, item4)

                bot.send_message(call.message.chat.id,'✋<b>Добро пожаловать</b>, {0.first_name}!\n Я помогу тебе раздеть любую девушку \n\n Выбери действие'.format(call.message.from_user, bot.get_me()),
                    parse_mode='html', reply_markup=markup)

            #Обрабатываем кнопку "Пополнить баланс"
            elif call.data == "pay":

                bot.delete_message(call.message.chat.id, call.message.message_id)
                #Создаем кнопки сбербанк и киви
                markup = types.InlineKeyboardMarkup(row_width=2)
                sber = types.InlineKeyboardButton("Сбербанк", callback_data='sber')
                qiwi = types.InlineKeyboardButton("QIWI", callback_data = "qiwi")
                markup.add(sber, qiwi)

                bot.send_message(call.message.chat.id, "Выберите способ оплаты".format(call.message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

            #Обрабатываем кнопку сбербанк
            elif call.data == "sber":

                bot.delete_message(call.message.chat.id, call.message.message_id)

                markup = types.InlineKeyboardMarkup(row_width=1)
                agree = types.InlineKeyboardButton("Согласен", callback_data='agree_sber')
                back = types.InlineKeyboardButton("⬅️Назад", callback_data='back')
                markup.add(agree, back)

                bot.send_message(call.message.chat.id, "Вы выбрали <b>Сбербанк</b>\n*️⃣Сумма перевода: ... руб. \n💳Номер карты: ... 9943\n<code>Пожалуйста, переводите точную сумму, иначе платеж не засчитается.</code>".format(call.message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

            #Обрабатываем кнопку "qiwi"
            elif call.data == "qiwi":

                bot.delete_message(call.message.chat.id, call.message.message_id)
                #Создаем кнопку согласен и назад
                markup = types.InlineKeyboardMarkup(row_width=1)
                agree = types.InlineKeyboardButton("Согласен", callback_data='agree_qiwi')
                back = types.InlineKeyboardButton("⬅️Назад", callback_data='back')
                markup.add(agree, back)

                bot.send_message(call.message.chat.id, "Вы выбрали <b>Qiwi</b>\n*️⃣Сумма перевода: ... руб. \n💳Номер: +7...\n<code>Пожалуйста, переводите точную сумму, иначе платеж не засчитается.</code>".format(call.message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

            #Обрабатываем согласен у сбера
            elif call.data == "agree_sber":

                #Удаляем кнопку согласен
                bot.edit_message_reply_markup(chat_id= call.message.chat.id ,message_id= call.message.message_id ,inline_message_id = None ,reply_markup = None )

                #Тут будет парсер работать

            #Обрабатываем согласен у qiwi
            elif call.data == "agree_qiwi":

                    #Удаляем кнопку согласен
                    bot.edit_message_reply_markup(chat_id= call.message.chat.id ,message_id= call.message.message_id ,inline_message_id = None ,reply_markup = None )

                    #Тут будет парсер работать
    except Exception as e:
        print(repr(e))
#RUN
bot.polling(none_stop=True)
