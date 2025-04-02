print('Vamos verificar sua maioridade!')
nome = input('Primeiro, me diga seu nome: ')
idade = int(input('Agora, me diga sua idade: '))
if idade <18:
    print(f'Você é menor de idade, {nome}, pois você tem {idade} anos')
elif idade >= 18:
    print(f'Você e maior de idade, {nome}, pois você tem {idade} anos')
