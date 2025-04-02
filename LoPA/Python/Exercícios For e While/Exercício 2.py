"""
Entrar com números enquanto forem positivos e
imprimir quantos números foram digitados.
"""
print('Me diga valores positivos (acima de zero) e eu vou contar quantos foram digitados, para sair, digite um número negativo (menor que zero)!')

valor = 0
while True:
    num = float(input('Me diga um valor para começarmos: '))
    if num < 0:
        print('Você escolheu acabar')
        break
    elif num == 0:
        print('0, número neutro')
        break
    valor = valor + 1
    print('Você digitou', valor, 'números positivos')
