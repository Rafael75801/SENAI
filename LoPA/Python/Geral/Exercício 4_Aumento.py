# -*- coding: UTF-8 -*-
print('Me diga um salário e depois um aumento que eu irei fazer o calculo do aumento e do novo salário!')
salario = float(input('Me diga o valor do salário para começarmos: ' ))
acrescimo = int(input('Me diga o valor do aumento em porcentagem: '))
aumento = (salario * acrescimo) / 100
novo_salario = salario + aumento
print('-=@===============@=-')
print('Seu aumento foi de: ', aumento)
print('E seu novo salário é: ', novo_salario)
