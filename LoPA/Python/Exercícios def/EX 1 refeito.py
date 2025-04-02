'''
Faça um programa com uma função que retorne o
maior de dois números.
'''

print('Vamos calcular qual o maior número')
def num():
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    if a > b:
        print(f'{a} é maior que {b}')
        return num()
    elif b > a:
        print(f'{b} e maior que {a}')
        return num()
print(num())
