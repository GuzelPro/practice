'''
С клавиатуры вводят предложение с несколькими пробелами между словами. 
Сократить каждый разрыв между словами до одного пробела и вывести в консоль.
Пример:
ввод - Привет    как        дела          ?
вывод - Привет как дела ?


''' 

sentence = input('Введите предложение\n')
s = sentence.split()
new_sentence =  ' '.join(s)
print(new_sentence)

