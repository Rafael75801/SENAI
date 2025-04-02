print('Vamos fazer a soma dos números antes de outro número!')
acum = 0
n = int(input('Digite o número: '))
for v in range (0, n+1):
    acum = acum + v
print(f'A soma é de: {acum}')
