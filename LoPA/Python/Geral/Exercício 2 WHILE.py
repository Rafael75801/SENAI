"""
2) Entrar com números enquanto forem positivos e
imprimir quantos números foram digitados.
"""
digito = 0
print('Vamos contar quantos números você digitou!')
while True:
    print('Digite algum número negativo, para parar a operação!')
    num = int(input('Digite um número: '))
    if num < 0:
        print('Você escolheu parar')
        break
    digito += 1
    print(f'Você digitou {digito}')
