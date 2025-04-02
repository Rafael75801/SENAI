print('Vamos validar os tipos de triângulo')
a = float(input('Digite o primeiro valor para um lado:'))
b = float(input('Digite o segundo valor para o outro lado: '))
c = float(input('Digite o terceiro valor para o terceiro lado: '))

soma1 = a + b
soma2 = b + c
soma3 = c + a

if c > soma1 or b > soma3 or a > soma2:
    print('Não e um triângulo.')

#Equilátero
elif a == b and b == c and c == a:
    print('Equilátero')
#Escaleno
elif a != b and b != c and c != a:
    print('Escaleno')
#Isósceles
else:
    print('Isósceles')
