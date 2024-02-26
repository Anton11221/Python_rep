numbers = [10, 21, 34, 40, 237, 50, 60, 70, 80]

for num in numbers:
    if num == 237:
        print("Встречено число 237. Программа остановлена.")
        break
    elif num % 2 == 0:
        print(num)
