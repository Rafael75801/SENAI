print('Vamos fazer a conversão de Fahrenheit para Celsius!')
temp_F = float(input('Me informe a temperatura em Fahrenheit: '))
def converter_para_celsius():
    global temp_F
    converter = (temp_F - 32) * 0.5
    return converter
    # print('Sua temperatura em Celsius é: %.2fºC)' % converter)
print(f'O resultado da conversão é: {converter_para_celsius()}')
