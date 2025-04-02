print('Vamos calcular a temperatura')

temperatura = float(input('Me diga a temperatura atual em Graus Celsius (ºC): '))

if temperatura <= 15:
    print(f'Muito frio, se loco, {temperatura}ºC? Tá congelando')
elif tempreatura <= 23:
    print(f'Frio, pega coberta ai porque {temperatura}ºC tá bom.')
elif temperatura <= 26:
    print(f'Agradável, dá até pra pegar uma cobertinha nesse clima de {temperatura}ºC')
elif temperatura <= 30:
    print(f'Quente, ta maluco {temperatura}ºC, não pode piorar não.')
else:
    print(f'Muito quente, {temperatura}ºC, se loco')
