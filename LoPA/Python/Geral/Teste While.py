# -*- coding: UTF-8 -*-
"""
n = 1
soma = 0
while n <= 10:
    x = int(input("Digite o %i número: " % n))
    soma = soma + x
    n = n + 1
print ("Soma: %i" % soma(/ total))
"""

acum = 0
while True:
    triagem = input("""Vamos fazer contas? Digite:
Sim - Para continuar
Não - Para parar
Digite: """)
    if triagem == 'Não' or triagem == 'não' or triagem == 'NÃO' or triagem == 'nao' or triagem == 'n' or triagem == 'ñ' or triagem == 'nÃo' or triagem == 'nãO' or triagem == 'NAo' or triagem== 'NãO' or triagem == 'nÃO':
        print('Você escolheu sair.')
        break
    else:
        valor = int(input("Digite um número a somar ou 0 para sair: "))
        acum = acum + valor
    """
    if valor == 0:
        print('Você escolheu sair.')
        break
    acum = acum + valor
print ('O resultado da sua soma é:', acum)
    """
