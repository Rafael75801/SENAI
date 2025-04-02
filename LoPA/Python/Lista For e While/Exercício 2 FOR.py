"""
2 - Faça um programa que calcule a soma dos primeiros 50 números pares.
"""
acum = 0

for v in range (0, 101, 2):
    acum = acum + v
print(f'A soma dos pares e de: {acum}')
