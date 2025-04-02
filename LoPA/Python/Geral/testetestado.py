temp_F = float(input('Digite o valor em Fahrenheit: '))
temp_C1 = (temp_F - 32) * (5/9)
temp_C2 = (temp_F - 32) * 0.5
print(f'Seus resultados foram %.2fºC e %ºC' % temp_C1, temp_C2)
