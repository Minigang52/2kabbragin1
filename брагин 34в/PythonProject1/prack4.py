matrihs = [

    [ 1, 2, 3],
    [ 4, 5, 6],
    [ 7, 8, 9]

]
summa = [sum(row) for row in matrihs]

for i, summa in enumerate(summa):
    print(f"Сумма строк {i+1}:{summa}")