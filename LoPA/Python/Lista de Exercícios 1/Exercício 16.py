print('Digite sua idade e eu lhe darei sua faixa etária!')

idade = int(input('Me diga sua idade: '))

if idade < 2:
    print('Bebê')
elif idade <= 12:
    print('Criança')
elif idade <= 23:
    print('Adolescente')
elif idade <= 70:
    print('Adulto')
else:
    print('Idoso')
