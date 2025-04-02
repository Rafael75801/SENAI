"""
8 - A prefeitura de Contagem abriu uma linha de crédito para os funcionários estatutários.
O valor máximo da prestação não poderá ultrapassar 30% do salário bruto.
Fazer um  algoritmo que permita entrar com o salário bruto e o valor da prestação,
e informar se o  empréstimo pode ou não ser concedido. 
"""
print('Vamos fazer uma validação de empréstimo e de suas prestações')
salario = float(input('Me diga o seu salário bruto: '))
prestacao = float(input('Me diga o valor da prestação: '))
emprestimo_validacao = salario * 30 / 100
if prestacao >= emprestimo_validacao:
    print('O empréstimo não pode ser concedido')
elif prestacao < emprestimo_validacao:
    print('O empréstimo pode ser concedido')
