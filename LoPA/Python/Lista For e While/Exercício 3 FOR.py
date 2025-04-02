"""
3 - Escreva um programa que apresenta o Fatorial de um número.
Ex: Fat de 5 = 5X4X3X2X1 = 120.
"""
print('Vamos calcular o fatorial de um número')
acum = 1
valor = int(input('Me diga o número para fazermos o fatorial: '))
for a in range(1, valor +1):
    acum = acum * a
    print(acum)
