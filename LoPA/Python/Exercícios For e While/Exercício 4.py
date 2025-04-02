"""
4) Ler vários números e informar quantos números entre 100 e 200 foram digitados.
Quando o valor 0 (zero) for lido, o programa deve cessar sua execução.
"""
print('Me informe números entre 100 e 200 para eu ver quantos foram digitados.')

a = int(input('Diga quantas vezes você quer digitar: '))
for v in range(100, 200, a):
    print(a)

