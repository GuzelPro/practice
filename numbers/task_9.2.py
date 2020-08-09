'''
ПЕРЕДЕЛАТЬ
С клавиатуры вводят три числа. Найти и вывести в консоль: минимальное число, 
минимальное число, среднеарифметическое значение всех чисел.
'''

'''
считать с консоли 1 число 
считать с консоли 2 число
считать с консоли 3 число 
Сравнить 1 число со 2 и 3 
Сравнить 2 число с 1 и 3 
Сравнить 3 число с 2 и 1 
вывести макс мин среднеарифметическое
'''

first_number = int(input('Введите 1 число\n'))
second_number = int(input('Введите 2 число\n'))
third_number = int(input('Введите 3 число\n'))
if first_number < second_number and first_number < third_number:
    print('Минимальное число ' + str(first_number))
if second_number < first_number and second_number < third_number:
    print('Минимальное число ' + str(second_number))
if third_number < second_number and third_number < first_number:
    print('Минимальное число ' + str(third_number))