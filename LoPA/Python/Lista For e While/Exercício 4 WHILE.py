"""
4 - Faça um programa que leia vários inteiros positivos e mostre, no final, a soma dos
números pares e a soma dos números ímpares. O programa para quando entrar um número maior que
1000.
"""
soma_par = 0
soma_impar = 0
print('Vamos fazer um programa para somar números inteiros positivos, separando-os em impares e em pares.')
print('O programa irá parar quando você digitar um número maior que 1000!')
while True:
    num = float(input('Digite um número: '))
    if num > 1000:
        print('Número maior que 1000, programa encerrado.')
        break
    if num % 2 == 0:
        soma_par += num
    elif num % 2 != 0:
        soma_impar += num
print(f'{soma_par} até agora para numeros os pares!')
print(f'{soma_impar} até agora para numeros os impares!')
