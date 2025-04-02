print('Vamos calcular seu aumento salarial!')
salario = float(input('Me diga seu salário: '))
if salario < 3000:
    aumento = (salario * 10) / 100
    salario_final = aumento + salario
    print(f'Seu novo salário é: %.2f' % salario_final)
else:
    aumento = (salario * 5) / 100
    salario_final = aumento + salario
    print(f'Seu novo salário é: %.2f' % salario_final)
