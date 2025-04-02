"""
Faça um programa com uma função que receba dois
números e retorne True se o primeiro número for
múltiplo do segundo.
"""
print('Vamos fazer uma conta para ver se um número e multiplo do outro')
def conta():
    a = int(input('Me diga o primeiro número: '))
    b = int(input('Me diga o segundo número: '))
    conta = a / b
    if a % b == 0:
        return True
    else:
        return False
print(conta())
