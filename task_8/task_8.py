# 8. Из задачи 7 доработайте списки так, чтобы в каждом из двух списков были элементы из другого.
# Переведите списки в множества. Возьмите объединение и пересечение.
import math

orders = [['Товар1', 1, 500], ['Товар2', 7, 1000], ['Товар3', 2, 300], ['Товар1', 6, 900],
          ['Товар4', 1, 200], ['Товар5', 1, 100], ['Товар6', 2, 500]]

unique_products = set()

for product, quantity, price in orders:
    unique_products.add(product)
unique_products = sorted(list(unique_products))
products_amount = len(unique_products)
list1_size = math.ceil(products_amount / 2) # Размер списка: деление пополам с округлением вверх
product_list_1 = unique_products[:list1_size]
product_list_2 = unique_products[list1_size:]

# Обмениваемся нулевыми товарами, если списки не пустые
if product_list_1 and product_list_2:
    product_list_1.append(product_list_2[0])
    product_list_2.append(product_list_1[0])

# Преобразуем списки во множества
set_1 = set(product_list_1)
set_2 = set(product_list_2)

# Находим объединение
set_union = set_1.union(set_2)

# Находим пересечение
set_intersection = set_1.intersection(set_2)

print(f'Уникальный список 1: {product_list_1}\nУникальный список 2: {product_list_2}')
print(f'Объединение: {sorted(set_union)}\nПересечение: {sorted(set_intersection)}')