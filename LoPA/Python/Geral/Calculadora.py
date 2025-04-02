"""
Escreva um programa que leia dois números e que
pergunte qual operação você deseja realizar: soma (+),
subtração (-), multiplicação (*) e divisão (/). Exiba o
resultado da operação solicitada.
"""
sub = '-'
som = '+'
mult = '*'
div = '/'

pergunta = input('Me diga uma forma de conta para fazermos: ')
if pergunta == som:
    numsom = int(input('Me diga um número para fazermos a conta: '))
    numsom2 = int(input('Me diga outro número para fazermos a conta: '))
    print('Sua resposta é: ', numsom + numsom2)
elif pergunta == sub:
    numsub = int(input('Me diga um número para fazermos a conta: '))
    numsub2 = int(input('Me diga outro número para fazermos a conta: '))
    print('Sua resposta é: ', numsub - numsub2)
elif pergunta == mult:
    nummult = int(input('Me diga um número para fazermos a conta: '))
    nummult2 = int(input('Me diga outro número para fazermos a conta: '))
    print('Sua resposta é: ', nummult * nummult2)
elif pergunta == div:
    numdiv = int(input('Me diga um número para fazermos a conta: '))
    numdiv2 = int(input('Me diga outro número para fazermos a conta: '))
    print('Sua resposta é: ', numdiv / numdiv2)
