print('Vamos fazer uma tabuada!')
def conta():
    i = int(input('Me diga um número para fazer a tabuada: '))
    for v in range(0, 10+1):
        print(f'{i} x {v} = {i * v}')
conta()
