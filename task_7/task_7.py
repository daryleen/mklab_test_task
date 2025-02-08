# Из задачи 6 постройте два списка идентификаторов товаров так, чтобы в каждом не было повторений.
import math

orders = [['Товар1', 1, 500], ['Товар2', 7, 1000], ['Товар1', 6, 900], ['Товар3', 2, 1200], ['Товар2', 3, 1500]]

unique_products = set()

for product, quantity, price in orders:
    unique_products.add(product)
unique_products = sorted(list(unique_products))
products_amount = len(unique_products)
list1_size = math.ceil(products_amount / 2) # Размер списка: деление пополам с округлением вверх
product_list_1 = unique_products[:list1_size]
product_list_2 = unique_products[list1_size:]
print(f'Уникальный список 1: {product_list_1}\nУникальный список 2: {product_list_2}')
