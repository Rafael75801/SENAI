"""
5 - Escreva um algoritmo que receba um número e imprima uma das mensagens:
    “é  múltiplo de 3” ou “não é múltiplo de 3”.  
"""
print('Vamos ver se o número é ou não múltiplo de 3!')
num = float(input('Digite o número: '))
resto = num % 3
if resto == 0:
    print('Ele e múltiplo de 3')
elif resto != 0:
    print('Ele não e múltiplo de 3')
