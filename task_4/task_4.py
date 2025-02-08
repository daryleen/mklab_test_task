# 4. Пользователь вводит две даты в формате ДД.ММ.ГГГГ ЧЧ:ММ.
# Вывести разницу между датами в часах, днях (целых), минутах и секундах.
import datetime

try:
    date1_input = input('Введите первую дату в формате ДД.ММ.ГГГГ ЧЧ:ММ: ')
    date2_input = input('Введите вторую дату в формате ДД.ММ.ГГГГ ЧЧ:ММ: ')
    date1_object = datetime.datetime.strptime(date1_input, '%d.%m.%Y %H:%M')
    date2_object = datetime.datetime.strptime(date2_input, '%d.%m.%Y %H:%M')
    delta = date2_object - date1_object
    days, secs = abs(delta.days), delta.seconds
    hours = secs // 3600
    mins = (secs // 60) % 60
    print(f'Разница: {days} дней, {hours} часов, {mins} минут, {secs % 60} секунд.')
except ValueError:
    print('Неверный формат даты!')