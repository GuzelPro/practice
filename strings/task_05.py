'''
С клавиатуры вводят слово и символ. 
Посчитать и вывести в консоль сколько раз символ встречается в слове.

Пример:
ввод - ананас, а
вывод - 3
''' 

def letter(letter_1, letter_2):
    s = 0
        for i in letter_1.lower():
            if i == letter_2:
                s+=1
    return s

