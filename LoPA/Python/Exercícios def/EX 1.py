"""
1) Faça um programa com uma função que retorne o maior de dois números.
"""

def maior():
    a = int(input('Insira o valor: (a): '))
    b = int(input('Insira o valor (b): '))
    if a > b:
        print(f'{a} é maior que {b}', a > b)
    elif b > a:
        print(f'{b} é maior que {a}', b > a)
    else:
        print('Dados incoerentes')

maior()
