"""
2 - Faça um programa que receba valores, mostrando na tela, no final imprima o maior e
o menor desses números.
Obs: O programa encerra quando receber um número negativo.
"""
print('Vamos fazer um programa que vai ver qual número é maior e qual é menor!')
print('Você pode encerrara  qualquer momento me entregando um numero negativo!')
n = float(input('Me diga um número: '))
maior = n
menor = n
while True:
    if n < 0:
        print('Você escolheu parar')
        break
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    print(f'{maior} é maior que {menor}')
    
    
