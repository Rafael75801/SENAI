"""
6) A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista
T = [-10, -8, 0, 1, 2, 5, -2, -4]. Faça um programa que imprima a menor e a maior temperatura
assim como a temperatura média. 
"""
print('Vamos medir a menor temperatura de Mons na Bélgica, e a média da temperatura')
T = [-10, -8, 0, 1, 2, 5, -2, -4]
N = len(T)
conta = (T[0] + T[1] + T[2] + T[3] + T[4] + T[5] + T[6] + T[7]) / N
T.sort()
print(f'A menor temperata é {T[0]}, e a maior temperatura é {T[7]}')
print(f'E a média da temperatura é {conta}')
