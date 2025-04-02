"""
Entrar com números e imprimir o triplo de cada número.
O programa acaba quando entrar o número -999
"""
while True:
    valor = int(input('Me diga um número, se você escolher -999, o programa acaba: '))
    if valor == -999:
        print('Você escolheu acabar')
        break
    valor2 = valor * 3
    print(valor2)
