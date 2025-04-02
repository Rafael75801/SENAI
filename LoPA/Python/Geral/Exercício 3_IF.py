"""
Escreva um programa para aprovar o empréstimo
bancário para a compra de uma casa. O programa deve
perguntar o valor da casa a comprar, o salário e a
quantidade de anos a pagar. O valor da prestação mensal
não pode ser superior a 30% do salário. Calcule o valor da
prestação como sendo o valor da casa a comprar dividido
pelo número de meses a pagar.
"""
print('Vamos fazer um programa para vermos se você está apto a um empréstimo')
preco_casa = float(input('Me diga o preço da casa que você quer comprar: '))
salario = float(input('Me informe seu salário: '))
tempo_casa = int(input('Me diga quanto anos você está disposto a pagar: '))
prestacao = preco_casa / (tempo_casa * 12)
validacao_salario = salario * 30 / 100
if prestacao <= validacao_salario:
    print('Você apto a pagar pelo empréstimo, e o valor de cada prestação será de: ', prestacao)
else:
    print('Você não está apto a pagar, pois o preço de cada prestação é de: ', prestacao)
    
