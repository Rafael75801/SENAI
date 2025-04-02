"""
Você está viajando para diferentes regiões do mundo e precisa converter as temperaturas de
Celsius para Fahrenheit e vice-versa.
Crie uma função que converta uma temperatura de acordo com a escolha do usuário. 
"""
resposta = input("""Siga a tabela para ser feita a conversão de temperatura:
F = Fahrenheit
C = Celsius
K = Kelvin


Digite: """)
# Contas
def fahrenheit():
    celsius = (temp_F - 32) * 0.5
    kelvin = (temp_F - 32) * 1.8 + 274
    print(f'Sua temperatura em Celsius é: {celsius}ºC')
    print(f'Sua temperatura em Kelvin é: {kelvin}ºK')

def celsius():
    fahrenheit = (temp_C * 1.8) + 32
    kelvin = temp_C + 274
    print(f'Sua temperatura em Fahrenheit é de: %.2fºF' % fahrenheit)
    print(f'Sua temperatura em Kelvin é de: {kelvin}ºK')


def kelvin():
    fahrenheit = (temp_K - 274) * 1.8 + 32
    celsius = temp_K - 274
    print(f'Sua temperatura em Fahrenheit é de: %.2fºF' % fahrenheit)
    print(f'Sua temperatura em Celsius é de: {celsius}ºC')

# Validação Resposta
if resposta == 'F':
    temp_F = float(input('Me diga a temperatura em Fahrenheit, para ser convertida: '))
    fahrenheit()
elif resposta == 'C':
    temp_C = float(input('Me diga a temperatura em Celsius, para ser convertida: '))
    celsius()
elif resposta == 'K':
    temp_K = float(input('Me diga a temperatura em Kelvin, para ser convertida: '))
    kelvin()
