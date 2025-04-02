print('Vamos fazer a conversão de Fahrenheit para Celsius!')
temp_F = float(input('Me informe a temperatura em Fahrenheit: '))
def converter_para_celsius():
    global temp_F
    converter = (temp_F - 32) * 0.5
    print('Sua temperatura em Celsius é: %.2fºC)' % converter)
converter_para_celsius()
