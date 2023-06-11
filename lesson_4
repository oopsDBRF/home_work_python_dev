"" Задача №1. Про уникальные числа."""
"""
import random

first_list = []
second_list =[]
show_num_list = []

def create_list(num, box):
    for _ in range(num):
        box.append(random.randint(1,10))
    return box

def comparison_list(box, box2):
    count = min(len(box), len(box2))
    show_num_list = []
    for i in range(count):
        if box[i] in box2:
            if box[i] not in show_num_list:
                show_num_list.append(box[i])

    return show_num_list

num = int(input('Введите размер первого набора чисел: '))
num2 = int(input('Введите размер второго набора чисел: '))


create_list(num, first_list)
create_list(num2, second_list)
comparison_list(first_list, second_list)

print(first_list)
print(second_list)

if comparison_list(first_list, second_list) == []:
    print('Одинаковых чисел нет.')
else:
    print(*sorted(comparison_list(first_list, second_list)))
"""

''' Задача №2. Кустарники. '''

num = int(input('Введите число кустарников: '))
count = 0
total = 0
bushes_list = []

for i in range(num):
    bushes_list.append(int(input(f'Укажите число ягод {i + 1} кустарника: ')))

if len(bushes_list) <= 3:
    for j in bushes_list:
        count += j
    print(f'Максимальное число ягод - {count}.') # тк кустов <= 3, то все они соседи.
else:
    for i in range(len(bushes_list)):
        if i + 1 == len(bushes_list):
            if bushes_list[i - 1] + bushes_list[i] + bushes_list[0] > total:
                count = i + 1
                total = bushes_list[i - 1] + bushes_list[i] + bushes_list[0]
        else:
            if bushes_list[i] + bushes_list[i - 1] + bushes_list[i + 1] > total:
                count = i + 1
                total = bushes_list[i] + bushes_list[i - 1] + bushes_list[i + 1]

    print(f'Максимальное число ягод - {total} собралось с куста {count}.')
