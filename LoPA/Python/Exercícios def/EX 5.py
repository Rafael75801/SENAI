"""
5) Faça um programa com uma função que receba o
raio (R) de um círculo e retorne a sua área (A = PI * R2).
"""
print('Vamos achar a área de um círculo!')
def circulo():
    x = int(input('Diga o raio do seu círculo: '))
    area = 3.14 * (x ** 2)
    print(f'Sua área é: {area}')
    return circulo()
print(circulo())
