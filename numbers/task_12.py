'''
С клавиатуры вводят три числа. Вывести все числа, которые меньше 10 и их сумму.

'''
first_number = int(input('ВВедите первое число\n'))
second_number = int(input('Введите второе число\n'))
third_number = int(input('Введите третье число\n'))
sum = first_number + second_number + third_number
if first_number < 10 and second_number < 10 and third_number < 10:
    print(str(first_number) + ' ' +  str(second_number) + ' ' + str(third_number) + ' Cумма этих чисел равна ' + str(sum))
elif first_number < 10 and second_number < 10 and third_number > 10:
    print(str(first_number) + ' ' + str(second_number) + ' ' + 'Сумма этих чисел равна ' + str(first_number + second_number))
elif first_number < 10 and second_number > 10 and third_number < 10:
    print(str(first_number) + ' ' + str(third_number) + ' '  + 'Сумма этих чисел равна ' + str(first_number + third_number))
elif first_number > 10 and second_number < 10 and third_number < 10:
    print(str(second_number) + ' ' + str(third_number) + ' ' + 'Сумма этих чисел равна ' +  str(second_number + third_number))
else:
    print('Все числа больше 10ы