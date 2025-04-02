"""
4 - Faça um algoritmo para ler um número inteiro e informar se o número é par ou ímpar. 

"""
print('Me diga um número inteiro e eu irei validar se ele e par ou impar')
num = int(input('Digite o número: '))
resto = num % 2
if resto == 0:
    print('O número é par')
elif resto != 0:
    print ('O número é impar!')
