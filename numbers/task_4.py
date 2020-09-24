'''
С клавиатуры вводят три числа.
 Определить и вывести в консоль равна ли сумма первых двух чисел третьему. 

'''

    
def numbers(int(first_number, second_number, third_number)):
    sum = int(first_number + second_number)
        if sum == third_number:
            return 'Сумма первых двух чисел равна третьему'
        else:
            return 'Cумма первых двух чисел не равна третьему'