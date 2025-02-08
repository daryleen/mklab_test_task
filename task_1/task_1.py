# 1. Посчитайте сумму всех четных и нечетных чисел в интервале от 100 до 1000.

odd_sum, even_sum = 0, 0
for i in range(100, 1000):
    if i % 2 == 0:
        even_sum += 1
    else:
        odd_sum += 1
print(f'Сумма четных: {even_sum}\nСумма нечетных: {odd_sum}')
