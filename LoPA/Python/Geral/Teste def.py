'''
# -*- coding: UTF-8 -*-

def soma(a, b):
    return(a + b)

print(soma(2, 9))
print(soma(7, 8))
print(soma(10, 15))

def media():
    num = float(input('Digite um número: '))
    num2 = float(input('Digite outro número: '))
    media = (num + num2) / 2
    print('Sua média é:', media)

media()
media()
media()
media()
'''

# -*- coding: UTF-8 -*-

def epar(x):
    return(x % 2 == 0)

def par_ou_impar(x):
    if epar(x):
        return "par"
    else:
        return "ímpar"
    
print(par_ou_impar(int(input('Digite um número: '))))
print(par_ou_impar(int(input('Digite outro número: '))))
