print('Vamos ver se você foi aprovado na faculdade!')
nota1 = float(input('Me diga sua primeira nota: '))
nota2 = float(input('Me diga sua segunda nota: '))
media = (nota1 + nota2) / 2

if media >=0 and media < 3:
    print:('Reprovado')
elif media < 7:
    print('Recuperação')
elif media <=10:
    print('Aprovado')
else:
    print('ERROR 404')
