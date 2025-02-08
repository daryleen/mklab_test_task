# 5. Пользователь вводит две даты в формате ДД.ММ.ГГГГ ЧЧ:ММ. Пользователь вводит третью дату в формате
# ДД.ММ.ГГГГ ЧЧ:ММ. Определить, лежит ли дата внутри временного интервала, образованного первыми двумя датами.
import datetime

try:
    date1_input = input('Введите первую дату (начало) в формате ДД.ММ.ГГГГ ЧЧ:ММ: ')
    date2_input = input('Введите вторую дату (конец) в формате ДД.ММ.ГГГГ ЧЧ:ММ: ')
    date3_input = input('Введите третью дату в формате ДД.ММ.ГГГГ ЧЧ:ММ: ')
    date1_object = datetime.datetime.strptime(date1_input, '%d.%m.%Y %H:%M')
    date2_object = datetime.datetime.strptime(date2_input, '%d.%m.%Y %H:%M')
    date3_object = datetime.datetime.strptime(date3_input, '%d.%m.%Y %H:%M')
    if date1_object <= date3_object <= date2_object:
        print('Дата находится внутри интервала.')
    else:
        print('Дата не находится внутри интервала.')
except ValueError:
    print('Неверный формат даты!')