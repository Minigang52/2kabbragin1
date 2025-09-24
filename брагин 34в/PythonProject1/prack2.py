spisok_stud = []
def average_stud(spisok_stud):
    if not spisok_stud:
        return 0
    return sum(spisok_stud) / len(spisok_stud)
for i in range(10):
    spisok_input = int(input("Введите оценки студентов:"))
    if spisok_input > 5 or spisok_input == 0:
        print("Пожалуйста, введите корректное число.")
    else:
        grade = float(spisok_input)
        spisok_stud.append(grade)

average = average_stud(spisok_stud)
print(f"Средний балл: {average}")
