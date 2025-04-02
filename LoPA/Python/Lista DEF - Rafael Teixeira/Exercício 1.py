"""
Escreva um programa com uma função que leia a altura e o raio de um cilindro e
imprima o volume do mesmo (Limite a 2 casas decimais o retorno).
"""
print('Vamos fazer uma conta para calcular o volume do cilindro')

altura = float(input('Me diga a altura do cilindro '))
raio = float(input('Me diga o raio do cilindro: '))
def conta(x, y):
    global altura, raio
    soma = 3.14 * (raio ** 2) * altura
    print('O valor é %.2f' % soma)
conta(altura, raio)
