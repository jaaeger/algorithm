data_1 = int(input())
result = 0

for i in data_1:
    data_2 = int(input())
    if data_2 == 1 or data_2 == 4:
        result += 1
    elif data_2 == 3: # Так можно вечно писать условия, нужна какая-то функция для просчёта
        pass