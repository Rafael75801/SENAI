"""
Escreva um programa que calcule o preço a pagar pelo
fornecimento de energia elétrica. Pergunte a quantidade
de kWh consumida e o tipo de instalação: R para
residências, I para indústrias e C para comércios. Calcule o
preço a pagar, de acordo com a tabela a seguir.
"""
print('Vamos calcular o preço de kWh que você tem que pagar com base no seu tipo')
tipo = input('Me diga qual o seu tipo (R para residência, C para comercial, I para industria): ')
if tipo == 'R':
    kWh = int(input('Me informe quantos kWh você consome: '))
    if kWh <= 500:
        print('Você vai pagar:', kWh * 0.40, 'reais')
    elif kWh <= 1000:
        print('Você vai pagar:', kWh * 0.65, 'reais')
elif tipo == 'C':
    kWh = int(input('Me informe quantos kWh você consome: '))
    if kWh <= 2500:
        print('Você vai pagar:', kWh * 0.55, 'reais')
    elif kWh <= 5000:
        print('Você vai pagar:', kWh * 0.60, 'reais')
elif tipo == 'I':
    kWh = int(input('Me informe quantos kWh você consome: '))
    if kWh <= 1000:
        print('Você vai pagar:', kWh * 0.55, 'reais')
    elif kWh <= 15000:
        print('Você vai pagar:', kWh * 0.60, 'reais')
