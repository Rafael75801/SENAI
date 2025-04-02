"""
3) Faça um programa com uma função que receba o lado
(l) de um quadrado e retorne a sua área (A = lado2).
"""
print('Vamos descobrir a área de um quadrado!')
def conta():
    l = float(input('Digite um lado do quadrado: '))
    area = l ** 2
    print(f'A área do seu quadrado é {area}')
    return conta()
print(conta())
