'''
С клавиатуры вводят слово и два символа.
 Заменить и вывести все вхождения в слове символа 1 на символ 2.
Пример:
ввод - венера, е, и
вывод - винира




''' 

word = input('Введите слово\n')
word_1 = input('Символ-1\n')
word_2 = input('Символ-2\n')
s = word.replace(word_1, word_2)
print(s)



