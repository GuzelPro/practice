'''
С клавиатуры вводят слово и два символа.
 Заменить и вывести все вхождения в слове символа 1 на символ 2.
Пример:
ввод - венера, е, и
вывод - винира

ЗАМЕЧАНИЕ:
не заменяет, если в слове символ для замены - большая буква
Пример:
ввод - Мама, м, т
вывод - Мата
upper()
''' 


 def word(word, word_1, word_2):
    s = (word.lower()).replace(word_1, word_2)
return s 