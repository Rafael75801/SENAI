"""
3) Faça um programa que leia 4 notas, mostre as notas e a média na tela.
"""
L = [float(input('Digite uma nota: ')), float(input('Digite outra nota: ')), float(input('Digite outra nota: ')), float(input('Digite outra nota: '))]
N = len(L)
conta = (L[0] + L[1] + L[2] + L[3]) / N
print(f'A média é: {conta}')
