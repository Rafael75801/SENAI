"""
3 - Solicitar a idade de várias pessoas e imprimir: Total de pessoas com menos de 21 anos.
Total de pessoas com mais de 50 anos. O programa termina quando idade for = -99.
"""
cont_menor = 0
cont_maior = 0
print('Vamos fazer um programa para verificar idades e seu total de pessoas!')
print('O programa termina quando você digitar "-99"')
print('Idades entre 21 e 50 não serão contabilizadas!')
while True:
    idade = int(input('Me informe uma idade: '))
    if idade == -99:
        print('-99, você escolheu encerrar.')
        break
    elif idade < 21:
        cont_menor = cont_menor + 1
    elif idade > 50:
        cont_maior = cont_maior +1
        
print(f'Total de {cont_maior} pessoas maiores que 50 anos.')
print(f'Total de {cont_menor} pessoas menores de 21 anos')
