"""
1 - Construir um algoritmo que leia dois números e efetue a adição. Caso o valor somado  seja maior que 20, este deverá ser apresentado somando-se a ele mais 8; caso o valor  somado seja menor ou igual a 20, este deverá ser apresentado subtraindo-se 5.
"""
print("""Vamos validar números! Se você me der um número maior que 20, somarei com 8, se me der um
número menor ou igual a 20, subtrairei por 5""")
num = float(input('Me diga o primeiro número: '))
num1 = float(input('Me diga o segundo número: '))
calculo = num + num1
if calculo > 20:
    print('O resultado é:', calculo + 8, 'já que o resultado seria: ', calculo, 'e e maior que 20!')
elif calculo <= 20:
    print('O resultado é:', calculo - 5, 'já que o resultado seria: ', calculo, 'e é menor ou igual a 20!')
