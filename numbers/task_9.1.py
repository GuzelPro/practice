'''
ПЕРЕДЕЛАТЬ
С клавиатуры вводят три числа. Найти и вывести в консоль: максимальное число, 
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


def (first_number, second_number, third_number)
    sum = (first_number + second_number + third_number)
if first_number > second_number and first_number > third_number:
    return('Максиальное число ' + str(first_number))
if second_number > first_number and second_number > third_number:
    return('Максиальное число ' + str(second_number))
if third_number > second_number and third_number > first_number: 
    return('Максиальное число ' + str(third_number))
if first_number < second_number and first_number < third_number:
    return('Минимальное число ' + str(first_number))
if second_number < first_number and second_number < third_number:
    return('Минимальное число ' + str(second_number))
if third_number < second_number and third_number < first_number:
    return('Минимальное число ' + str(third_number))
return('Среднеарифмитическое число равно  ' + str(int(sum/3)))

