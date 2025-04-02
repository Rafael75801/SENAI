"""
5) Faça um programa que percorra duas listas e
gere uma terceira com os elementos das duas primeiras.
"""
L = ['a', 'b', 'c']
print(f'A primeira lista é {L}')
V = ['d', 'e', 'f']
print(f'A segunda lista é {V}')
L.extend(V)
print(f'Juntando, temos: {L}')
