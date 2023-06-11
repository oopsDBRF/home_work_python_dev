''' Задача #1. Степень числа. '''
'''
def rec_func(num, degree):
    if (num == 0 and degree == 0) or (degree == 0):
        return 1
    if degree == 1:
        return num
    else:
        return num*rec_func(num, degree - 1)

num = int(input('Введите числа для возведения в степень: '))
degree = int(input('Введите число степени: '))



print(rec_func(num, degree))
'''

''' Задача #2. Сумму чисел с исп +1 и -1. '''
'''
num = int(input('Введите положительное целое число а: '))
second_num = int(input('Введите положительное целое число b: '))

def sum_nums(num, second_num):
    if num == 0:
        return second_num;
    if second_num == 0:
        return num;
    else:
        return sum_nums(num - 1, second_num + 1)


print(sum_nums(num, second_num))
'''
