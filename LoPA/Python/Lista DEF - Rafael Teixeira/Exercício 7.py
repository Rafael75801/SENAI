"""
Você precisa executar cálculos entre dois números com os operadores matemáticos
simples (adição, subtração, multiplicação e divisão).
Crie um programa com 4 funções (uma para cara operador) que deixe a opção de escolha
para o usuário que irá inserir dois valores e selecionar sua operação
"""
# Calculadora 1
def soma():
    a = float(input('Digite o primeiro número para a soma: '))
    b = float(input('Digite o segundo número para a soma: '))
    print(f'{a} + {b} = {a + b}')
def sub():
    a = float(input('Digite o primeiro número para a subtração: '))
    b = float(input('Digite o segundo número para a subtração: '))
    print(f'{a} - {b} = {a - b}')
def mult():
    a = float(input('Digite o primeiro número para a multiplicação: '))
    b = float(input('Digite o segundo número para a multiplicação: '))
    print(f'{a} x {b} = {a * b}')
def div():
    a = float(input('DIgite o primeiro número para a divisão: '))
    b = float(input('Digite o segundo número para a divisão: '))
    pergunta = input('Você quer fazer que a divisão tenha resto 0 sempre ou não? (Sim ou Não): ')
    if pergunta == 'Sim':
        print(f'{a} / {b} = {a // b}')
    else:
        print(f'{a} / {b} = {a / b}')
print('Vamos fazer uma calculadora!')
resposta = input('''Escolha qual tipo de operação você quer fazer, siga a tabela:

Adição = +
Subtração = -
Multiplicação = x
Divisão = /

Digite: ''')

if resposta == '+':
    soma()
elif resposta == '-':
    sub()
elif resposta == 'x':
    mult()
elif resposta == '/':
    div()
else:
    print('ERRO')
