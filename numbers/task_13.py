'''
С клавиатуры вводят число до 5 цифрой. 
Вывести в консоль его текстовое представление, 
например, ввод - 3, вывод - три.


''' 

def number(number):
    if number == 1:
        return 'один'
    elif number == 2:
        return 'Два'
    elif number == 3:
        return 'Три'
    elif number == 4:
        return 'Четыре'
    elif number == 5:
        return 'Пять'
    else:
       return 'Хуета'