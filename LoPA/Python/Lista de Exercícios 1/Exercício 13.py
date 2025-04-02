print('Digite suas 3 notas e suas faltas, eu darei sua média e seu status!')
# Validações
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))
media = (nota1 + nota2 + nota3) / 3

falta = int(input('Digite sua quantidade de faltas: '))
limite_falta = 80 * 25 / 100

# Chats
if media < 7 and falta > limite_falta:
    media = a
    print(f'Você foi reprovado, por média e por falta. Sua média foi {a}, e sua quantidade de faltas superou a espectativa mínima.')
elif media >=7 and falta > limite_falta:
    print(f'Aprovado por média, sua média é de: {media}!')
    print('Reprovado por falta')
elif media < 7 and falta < limite_falta:
    print('Você foi reprovado pro média. Sua média foi de {media}')
    print('Você foi aprovado por frequência')
else:
    print('Aprovado com excelência!')
