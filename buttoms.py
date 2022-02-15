from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('Главное меню⏪')
btnRec = KeyboardButton('Назад к выбору врача')

#main menu
btnRec = KeyboardButton('Запись на прием👩🏽‍⚕️')
btnAnal = KeyboardButton('Исследование📝')
btnCOV = KeyboardButton('COVID19🦠')
btnEmer = KeyboardButton('Экстренная помощь🚑')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRec, btnAnal, btnCOV, btnEmer)

#Reception Menu
btnTerap = KeyboardButton('Терапевт')
btnSurg = KeyboardButton('Хирург')
btnGynec = KeyboardButton('Гинеколог')
btnLOR = KeyboardButton('Оториноларинголог (ЛОР)')
recMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnTerap, btnSurg, btnGynec, btnLOR, btnMain)

#Analysus Menu
btnYes = KeyboardButton('Да')
btnNo = KeyboardButton('Нет')
analMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnYes, btnNo, btnMain)

#COVID Menu
btnPCR = KeyboardButton('Запись на мазок(ПЦР)')
btnAntib = KeyboardButton('Запись на кровь(антитела)')
btnVakc = KeyboardButton('Запись на вакцинацию')
covMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnPCR, btnAntib, btnVakc, btnMain)

#Emergency Menu
btnEMess = KeyboardButton('Горячая линия')
emergMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnEMess, btnMain)

#Код Карины
#Therapist Menu
btnTimeTer1 =  KeyboardButton('11:20')
btnTimeTer2 =  KeyboardButton('12:20')
btnTimeTer3 =  KeyboardButton('14:20')
btnTimeTer4 =  KeyboardButton('15:20')
timeTerMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnTimeTer1, btnTimeTer2, btnTimeTer3, btnTimeTer4, btnMain)

#Surgeon Menu
btnTimeSurg1 =  KeyboardButton('14:20')
btnTimeSurg2 =  KeyboardButton('16:20')
btnTimeSurg3 =  KeyboardButton('18:20')
btnTimeSurg4 =  KeyboardButton('19:20')
timeSurgMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnTimeSurg1, btnTimeSurg2, btnTimeSurg3, btnTimeSurg4, btnMain)

#Gynecologist Menu
btnTimeGyn1 =  KeyboardButton('8:20')
btnTimeGyn2 =  KeyboardButton('9:20')
btnTimeGyn3 =  KeyboardButton('12:20')
btnTimeGyn4 =  KeyboardButton('15:20')
timeGynMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnTimeGyn1, btnTimeGyn2, btnTimeGyn3, btnTimeGyn4, btnMain)

#LOR Menu
btnTimeLor1 =  KeyboardButton('11:20')
btnTimeLor2 =  KeyboardButton('12:20')
btnTimeLor3 =  KeyboardButton('14:20')
btnTimeLor4 =  KeyboardButton('15:20')
timeLorMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnTimeLor1, btnTimeLor2, btnTimeLor3, btnTimeLor4, btnMain)