import logging

from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, executor, types
from aiogram.bot.api import TelegramAPIServer
from aiogram.types import ContentType

import buttoms as nav

#import mysql.connector


API_TOKEN = '2128273636:AAGQWY2z9O1pe2sBFCMDVf_qHLP_3UHKPeQ'
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# user_data = {}

# class User:
#     def __init__(self, first_name):
#         self.first_name = first_name
#         self.last_name = ''


# db = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     passwd = '2002',
#     port = '3306',
#     database = 'tgbot'
# )

# cursor = db.cursor()

#cursor.execute("CREATE DATABASE tgbot")
#cursor.execute("CREATE TABLE users (first_name VARCHAR(255), last_name VARCHAR(255))")
#cursor.execute("ALTER TABLE users ADD COLUMN (id INT AUTO_INCREMENT PRIMARY KEY, user_id INT UNIQUE)")

# sql = "INSERT INTO users (first_name, last_name, user_id) VALUES (%s, %s, %s)"
# val = ("Anna", "Borisyuk", 1)
# cursor.execute(sql, val)
# db.commit()

# print(cursor.rowcount, "Пользователь зарегистрован.")



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_sticker(message.from_user.id, 'https://cdn.tlgrm.app/stickers/110/fa7/110fa78e-0ff1-3ef2-aae6-322248b5cfe5/192/7.webp')
    await bot.send_message(message.from_user.id, 'Здравствуйте!\nЯ помогу Вам записаться к врачу\nПожалуйста, выберете услугу', reply_markup=nav.mainMenu)

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await bot.send_sticker(message.from_user.id, 'https://cdn.tlgrm.app/stickers/110/fa7/110fa78e-0ff1-3ef2-aae6-322248b5cfe5/192/10.webp')
    await bot.send_message(message.from_user.id, "Пожалуйста опишите свою проблему\n")

@dp.message_handler(commands=['data'])
async def cmd_data(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Отправить геолокацию", request_location=True))
    keyboard.add(types.KeyboardButton(text="Отправить контакт", request_contact=True))
    await message.answer("Выберите действие:", reply_markup=keyboard)



# @dp.message_handler(commands=['registration'])
# async def send_welcome(message: types.Message):
#     msg = bot.sent_message(message.chat.id, 'Введите свое имя')
#     bot.register_next_step_handler(msg, process_firstname_step)

# async def process_firstname_step(message: types.Message):
#     try:
#         user_id = message.from_user.id
#         user_data[user_id] = User(message.text)

#         msg = bot.sent_message(message.chat.id, 'Введите свою фамилию')
#         bot.register_next_step_hander(msg, process_lastname_step)
#     except Exception as e:
#         bot.sent_message(message.chat.id, 'Ошибка в регистрации, повторите еще раз')

# async def process_lastname_step(message: types.Message):
#     try: 
#         user_id = message.from_user.id
#         user = user_data[user_id]
#         user.last_name = message.text

#         sql = "INSERT INTO users (first_name, last_name, user_id) VALUES (%s, %s, %s)"
#         val = (user.first_name, user.last_name, user_id)
#         cursor.execute(sql, val)
#         db.commit()

#         bot.sent_message(message.chat.id, 'Вы успешно зарегистрированы')
#     except Exception as e:
#         bot.sent_message(message.chat.id, 'Ошибка в регистрации, или Вы уже зарегестрированы')


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == 'Главное меню⏪':
        await bot.send_message(message.from_user.id, 'Пожалуйста, выберете услугу', reply_markup=nav.mainMenu)
    elif message.text == 'Запись на прием👩🏽‍⚕️':
        await bot.send_message(message.from_user.id, 'Выберете специализацию врача:', reply_markup=nav.recMenu)
    elif message.text == 'Исследование📝':
        await bot.send_message(message.from_user.id, 'У Вас есть направление?', reply_markup=nav.analMenu)
    elif message.text == 'COVID19🦠':
        await bot.send_message(message.from_user.id, 'На данный момент в городе высокий уровень заболеваемости, берегите себя!\nКакую услугу, связанную с коронавирусом, Вы хотите получить?', reply_markup=nav.covMenu)
    elif message.text == 'Экстренная помощь🚑':
        await bot.send_sticker(message.from_user.id, 'https://cdn.tlgrm.app/stickers/110/fa7/110fa78e-0ff1-3ef2-aae6-322248b5cfe5/192/10.webp')
        await bot.send_message(message.from_user.id, 'Не паникуйте!\nВы можете позвонить по номеру: 103\nИли описать нам свою проблему и адрес(выберете кнопку "Горячая линия"), Ваше сообщение сразу отправится в ближайшую больницу!', reply_markup=nav.emergMenu) 
    
    #Код Карины
    elif message.text == 'Терапевт' :
        await bot.send_message(message.from_user.id, 'Вы выбрали терапевта. Выберете время записи к врачу:',
                               reply_markup=nav.timeTerMenu)
    elif message.text == 'Хирург' :
        await bot.send_message(message.from_user.id, 'Вы выбрали хирурка. Выберете время записи к врачу:',
                               reply_markup=nav.timeSurgMenu)
    elif message.text == 'Гинеколог':
        await bot.send_message(message.from_user.id, 'Вы выбрали гинеколога. Выберете время записи к врачу:',
                               reply_markup=nav.timeGynMenu)
    elif message.text == 'Оториноларинголог (ЛОР)':
        await bot.send_message(message.from_user.id, 'Вы выбрали оториноларинголога. Выберете время записи к врачу:',
                               reply_markup=nav.timeLorMenu)
    
    else:
        await message.reply('Извините, я Вас не поняла, попробуйте еще раз задать свой вопрос')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)