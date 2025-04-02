print('Vamos fazer uma calculadora!')
resposta = input('''Me diga uma conta para fazer, utilize:
Soma = +
Subtração = -
Multiplicação = *
Divisão = /

DIgite: ''')

if resposta == '+':
    def soma ():
        a = int(input('Digite um número para a soma: '))
        b = int(input('Digite outro número para a soma: '))
        return (a + b)
    print(soma())
elif resposta == '-':
    def sub ():
        a = int(input('Digite um número para a subtração: '))
        b = int(input('Digite outro número para a subtração: '))
        return (a - b)
    print(sub())
elif resposta == '*':
    def mult():
        a = int(input('Me diga um número a multiplicação: '))
        b = int(input('Me diga outro número a a multiplicação: '))
        return (a * b)
    print(mult())
elif resposta == '/':
    def div():
        a = int(input('Me diga um número para a divisão: '))
        b = int(input('Me diga outro número para a divisão: '))
        pergunta = input('Você quer que a conta tenha resto zero? (Sim ou Não): ')
        if pergunta == 'Sim':
            return (a // b)
        else:
            return (a / b)
    print(div())
else:
    print('ERRO')
