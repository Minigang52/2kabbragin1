filename = 'students.txt'

try:
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    students = []

    for line in lines:
        line = line.strip()
        if line:
            parts = line.split()
            if len(parts) == 2:
                surname, grade_str = parts
                try:
                    grade = float(grade_str)
                    students.append((surname, grade))
                except:
                    pass  #если оценка не число

    if students:
        avg = sum(s[1] for s in students) / len(students)
        print(f'Средний балл: {avg:.2f}')
        print('Студенты с оценками выше среднего:')

        for s in students:
            if s[1] > avg:
                print(s[0])
    else:
        print('Нет данных')
except:
    print('Не удалось открыть файл')

##############################################################################################################

from datetime import datetime

now = datetime.now()

timestamp = now.strftime("%m-%d %H:%M")

with open('log.txt', 'a', encoding='utf-8') as log_file:
    log_file.write(timestamp + '\n')

print('Запись выполнена')

#############################################################################################################


with open('data.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

line_count = len(lines)

word_count = 0
char_count = 0

for line in lines:
    # строк
    words = line.split()
    #слов
    word_count += len(words)
    #символы
    char_count += len(line)

# Выводим результаты
print(f'Количество строк: {line_count}')
print(f'Количество слов: {word_count}')
print(f'Количество символов: {char_count}')

#############################################################################################################

# исходный файл
with open('source.txt', 'r', encoding='utf-8') as source_file:
    content = source_file.read()

# в верхний регистр
content_upper = content.upper()

# в новый файл
with open('vtoroyfile.txt', 'w', encoding='utf-8') as dest_file:
    dest_file.write(content_upper)

print("копирование готово.")