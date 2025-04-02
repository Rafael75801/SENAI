"""
9 - Construa um algoritmo para determinar se o indivíduo esta com um peso favorável.
Essa situação é determinada através do IMC (Índice de Massa Corpórea), que é definida como
sendo a relação entre o peso (PESO) e o quadrado da Altura (ALTURA) do  indivíduo. Ou seja,
"""
print('Vamos calcular sua situação de acordo com a calculadora IMC')
peso = float(input('Me informe seu peso: '))
altura = float(input('Me informa sua altura: '))
calculo = peso // (altura ** 2)
if calculo < 20:
    print('Sua situação é de estar abaixo do peso')
elif calculo >= 20 and calculo < 25:
    print('Sua situação e peso normal')
elif calculo >= 25 and calculo < 30:
    print('Sua situação e acima do peso')
elif calculo >= 30 and calculo < 40:
    print('Sua situação e de obesidade')
elif calculo >= 40:
    print('Sua situação e de obesidade mórbida, procure um médico.')
