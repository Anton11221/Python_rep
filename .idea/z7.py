"""Напишите программу, которая принимает на вход температуру в градусах
Цельсия и переводит ее в градусы Фаренгейта или наоборот,
в зависимости от выбора пользователя."""

def celsius_to_fahrenheit(celsius):
    fahrenheit = round((celsius * 9/5) + 32, 1)
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = round((fahrenheit - 32) * 5/9, 1)
    return celsius

choice = input("Выберите тип конвертации (C для Цельсия в Фаренгейты, F для Фаренгейтов в Цельсии): ")

if choice.upper() == 'C':
    celsius = float(input("Введите температуру в градусах Цельсия: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} градусов Цельсия = {fahrenheit} градусов Фаренгейта")
elif choice.upper() == 'F':
    fahrenheit = float(input("Введите температуру в градусах Фаренгейта: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} градусов Фаренгейта = {celsius} градусов Цельсия")
else:
    print("Некорректный выбор. Пожалуйста, введите 'C' или 'F'.")