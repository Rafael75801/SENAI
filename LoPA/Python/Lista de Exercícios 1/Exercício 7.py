"""
7- Em uma empresa paga-se R$ 19,50 a hora e recolhe-se para o imposto de renda 10% dos salários
acima de R$ 1500,00.
Dado o número de horas trabalhadas por um  funcionário, informar o valor do seu salário líquido.
"""
print('Vamos calcular o seu salário líquido baseado em suas horas trabalhadas e os impostos!')
horas = float(input('Me diga suas horas trabalhadas por dia: '))
salario = (horas * 20) * 19.50
if salario >= 1500:
    imposto = (1500 * 10) / 100
    salario1 = salario + imposto
    print('Seu salário é de:', salario1)
elif salario <= 1500:
    print('Seu salário é de:', salario)
