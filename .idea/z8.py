'''Создайте программу, которая генерирует случайное число
в определенном диапазоне и выводит его на экран.'''

import random

min_value = int(input("Введите минимальное значение диапазона: "))
max_value = int(input("Введите максимальное значение диапазона: "))

random_number = random.randint(min_value, max_value)

print(f"Случайное число в диапазоне от {min_value} до {max_value}: {random_number}")