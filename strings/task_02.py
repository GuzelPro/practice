'''
С клавиатуры вводят три слова. Соединить эти слова через строку ‘ и ’ 
и вывести полученную строку в консоль.
Пример:
ввод - один, два, три
вывод - один и два и три



''' 

word = input('Введите 3 слова\n')
print(word.replace(',', ' и'))


