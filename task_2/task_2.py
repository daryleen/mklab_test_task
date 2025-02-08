# 2. Пользователь вводит дату в формате ДД.ММ.ГГГГ. Вывести первый день месяца, последний день месяца, сам месяц.
import datetime

month_names = [
    'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
    'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
]

try:
    date_input = input('Введите дату в формате ДД.ММ.ГГГГ: ')
    date_object = datetime.datetime.strptime(date_input, '%d.%m.%Y')
    first_day = date_object.replace(day=1)
    next_month = date_object.replace(day=28) + datetime.timedelta(days=4)
    last_day = next_month - datetime.timedelta(days=next_month.day)
    month = month_names[date_object.month - 1]
    print(f'Первый день месяца: {first_day.day}\nПоследний день месяца: {last_day.day}\nМесяц: {month}')
except ValueError:
    print('Неверный формат даты!')
