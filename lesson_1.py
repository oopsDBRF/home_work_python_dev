""" Задача #1 """
""" Найдите сумму цифр трехзначного числа. Используйте f-строки чтобы оформить красивый вывод """
"""
num = int(input('Введите число: '))
copy_num = num
total = 0

if num < 0:
    num *= -1

for i in range(3):
    total += num % 10
    num = num // 10

print(f'Сумма цифр числа {copy_num} = {total}')
"""

""" Задача #1* """
""" Решите для числа произвольной разрядности: произвольное количество цифр в числе. """
"""
num = int(input('Введите число: '))
str_copy_num = str(num)
total = 0

if num < 0:
    num *= -1

for i in range(len(str_copy_num)):
    total += num % 10
    num = num // 10

print(f'Сумма цифр числа {str_copy_num} = {total}')
"""

""" Задача #1** """
""" Для числа произвольной разрядности добавить в вывод строку с числами. """
"""
num = int(input('Введите число: '))
copy_num = str(num)
total = 0
text = ''

if num < 0:
    num *= -1

if '-' in copy_num:
    for i in range(len(copy_num)-1):
        total += num % 10
        text += str(num % 10) + '+'
        num = num // 10
else:
    for i in range(len(copy_num)):
        total += num % 10
        text += str(num % 10) + '+'
        num = num // 10

print(f'Сумма цифр числа {copy_num} = {total}({text[0:len(text) - 1]})')
"""
""" Задача #2 """
"""
total = int(input('Сколько журавлей всего сделано?: '))
# Более костыльное решение
kate = 0
petya = 0
sergey = 0

flag = True

while flag == True:
    petya += 1
    sergey +=1
    kate = (petya+sergey)*2
    if kate + petya + sergey == total:
        flag = False
        break

print(f'Петя и Сергей сделали {petya+sergey}, Катя сделала {kate}.')

# Более симпотичное решение

total = 24

k, s, p = 0, 0, 0

for i in range(1, total+1):

    if i%5 == 0 or i%6 == 0:
        s += 1
        p += 1
    else:
        k += 1

print(f'Катя - {k}, Петя - {p//2}, Сергей - {s//2}')

print(f'Петя и Сергей сделали {petya+sergey}, Катя сделала {kate}.')
"""

""" Задача #3 """
"""
ticket_num = input('Введите номер билета: ')

left_num = int(ticket_num[0]) + int(ticket_num[1]) + int(ticket_num[2])
right_num = int(ticket_num[3]) + int(ticket_num[4]) + int(ticket_num[5])

if left_num == right_num:
    print('Поздравляю! Ваш билет счастливый!')
else:
    print('Увы! Ваш билет не счастливый.')
"""


""" Задача #4 """
"""
n = int(input('Ширина шоколадки, долек: '))
m = int(input('Длина шоколадки, долек: '))
k = int(input('Сколько долек вы хотите отломить: '))

if k == n * m:
    print('Вы съедите всю шоколадку.')
elif k > n * m:
    print('Превышен размер шоколадки.')
elif k <= 0:
    print('Вы ничего не отломили.')
elif k < n * m and (k % n == 0 or k % m == 0):
    print('Вы отломили шоколадку!')
else:
    print('Что то пошло не так.')
"""