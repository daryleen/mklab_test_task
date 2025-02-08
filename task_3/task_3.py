# 3. Пользователь вводит дату и время в формате ДД.ММ.ГГГГ ЧЧ:ММ. Обрежьте секунды. Замените час на 10.
import datetime

try:
    date_input = input('Введите дату в формате ДД.ММ.ГГГГ ЧЧ:ММ: ')
    date_object = datetime.datetime.strptime(date_input, '%d.%m.%Y %H:%M')
    new_date = date_object.replace(hour=10).strftime('%d.%m.%Y %H:%M')
    print(f'Новая дата: {new_date}')
except ValueError:
    print('Неверный формат даты!')