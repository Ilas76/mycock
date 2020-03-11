from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import random
import asyncio
import pickle
import qiwi

TOKEN = "1080043755:AAE_7UqPSA-2sBYIE_ipSp7nrX4Mu056jrs"

photo = InlineKeyboardButton("🤩Раздеть", callback_data='photo')
balance = InlineKeyboardButton("🗄Баланс", callback_data='balance')
subs = InlineKeyboardButton("🌐Подписка", callback_data='subs')
free = InlineKeyboardButton("🎁Бесплатные монеты", callback_data='free')

back = InlineKeyboardButton("⬅️Назад", callback_data='back')
menu = InlineKeyboardButton("⬅️В меню", callback_data='back')

repl = InlineKeyboardButton("Купить коины", callback_data='add')
ad_subs = InlineKeyboardButton("Купить подписку", callback_data='add_s')

sber = InlineKeyboardButton("Сбербанк", callback_data='sber')
qiwi = InlineKeyboardButton("QIWI", callback_data='qiwi')

sber_s = InlineKeyboardButton("Сбербанк", callback_data='sber_s')
qiwi_s = InlineKeyboardButton("QIWI", callback_data='qiwi_s')

sub_1 = InlineKeyboardButton("На неделю", callback_data='sub1')
sub_2 = InlineKeyboardButton("На месяц", callback_data='sub2')
sub_3 = InlineKeyboardButton("На 2 месяца", callback_data='sub3')
sub_4 = InlineKeyboardButton("На 6 месяцев", callback_data='sub4')

agree_coins = InlineKeyboardButton("Согласен", callback_data='agree_coins')
agree_subs = InlineKeyboardButton("Согласен", callback_data='agree_subs')

#126c962c6eaf147aae085d416ae44366

def randls():
    a = random.random()
    b = float("{0:.2f}".format(a))
    return b

def chek_sber(value):
    with open("value.txt" , 'rb') as f:
        sum = pickle.load(f)
    for i in sum:
        if i == value:
            return True
    return False

def string(call):
    string =str("id/") + str(int(call["id"])) + str(".txt")
    with open(string , 'rb') as f:
        id = pickle.load(f)
    sum = id[1]
    return sum

def coins(call):
    string =str("id/") + str(int(call["id"])) + str(".txt")
    with open(string , 'rb') as f:
        id = pickle.load(f)
    sum = id[0]
    return sum

def this_sub_a(data, string):
    if data == "sub1":
        a = float(110) + randls() - 5
        mass = [1,a]
        subb = "на неделю"
        with open(string , 'wb') as f:
                pickle.dump(mass, f)
        return a
    elif data == "sub2":
        a = float(320) + randls() - 5
        mass = [2,a]
        subb = "на месяц"
        with open(string , 'wb') as f:
                pickle.dump(mass, f)
        return a
    elif data == "sub3":
        a = float(499) + randls() - 5
        mass = [3,a]
        subb = "на 2 месяца"
        with open(string , 'wb') as f:
                pickle.dump(mass, f)
        return a
    elif data == "sub4":
        a = float(1199) + randls() - 5
        mass = [4,a]
        subb = "на 6 месяцев"
        with open(string , 'wb') as f:
                pickle.dump(mass, f)
        return a

def this_sub_subb(data, string):
    if data == "sub1":
        a = float(110) + randls() - 5
        mass = [1,a]
        subb = "на неделю"
        with open(string , 'wb') as f:
                pickle.dump(mass, f)
        return subb
    elif data == "sub2":
        a = float(320) + randls() - 5
        mass = [2,a]
        subb = "на месяц"
        with open(string , 'wb') as f:
                pickle.dump(mass, f)
        return subb
    elif data == "sub3":
        a = float(499) + randls() - 5
        mass = [3,a]
        subb = "на 2 месяца"
        with open(string , 'wb') as f:
                pickle.dump(mass, f)
        return subb
    elif data == "sub4":
        a = float(1199) + randls() - 5
        mass = [4,a]
        subb = "на 6 месяцев"
        with open(string , 'wb') as f:
                pickle.dump(mass, f)
        return subb

def subs_sum(string):
    with open(string , 'rb') as f:
        id = pickle.load(f)
    sum = id[1]
    return sum

def subs_type(string):
    with open(string , 'rb') as f:
        id = pickle.load(f)
    sum = id[0]
    return sum

def check_photo(name):
    try:
        photo = open(name, 'rb')
        return True
    except Exception:
        return False
