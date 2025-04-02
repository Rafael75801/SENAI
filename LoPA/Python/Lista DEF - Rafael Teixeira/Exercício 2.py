print('Vamos ver se um número é um número perfeito')
valor = 0
div = 0

def conta():
    valor = int(input('DIgite o número: '))
    soma = 0
    for i in range(1, valor):
        if valor % i == 0:
            soma = soma + i
    if soma == valor:
        print('Número perfeito!')
    else:
        print('Não e um número perfeito...')            
