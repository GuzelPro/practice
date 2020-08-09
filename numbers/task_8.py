'''
ПЕРЕДЕЛАТЬ
С клавиатуры вводят два числа. 
Вывести в консоль, какое число больше. 
Например, "Первое число больше".
'''

second_number = int(input('Введите первое число\n'))
first_number = int(input('Введите второе число\n'))
if second_number > first_number:
    print('Первое число больше')
if first_number > second_number:
    print('Второе число больше')