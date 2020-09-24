'''
С клавиатуры вводят слово. Выполнить маскирование слова звездочками.
Пример:
ввод - пароль
вывод - ******

'''

def password(password):
    new_password = '*' * len(password)
return new_password