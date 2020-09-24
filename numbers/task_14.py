'''
С клавиатуры вводят число n.
 Вывести в консоль факториал числа n.

''' 

def number(number):
    fack = 1
        for i in range(1,number+1):
    fack = fack * i
return(fack)