print('Vamos transformar as temperaturas!')
temp_c = float(input('Me diga uma quantidade de graus em Celsius: '))
temp_f = temp_c * 1.8 + 32
temp_k = temp_c + 273
print('Sua temperatura em Fahrenheit é de: ', temp_f)
print('Sua temperatura em Kelvin é de: ', temp_k)



print("Agora vamos calcular sua quantidade de graus Fahrenheit!")
temp_f1 = float(input('Me diga uma quantidade de graus em Fahrenheit: '))
temp_c1 = (temp_f1 - 32) * 0.55
temp_k1 = (temp_f1 -  32) * 0.55 + 273
print('Sua temperatura em graus Celsius é de: ', temp_c1)
print('Sua temperatura em graus Kelvin é de: ', temp_k1)



print("Agora vamos calcular sua quantidade de graus Kelvin.")
temp_k2 = float(input('Me diga uma quantidade de graus em Kelvin: '))
temp_f2 = (temp_k2 - 273) * 1.8 + 32
temp_c2 = temp_k2 - 273
print('Sua temperatura em graus Celsius é de: ', temp_c2)
print('Sua temperatura em graus Fahrenheit é de: ', temp_f2)
    
