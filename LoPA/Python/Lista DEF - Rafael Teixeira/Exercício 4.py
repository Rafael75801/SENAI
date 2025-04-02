"""
Você está participando de um evento que conta com uma contagem regressiva antes de algo grande acontecer. Crie uma função que imprima a contagem regressiva até zero.
A cada número, ele deve ser impresso, e ao final deve aparecer uma mensagem de celebração!
"""

print('Vamos fazer uma contagem regressiva!')
def conta():
    for v in range(int(input('Digite um número para ir até 0: ')), 0, -1):
        print(v)
    print('Feliz ano novo!')
conta()
