# -*- coding: UTF-8 -*-
print('Digite para mim uma quantidade de dias, horas, minutos e segundos que eu vou somas tudo e converter em segundos!')
dias = int(input('Digite a quantidade de dias: '))
horas = int(input('Digite a quantidade de horas: '))
minutos = int(input('Digite a quantidade de minutos: '))
segundos = int(input('Digite a quantidade de segundos: '))
print('Calculando...')
dias_calculado = dias * 86400
horas_calculada =horas * 3600
minutos_calculado = minutos * 60
resultado = dias_calculado + horas_calculada + minutos_calculado + segundos
print("O resultado é: ", resultado)
