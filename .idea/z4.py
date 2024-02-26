#Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.

def convert_seconds(seconds):
    days = seconds // (24 * 3600)
    seconds %= (24 * 3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return f"{days}:{hours}:{minutes}:{seconds}"

total_seconds = int(input("Введите количество секунд: "))
result = convert_seconds(total_seconds)
print(result)