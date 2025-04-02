"""
Escreva um programa, com uma função para ler a idade
de uma pessoa e informar a sua classe eleitoral, conforme:
Não-eleitor (abaixo de 16 anos).
Eleitor obrigatório (entre 18 e 65 anos).
Eleitor facultativo (entre 16 e 18 ou maior de 65
anos).
"""
print('Vamos ver se você está apto para votar')
def validacao():
    idade = int(input('Me diga sua idade: '))
    if idade < 16:
        print(f'Você não está apto a votar porque tem {idade}, e a idade mínima para votar e 16 anos.')
    elif idade >= 18 and idade < 66:
        print(f'Seu voto e obrigatório porque você tem {idade} anos')
    elif idade >=16 and idade < 18 and idade > 65:
        print(f'Seu voto é facultativo porque você tem {idade} anos.')
validacao()
