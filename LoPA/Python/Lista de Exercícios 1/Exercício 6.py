"""
6 - Faça um algoritmo para ler dois números inteiros A e B e informar se A é divisível  por B.
"""
print('Vamos calcular e ver se um número é divisivel pelo outro!')
num = int(input('Me diga o primeiro número: '))
num1 = int(input('Me diga o segundo número: '))
divisivel = num % num1
if divisivel == 0:
    print(num, 'é divisível por', num1)
elif divisivel != 0:
    print(num, 'não e divisível por', num1)
