import logging
from aiogram import filters
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import asyncio
import time
import aiohttp
import config
from utils import TestStates
import pickle
import os
import io
from PIL import Image
import module1
import returnimg
import deep
import subprocess

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=config.TOKEN)
#dp = Dispatcher(bot)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


#ОБрабатваем комманду /start
@dp.message_handler(state="*", commands=['start'])
async def welcome(message: types.Message):
    #Сбрасываем состояние
    state = dp.current_state(chat=message.chat.id, user=message.from_user.id)
    await state.reset_state()

    #Добавляем кнопки
    inline = InlineKeyboardMarkup(row_width=1).add(config.photo, config.balance, config.subs, config.free)

    await bot.send_message(message.from_user.id, '✋<b>Добро пожаловать</b>, {0.first_name}!\nТут ты можешь раздеть любую девушку😈\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nИнформация об аккаунте:\n\n<b>Коины:</b> ... \n<b>Подписка:</b> ... \n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n🗣 <b>Каждому новому клтенту мы дарим 2 коина.</b>\n\n🛠 Наша техподдержка: @godofpussies \n🏵 Наш телеграм канал: ... \n\n<i><b>Просто нажми кнопку "Раздеть" и получай удовольствие</b></i>'.format(message.from_user, bot.get_me()),parse_mode ='html', reply_markup = inline)
    module1.Sql.start(message.from_user.first_name,message.chat.id,'false','2','false')



@dp.message_handler(content_types=["photo"])
async def audio_handler(message: types.Message):

    #Сохранем Фотку
    chatid = message.chat.id
    str_id = str(chatid)
    await message.photo[-1].download(str_id+ ".jpg")

    #Обработаем фото
    returnimg.result(str_id + ".jpg", str_id + "inp.png")
    os.remove(str_id + ".jpg")

    #пихаем в нейронку
    # Тут нужно sql, если есть подписка или коины то выполняется этот код
    cmd = 'python deep.py --input="%s" --output="%s"' %(str_id + "inp.png", str_id + "result.png")
    subprocess.Popen(cmd, shell = True)
    await asyncio.sleep(3)
    os.remove(str_id + "inp.png")

    i = 0
    while i < 30:
        if config.check_photo(str_id + "result.png") == False:
            await asyncio.sleep(10)
            i += 0.5
        elif config.check_photo(str_id + "result.png") == True:
            photo = open(str(str_id + "result.png"), 'rb')
            await bot.send_photo(message.from_user.id, photo)
            await bot.send_message(message.from_user.id,("❕<b><i>Для входа в меню нажмите /start</i></b>"),parse_mode ='html')
            i = 60
            os.remove(str_id + "result.png")

    #Если нет подписи ил коинов то этот
    """await bot.send_message(message.from_user.id,("❕<b><i>У вас нет коинов или подписки, поэтому обработка фотографии будет выполняться в режиме очереди.</i></b>"),parse_mode ='html')
    await asyncio.sleep(1200)
    cmd = 'python deep.py --input="%s" --output="%s"' %(str_id + "inp.png", str_id + "result.png")
    subprocess.Popen(cmd, shell = True)
    await asyncio.sleep(3)
    os.remove(str_id + "inp.png")

    i = 0
    while i < 30:
        if config.check_photo(str_id + "result.png") == False:
            await asyncio.sleep(10)
            i += 0.5
        elif config.check_photo(str_id + "result.png") == True:
            photo = open(str(str_id + "result.png"), 'rb')
            await bot.send_photo(message.from_user.id, photo)
            i = 60
            os.remove(str_id + "result.png")"""

#Обработчик числа коинов которые вводят пользователи

#---------------------------------Тут пизда нэ смотреть-----------------------------------#
@dp.message_handler(state=TestStates.TEST_STATE_1)
async def msg_handler(message: types.Message):
    try:
        #Проверка на целое число
        sum = int(message.text)
        string = str("id/") + str(int(message.from_user["id"])) + str(".txt")
        mass = [sum]
        if (sum < 30):
            ran = float(sum*5) + config.randls() - 1
            mass.append(ran)
            with open(string , 'wb') as f:
                    pickle.dump(mass, f)

            inline = InlineKeyboardMarkup(row_width=1).add(config.sber,config.back)
            await bot.send_message(message.from_user.id,("🤖Вы хотите купить <b>%i</b> коинов. \n📈Стоимость:  <b>%.2f</b> рублей \n\n🔽<i>Выберете способ оплаты</i>" %(sum, ran)),parse_mode ='html', reply_markup = inline)

            #Удалим файл
            await asyncio.sleep(1800)
            os.remove(string)

        elif (sum > 29) and (sum < 70):
            ran = float(sum*3.3) + config.randls() - 1
            mass.append(ran)
            with open(string , 'wb') as f:
                    pickle.dump(mass, f)

            inline = InlineKeyboardMarkup(row_width=1).add(config.sber,config.back)
            await bot.send_message(message.from_user.id,("🤖Вы хотите купить <b>%i</b> коинов. \n📈Стоимость:  <b>%.2f</b> рублей \n\n🔽<i>Выберете способ оплаты</i>" %(sum, ran)),parse_mode ='html', reply_markup = inline)
            #Удалим файл
            await asyncio.sleep(1800)
            os.remove(string)

        elif (sum > 69) and (sum < 120):
            ran = float(sum*2.8) + config.randls() - 1
            mass.append(ran)
            with open(string , 'wb') as f:
                    pickle.dump(mass, f)

            inline = InlineKeyboardMarkup(row_width=1).add(config.sber,config.back)
            await bot.send_message(message.from_user.id,("🤖Вы хотите купить <b>%i</b> коинов. \n📈Стоимость:  <b>%.2f</b> рублей \n\n🔽<i>Выберете способ оплаты</i>" %(sum, ran)),parse_mode ='html', reply_markup = inline)
            #Удалим файл
            await asyncio.sleep(1800)
            os.remove(string)

        elif (sum > 119) and (sum < 170):
            ran = float(sum*2.5) + config.randls() - 1
            mass.append(ran)
            with open(string , 'wb') as f:
                    pickle.dump(mass, f)

            inline = InlineKeyboardMarkup(row_width=1).add(config.sber,config.back)
            await bot.send_message(message.from_user.id,("🤖Вы хотите купить <b>%i</b> коинов. \n📈Стоимость:  <b>%.2f</b> рублей \n\n🔽<i>Выберете способ оплаты</i>" %(sum, ran)),parse_mode ='html', reply_markup = inline)
            #Удалим файл
            await asyncio.sleep(1800)
            os.remove(string)

        elif (sum > 169) and (sum < 230):
            ran = float(sum*2.3) + config.randls() - 1
            mass.append(ran)
            with open(string , 'wb') as f:
                    pickle.dump(mass, f)

            inline = InlineKeyboardMarkup(row_width=1).add(config.sber,config.back)
            await bot.send_message(message.from_user.id,("🤖Вы хотите купить <b>%i</b> коинов. \n📈Стоимость:  <b>%.2f</b> рублей \n\n🔽<i>Выберете способ оплаты</i>" %(sum, ran)),parse_mode ='html', reply_markup = inline)
            #Удалим файл
            await asyncio.sleep(1800)
            os.remove(string)

        elif (sum > 229) and (sum < 251):
            ran = float(sum*2.1) + config.randls() - 1
            mass.append(ran)
            with open(string , 'wb') as f:
                    pickle.dump(mass, f)

            inline = InlineKeyboardMarkup(row_width=1).add(config.sber,config.back)
            await bot.send_message(message.from_user.id,("🤖Вы хотите купить <b>%i</b> коинов. \n📈Стоимость:  <b>%.2f</b> рублей \n\n🔽<i>Выберете способ оплаты</i>" %(sum, ran)),parse_mode ='html', reply_markup = inline)
            #Удалим файл
            await asyncio.sleep(1800)
            os.remove(string)

        else:
            await bot.send_message(message.from_user.id,"❗️<b>Неверное знаечение, попробуйте еще раз</b>",parse_mode ='html')
    except Exception:
        await bot.send_message(message.from_user.id,"❗️<b>Неверное знаечение, попробуйте еще раз</b>",parse_mode ='html')
#-------------------------------------------------------------------------------------------------------#


#Тут нейронка
@dp.callback_query_handler(text = 'photo')
async def process_callback_button1(callback_query: types.CallbackQuery):

    #удаляем педыдущее сообщение
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

    await bot.send_message(callback_query.from_user.id, '📋 Условия качественного результата: \n\n1️⃣<b>Фотография девушки должна быть в купальнике или нижнем белье!</b> \n2️⃣<b>Девушка должна быть по центру фото , лицом и грудью к объективу!</b> \n\n <i>Для возвращения в меню нажмите</i> /start\n\n❕<b>А теперь просто пришли фото и получи результат.</b>',parse_mode ='html')

#Баланс
@dp.callback_query_handler(text = 'balance')
async def process_callback_button1(callback_query: types.CallbackQuery):

    #удаляем педыдущее сообщение
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    # По идеии должно так выглядеть и работать:
    info = module1.Sql.select(callback_query.message.message_id)
    coin = "456"#info[1]
    sub = "..."#info[0]
    #Добавим кнопки
    inline = InlineKeyboardMarkup(row_width=1).add(config.repl, config.back)
    await bot.send_message(callback_query.from_user.id, ('<i>Фотограии за коины обрабтываются вне очереди и без вводных знаков</i>\n\n🎲Информация о вашем аккаунте: \n\n<b>-Коинов:</b> %0.f \n<b>-Подписка:</b>  %s\n\n〽️Стоимость коинов:\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n<b>1 коин</b> - 5 рублей\n<b>30 коинов</b> - 100 рублей\n<b>70 коинов</b> - 200 рублей\n<b>120 коинов</b> - 300 рублей\n<b>170 коинов</b> - 400 рублей\n<b>230 коинов</b> - 500 рублей\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n🗣<b><i>Нажмите на кнопку "Купить коины" для пополнения</i></b>' %(coin , sub)),parse_mode ='html', reply_markup = inline)

#Кнопка "Купить коины"
@dp.callback_query_handler(text = 'add')
async def process_callback_button1(callback_query: types.CallbackQuery):

    #удаляем кнопки
    await bot.edit_message_reply_markup(chat_id= callback_query.message.chat.id ,message_id= callback_query.message.message_id ,inline_message_id = None ,reply_markup = None )

    #Меняем состояние
    state = dp.current_state(chat=callback_query.message.chat.id, user=callback_query.from_user.id)
    await state.set_state(TestStates.all()[1])

    await bot.send_message(callback_query.from_user.id, '📲<b>Введите сколько коинов вы хотите купить</b>\n<i>Для отмены /start</i>',parse_mode ='html')


#Обрабатываем сбербанк
@dp.callback_query_handler(state=TestStates.TEST_STATE_1, text = 'sber')
async def process_callback_button1(callback_query: types.CallbackQuery):

    #удаляем педыдущее сообщение
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

    #Сбрасываем состояние
    state = dp.current_state(chat=callback_query.message.chat.id, user=callback_query.from_user.id)
    await state.reset_state()

    #Выттащим сумму
    sum = config.string(callback_query.from_user)

    inline = InlineKeyboardMarkup(row_width=1).add(config.agree_coins, config.back)
    await bot.send_message(callback_query.from_user.id, ('💠Вы выбрали <b>Сбербанк</b> \n💳Карта: <b>0000 0000 0000 0000</b>\n\n<i>Нажмите кнопку <b>"Согласен"</b> и переведите на карту <b>%.2f рублей</b> в течении 30 минут. После поступления средств бот автоматически уведомит вас.</i> \n\n<code>Если бот не увидел платеж или возникли другие проблемы, просьба обращаться в техподдержку</code> - <b>@godofpussies</b>\n\n⬇️<b>Нажмите кнопку "Согласен"</b>⬇️' %sum) ,parse_mode ='html', reply_markup = inline)
    #await bot.send_message(callback_query.from_user.id, 'Вы выбрали <b>Сбербанк</b> \nКарта: <b>0000 0000 0000 0000</b>\n\n<i>Переведите на карту %2f рублей в течении 30 минут и нажмите кнопку <b>"Оплатил"</b>. Рекумендуем подождать 5 минут после перевода</i>',parse_mode ='html')


#Обрабатываем согласен у сбербанка для коинов
@dp.callback_query_handler(text = 'agree_coins')
async def process_callback_button1(callback_query: types.CallbackQuery):

    #удаляем кнопки
    await bot.edit_message_reply_markup(chat_id= callback_query.message.chat.id ,message_id= callback_query.message.message_id ,inline_message_id = None ,reply_markup = None )

    await bot.send_message(callback_query.from_user.id, ('<i>Для удаления заявки нажмите /start</i>') ,parse_mode ='html')
    #Выттащим сумму
    sum = float(config.string(callback_query.from_user))
    value = int(config.coins(callback_query.from_user))

    i = 0
    while i < 30:
        if config.chek_sber(sum) == True:
            #Тут надо занести в бд кол-во коинов, то есть переменную value
            inline = InlineKeyboardMarkup(row_width=1).add(config.menu)
            await bot.send_message(callback_query.from_user.id, ('🙌<b>Поздравляем!</b>\n<b>Ваш баланс успешно пополнен.</b>') ,parse_mode ='html', reply_markup = inline)
            #module1.Sql.update(callback_query.chat.id,value,'false','false')
            i = 60
        else:
            await asyncio.sleep(60)
            i+=1
    if i == 30:
        inline = InlineKeyboardMarkup(row_width=1).add(config.menu)
        await bot.send_message(callback_query.from_user.id, ('📍<b>Оплата не прошла</b>\n<i>Попробуйте еще раз или обратитесь в техподдержку - @godofpussies</i>') ,parse_mode ='html', reply_markup = inline)


#Подписки
@dp.callback_query_handler(text = 'subs')
async def process_callback_button1(callback_query: types.CallbackQuery):

    #удаляем педыдущее сообщение
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

    #Добавим кнопки
    inline = InlineKeyboardMarkup(row_width=1).add(config.ad_subs, config.back)
    await bot.send_message(callback_query.from_user.id, '🗂<i>Подписка имеет свои преимущества:</i>\n\n▫️ Без очереди.\n▫️ Без водяного знака.\n▫️ Без ограничений и лимитов.\n\n〽️<b>Стоимоть подписок:</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n<b>Подписка на неделю</b> - 110 рублей\n<b>Подписка на месяц</b> - 320 рублей\n<b>Подписка на 2 месяца</b> - 499 рублей\n<b>Подписка на 6 месяцев</b> - 1199 рублей\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n🗣<b>Нажмите кнопку "Купить подписку" для покупки.</b>',parse_mode ='html', reply_markup = inline)


#Бесплатные монеты
@dp.callback_query_handler(text = 'free')
async def process_callback_button1(callback_query: types.CallbackQuery):

    #удаляем педыдущее сообщение
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

    #Добавим кнопки
    inline = InlineKeyboardMarkup(row_width=1).add(config.back)
    await bot.send_message(callback_query.from_user.id, '📋 Условия',parse_mode ='html', reply_markup = inline)


#Кнопка назад
@dp.callback_query_handler(text = 'back')
async def process_callback_button1(callback_query: types.CallbackQuery):

    #удаляем педыдущее сообщение
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

    #Добавим кнопки
    inline = InlineKeyboardMarkup(row_width=1).add(config.photo, config.balance, config.subs, config.free)
    await bot.send_message(callback_query.from_user.id, '✋<b>Добро пожаловать</b>, {0.first_name}!\nТут ты можешь раздеть любую девушку😈\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nИнформация об аккаунте:\n\n<b>Коины:</b> ... \n<b>Подписка:</b> ... \n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n🗣 <b>Каждому новому клтенту мы дарим 2 коина.</b>\n\n🛠 Наша техподдержка: ... \n🏵 Наш телеграм канал: ... \n\n<i><b>Просто нажми кнопку "Раздеть" и получай удовольствие</b></i>'.format(callback_query.message.from_user, bot.get_me()),parse_mode ='html', reply_markup = inline)


#Купить подписку
@dp.callback_query_handler(text = 'add_s')
async def process_callback_button1(callback_query: types.CallbackQuery):

    #удаляем педыдущее сообщение
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

    #Добавим кнопки
    inline = InlineKeyboardMarkup(row_width=1).add(config.sub_1, config.sub_2, config.sub_3, config.sub_4, config.back)
    await bot.send_message(callback_query.from_user.id, '〽️<b>Стоимоть подписок:</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n<b>Подписка на неделю</b> - 110 рублей\n<b>Подписка на месяц</b> - 320 рублей\n<b>Подписка на 2 месяца</b> - 499 рублей\n<b>Подписка на 6 месяцев</b> - 1199 рублей\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n⬇️<b>Выберете подписку которую хотите купить</b>⬇️',parse_mode ='html', reply_markup = inline)


#Первая вторая третья и четвертая подписки
@dp.callback_query_handler(text = 'sub1')
@dp.callback_query_handler(text = 'sub2')
@dp.callback_query_handler(text = 'sub3')
@dp.callback_query_handler(text = 'sub4')
async def process_callback_button1(callback_query: types.CallbackQuery):
    data = callback_query.data
    string = str("id/") +str("sub")+ str(int(callback_query.from_user["id"])) + str(".txt")
    #удаляем педыдущее сообщение
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

    a = config.this_sub_a(data, string)
    subb = config.this_sub_subb(data, string)

    #Добавим кнопки
    inline = InlineKeyboardMarkup(row_width=1).add(config.sber_s,config.back)
    if (data == "sub1") or (data == "sub2") or (data == "sub3") or (data == "sub4"):
        await bot.send_message(callback_query.from_user.id, ('💠Вы выбрали <b>подписку %s</b>\n🔋Стоимость составит: <b>%.2f рублей</b>\n\n🔽<i>Выберете способ оплаты</i>🔽' %(subb, a)),parse_mode ='html', reply_markup = inline)

    await asyncio.sleep(1800)
    os.remove(string)


#Сбербанк у подписок
@dp.callback_query_handler(text = 'sber_s')
async def process_callback_button1(callback_query: types.CallbackQuery):
    string = str("id/") +str("sub")+ str(int(callback_query.from_user["id"])) + str(".txt")

    #удаляем педыдущее сообщение
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

    #Достаем сумму
    sum = config.subs_sum(string)

    inline = InlineKeyboardMarkup(row_width=1).add(config.agree_subs, config.back)
    await bot.send_message(callback_query.from_user.id, ('💠Вы выбрали <b>Сбербанк</b> \n💳Карта: <b>5469 6800 2884 9943</b>\n\n<i>Нажмите кнопку <b>"Согласен"</b> и переведите на карту <b>%.2f рублей</b> в течении 30 минут. После поступления средств бот автоматически уведомит вас.</i> \n\n<code>Если бот не увидел платеж или возникли другие проблемы, просьба обращаться в техподдержку</code> - <b>@godofpussies</b>\n\n⬇️<b>Нажмите кнопку "Согласен"</b>⬇️' %sum) ,parse_mode ='html', reply_markup = inline)


#Обрабатываем согласен у сбербанка для подписок
@dp.callback_query_handler(text = 'agree_subs')
async def process_callback_button1(callback_query: types.CallbackQuery):
    string = str("id/") +str("sub")+ str(int(callback_query.from_user["id"])) + str(".txt")

    #удаляем кнопки
    await bot.edit_message_reply_markup(chat_id= callback_query.message.chat.id ,message_id= callback_query.message.message_id ,inline_message_id = None ,reply_markup = None )

    await bot.send_message(callback_query.from_user.id, ('<i>Для удаления заявки нажмите /start</i>') ,parse_mode ='html')
    #Выттащим сумму
    sum = config.subs_sum(string)
    type = int(config.subs_type(string))

    i = 0
    while i < 1:
        if config.chek_sber(sum) == True:
            #Тут надо занести в бд полписку, то есть переменную type(если type = 1, то подписка на неделю, 2 - на месяц, 3 - на 2 месяца, 4 - на 6 месяцев)
            inline = InlineKeyboardMarkup(row_width=1).add(config.menu)
            await bot.send_message(callback_query.from_user.id, ('🙌<b>Поздравляем!</b>\n<b>Подписка успешно куплена.</b>') ,parse_mode ='html', reply_markup = inline)
            i = 60
        else:
            await asyncio.sleep(60)
            i+=1
    if i == 1:
        inline = InlineKeyboardMarkup(row_width=1).add(config.menu)
        await bot.send_message(callback_query.from_user.id, ('📍<b>Оплата не прошла</b>\n<i>Попробуйте еще раз или обратитесь в техподдержку - @godofpussies</i>') ,parse_mode ='html', reply_markup = inline)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
