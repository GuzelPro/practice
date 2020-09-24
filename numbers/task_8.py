'''

С клавиатуры вводят два числа. 
Вывести в консоль, какое число больше. 
Например, "Первое число больше".
'''

def number (int(second_number, first_number)):
    if second_number > first_number:
        return 'Первое число больше'
    if first_number > second_number:
        return 'Второе число больше'
    else:
        return 'Числа равны'