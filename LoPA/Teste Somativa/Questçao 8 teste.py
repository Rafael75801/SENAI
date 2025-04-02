x = 0
print('Vamos ver quantos números vem antes de outro número!')
num = int(input('Me diga um valor para eu ver quantos números tem até ele: '))
while x < num:
    for x in range(0, num):
        x += 1
        print(f'{x}')
