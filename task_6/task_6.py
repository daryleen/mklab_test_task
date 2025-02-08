# 6. На входе многомерный список, каждый элемент содержит информацию о товаре, количестве и цене,
# которые были в каком-то заказе. Например: [[Товар1, 1,500], [Товар2, 7,1000],[Товар1, 6,900]].
# Вывести словарь: {Товар:Общая сумма заказа}.

orders = [['Товар1', 1, 500], ['Товар2', 7, 1000], ['Товар1', 6, 900]]
order_summary = {}
for product, quantity, price in orders:
    total_cost = quantity * price
    if product in order_summary:
        order_summary[product] += total_cost
    else:
        order_summary[product] = total_cost
print(order_summary)