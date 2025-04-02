"""
6) Faça um programa com uma função que necessite de
um argumento. A função retorna o valor do caractere 'P',
se o seu argumento for positivo, e 'N', se o seu argumento
for zero ou negativo.
"""
print('Vamos ver se um número é negativo ou positivo')
def conta():
    x = float(input('Me diga um valor: '))
    if x > 0:
        print(f'Seu valor é P')
    elif x <= 0:
        print(f'Seu valor e N')
conta()
    
