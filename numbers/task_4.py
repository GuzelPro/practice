'''
С клавиатуры вводят три числа. Определить и вывести в консоль равна ли сумма первых двух чисел третьему. 

'''



first_number = int(input('Введите первое число\n'))
second_number = int(input('Введите второе число\n'))
third_number = int(input('Введите третье число\n'))
sum = int(first_number + second_number)
if sum == third_number:
    print('Сумма первых двух чисел равна третьему')
else:
    print('Cумма первых двух чисел не равна третьему')