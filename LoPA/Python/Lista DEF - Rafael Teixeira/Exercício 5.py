"""
5) Em uma aventura matemática, o personagem encontra números misteriosos e precisa
determinar se eles são primos.
Um número primo é aquele maior que 1 e que não é divisível por nenhum outro número
além de 1 e ele mesmo. Sua missão é criar uma função que verifica se um número é primo.
"""
def primo():
    num = float(input('Me diga um número: '))
    if num % 2 == 0:
        print('Não é número primo')
    else:
        print('É um número primo')
primo()
