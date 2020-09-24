'''
С клавиатуры вводят три числа. Вывести все числа, которые меньше 10 и их сумму.

'''

def number(first_number, second_number, third_number):
    sum = first_number + second_number + third_number
        if first_number < 10 and second_number < 10 and third_number < 10:
            return (str(first_number) + ' ' +  str(second_number) + ' ' + str(third_number) + ' Cумма этих чисел равна ' + str(sum))
        elif first_number < 10 and second_number < 10 and third_number > 10:
            return(str(first_number) + ' ' + str(second_number) + ' ' + 'Сумма этих чисел равна ' + str(first_number + second_number))
        elif first_number < 10 and second_number > 10 and third_number < 10:
            return(str(first_number) + ' ' + str(third_number) + ' '  + 'Сумма этих чисел равна ' + str(first_number + third_number))
        elif first_number > 10 and second_number < 10 and third_number < 10:
            return(str(second_number) + ' ' + str(third_number) + ' ' + 'Сумма этих чисел равна ' +  str(second_number + third_number))
        else:
            return('Все числа больше 10')