"""Создайте простой калькулятор, который позволяет пользователю вводить два числа и
выполнять над ними основные арифметические операции (сложение, вычитание, умножение, деление)."""

def calculator():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    operation = input("Выберите операцию (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
        print(f"Результат: {num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"Результат: {num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"Результат: {num1} * {num2} = {result}")
    elif operation == '/':
        if num2 == 0:
            print("Ошибка: деление на ноль!")
        else:
            result = num1 / num2
            print(f"Результат: {num1} / {num2} = {result}")
    else:
        print("Некорректная операция. Пожалуйста, выберите из '+', '-', '*', '/'.")

calculator()