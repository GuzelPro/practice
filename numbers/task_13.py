'''
С клавиатуры вводят число до 5 цифрой. 
Вывести в консоль его текстовое представление, 
например, ввод - 3, вывод - три.


''' 
number = int(input('Введите число\n'))
if number == 1:
    print('один')
elif number == 2:
    print('Два')
elif number == 3:
    print('Три')
elif number == 4:
    print('Четыре')
elif number == 5:
    print('Пять')
else:
    print('Хуета')