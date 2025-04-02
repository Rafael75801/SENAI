print('Infelizmente as pessoas fumam... Vamos calcular o tempo de vida que eles perdem')
cigarros_dias= int(input('Me diga quantos cigarros por dia você fuma: '))
anos_fumados= int(input('Me diga por quantos anos você continuou a fumar: '))
quantidade_cigarros = cigarros_dias * 365 * anos_fumados
minutos_perdidos = quantidade_cigarros * 10 // 1440
print('Você perdeu: ', minutos_perdidos, 'dias por fumar')
print('Em anos, você perdeu: ', minutos_perdidos // 365)

