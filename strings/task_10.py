'''
С клавиатуры вводят предложение.
 Вывести это предложение в верхнем и нижнем регистре.
Пример:
ввод - Меня зовут Дима
вывод - МЕНЯ ЗОВУТ ДИМА, меня зовут дима

''' 

sentence = input('Введите предложение\n')
upper = sentence.upper()
lower = sentence.lower()
print(upper + ',' + lower)