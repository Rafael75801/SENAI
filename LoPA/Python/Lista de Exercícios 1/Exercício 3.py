"""
3 - Faça um algoritmo para ler dois números inteiros e escrever o maior.
"""
print('Vamos descobrir qual número e maior!')
num = float(input('Me diga o primeiro número: '))
num1 = float(input('Me diga o segundo número: '))
if num >= num1:
    print(num, 'é maior que', num1)
elif num <= num1:
    print(num1, 'é maior que', num)
