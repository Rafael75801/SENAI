"""
Faça um programa com uma função que receba dois números e retorne
True se o primeiro número for múltiplo do segundo.
"""
print('Vamos descobrir se dois valores são múltiplos!')
def teste():
    a = int(input('Me diga um número (a): '))
    b = int(input('Me diga um número (b): '))
    if True a % b == 0:
        print(f'{b} é múltiplo de {a}')
    else:
        print(f'Os dois números não são multiplos')
teste()
