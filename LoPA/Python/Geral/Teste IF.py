print('Vamos descobrir se você está apto a tirar sua habilitação')
idade = int(input('Me diga sua idade para começarmos: '))
if idade > 17:
    aulas = int(input('Me diga quantas aulas você já fez para tirar sua habilitação: '))
    if aulas <= 20:
        print('Você tem que terminar suas aulas')
    else:
        print('Você pode começar em breve o seu exame pra tirar sua CNH')
else:
    print('Você ainda não pode tirar sua habilitação')
