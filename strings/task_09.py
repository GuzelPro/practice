'''
С клавиатуры вводят предложение и слово.
 Проверить есть ли данное слово в предложении.
Пример:
ввод - Меня зовут Дима, Дима
вывод - Слово есть
''' 

def sentence(sentence, word):
    if word in sentence.lower():
        return 'Слово есть'
    else:
        return 'Слова нет'