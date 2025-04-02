"""9) Escreva um programa, com uma função que imprima o
conceito de um aluno, dada a sua nota. Supor, apenas,
notas inteiras. O critério para conceitos é o seguinte:"""

print('Vamos analisar seu conceito de acordo com suas notas')
def nota():
    nota = int(input('Me diga sua nota: '))
    if nota < 3:
        print('Conceito E')
    elif nota >= 3 and nota< 6:
        print('Conceito D')
    elif nota > 6 and nota < 8:
        print('Conceito C')
    elif nota >= 8 and nota < 10:
        print('Conceito B')
    elif nota == 10:
        print('Conceito A')
    else:
        print('ERRO')
nota()
