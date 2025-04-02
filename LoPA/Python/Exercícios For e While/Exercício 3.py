"""
3) Entrar com vários números positivos e imprimir a média dos números
"""
valor_repetir = int(input('Digite a quantidade de vezes que você quer repetir: '))
acum = 0
for v in range (0, valor_repetir):
    valor_conta = float(input('Digite o valor: '))
    acum = acum + valor_conta
print('A média dos valores é: ', acum / valor_repetir)
