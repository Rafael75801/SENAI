print('Vamos fazer alguns calculos de velocidade de um veiculo')
velocidade = int(input('Me diga a velocidade do seu veículo: '))
multa = (velocidade - 80) * 5
if velocidade > 81:
    print('Você foi multado em:', multa)
else:
    print('Você não ultrapassou a velocidade')
