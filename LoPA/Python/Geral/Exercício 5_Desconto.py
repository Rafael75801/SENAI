print("Me diga um valor de uma mercadoria que eu vou calcular ela com algum desconto!")
preço = float(input("Me diga o valor da mercadoria para começarmos: "))
a_descontar = int(input('Me diga o valor do desconto: '))
preço_desconto = preço * a_descontar / 100
preço_final = preço - preço_desconto
print('O seu produto com desconto fica: ', preço_final)
