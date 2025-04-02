"""
2) Faça um programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""
L = []
x = 0
while x < 11:
    n = int(input("Digite um número (0 sai): "))
    x += 1
    if n == 0:
        break
    L.append(n)
for i in range (len(L)-1, -1, -1):
    print(L[i])
    
