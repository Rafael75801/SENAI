print('Vou te ajudar a ver o preço do seu aluguel do carro')
dis=int(input('Me diga a distância que você percorreu com seu carro: '))
dias=int(input('Me diga a quantidade de dias que você ficou com o seu carro alugado: '))
dias_calculo = dias + 60
dis_calculo = dis * 0.15
resultado= dias_calculo + dis_calculo
print('O valor total que você terá que pagar e de: ', resultado, 'reais')
