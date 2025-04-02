print('Vamos ver qual valor é maior e coloca-los em ordem crescente!')
a = int(input('Digite o primeiro valor (a): '))
b = int(input('Digite o segundo valor (b): '))

if a > b:
    print(f'O menor valor é: {b} e o maior é {a}')
elif b > a:
    print(f'O menor valor é {a} e o maior e {b}')
else:
    print('Números iguais, não e possível definir o maior')
