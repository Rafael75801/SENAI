# -*- coding: UTF-8 -*-
"""
Escreva um programa que pergunte o salário do
funcionário e calcule o valor do aumento. Para salários
superiores a R$ 1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, de 15%.
"""
print('Vamos calcular um aumento de salário')
salario = float(input('Me diga o seu salário para calcular o aumento: '))

if salario >= 1249:
    aumento = salario * 10 / 100
    print('Seu novo salário é de: ', salario + aumento)

else:
    aumento1 = salario * 15 / 100
    print('Seu novo salário é de: ', salario + aumento1)
