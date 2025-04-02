"""
7) Faça um programa para selecionar os elementos de uma lista
de forma a copiá-los para outras duas listas.
Nesse caso, considere que, inicialmente, os valores estão na lista V = [9, 8, 7, 12, 0, 13, 21]
mas que devem ser copiados para a P, se forem pares; ou para a I, se forem ímpares.
"""
V = [9, 8, 7, 12, 0, 13, 21]
for i in V:
    if i % 2:
        print(f'{i} = impar')
    else:
        print(f'{i} = par')
