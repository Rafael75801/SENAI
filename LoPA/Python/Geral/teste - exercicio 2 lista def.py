numero_principal = 0
divisao = 0
def perfeito(numero_principal, divisao):
    numero_principal = int(input("Diga aqui o valor do número e eu direi se ele é perfeito ou não! "))
    soma = 0
    for x in range(1, numero_principal):
        divisao = numero_principal % x
        if divisao == 0:
            soma = soma + x
        elif soma == numero_principal:
                return("número perfeito! ")
        else:
                return("não é um número perfeito")

print(perfeito(numero_principal, divisao))
