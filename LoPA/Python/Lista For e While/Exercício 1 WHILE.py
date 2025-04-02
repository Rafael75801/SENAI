"""
1 - Faça um programa que receba valores, mostrando na tela, e calcula a soma e a média desses
números. Obs: O programa encerra quando receber um número negativo.
"""
print('Vamos fazer um programa que vai calcular a soma e a média dos números que você me apresentar.')
print('Você para o programa quando inserir um número negativo.')
soma = 0
cont = 0
while True:
    num = float(input('Digite um número: '))
    if num < 0:
        print('Você escolheu parar')
        break
    soma += num
    cont += 1
media = soma / cont
print(f'Soma: {soma}')
print(f'Média: {media}')
