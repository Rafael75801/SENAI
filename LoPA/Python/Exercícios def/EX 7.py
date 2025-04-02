"""
Faça um programa com uma função chamada
somaImposto. A função possui dois parâmetros formais:
taxaImposto, que é a quantia de imposto sobre vendas
expressa em porcentagem, e custo, que é o custo de um
item antes do imposto. A função "altera" o valor de custo
para incluir o imposto sobre vendas.
"""

print('Vamos calcular o preço de um produto')
taxa = int(input('Digite o valor da porcentagem da taxa do imposto: '))
custo_item = float(input('Digite o custo do item antes do imposto: '))
def  somaImposto(taxaImposto, custo):
    return custo + custo * taxaImposto / 100
print(somaImposto(taxa, custo_item))
