import random
shethik = 0
spisok = []
randoms = [random.randint(0, 100) for x in range(1000)]
spisok_len = len(randoms)
max_spisok = max(randoms)
min_spisok = min(randoms)
randoms.sort()
print("Весь список:", randoms)
print("Длина списка:", spisok_len)
print("Максимальное число:", max_spisok)
print("Минимальное число:", min_spisok)
print("Прямой")
for i in range(0, 1000, 25):
    print(randoms[i:i+25])
print("Обратный")
for i in range(-1, -1001, -25):
    print(randoms[i:i-25:-1])

for i in randoms:
    if i == 6 or i == 13 or i == 66:
        shethik += 1
    else:
        spisok.append(i)
print("Кол-во удаленых элементов:", shethik)