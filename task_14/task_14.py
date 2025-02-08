#  14. Отсортируйте список из задачи 6 по: товару, по сумме в строке (количество*цену).
#  Используйте для сортировки лямда функцию.

orders = [['Товар1', 1, 500], ['Товар2', 7, 1000], ['Товар1', 6, 900]]
order_summary = {}
for product, quantity, price in orders:
    total_cost = quantity * price
    if product in order_summary:
        order_summary[product] += total_cost
    else:
        order_summary[product] = total_cost
print(order_summary)
# Преобразование в list
order_summary_list = list(order_summary.items())
# Сортировка по товару
order_summary_list.sort(key=lambda x: x[0])
print(f'Сортировка по товару:\n{order_summary_list}')
# Сортировка по сумме в строке (от большей к меньшей)
order_summary_list.sort(key=lambda x: x[1], reverse=True)
print(f'Сортировка по товару:\n{order_summary_list}')


