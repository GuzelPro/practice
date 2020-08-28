'''
С клавиатуры вводят число n.
 Вывести в консоль факториал числа n.

''' 


number = int(input('Введите число \n'))
fack = 1
for i in range(1,number+1):
    fack = fack * i
print(fack)
    
