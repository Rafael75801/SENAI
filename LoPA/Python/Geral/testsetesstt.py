def conta_vogais(string): 
    string = string.lower() # para que a comparação não seja sensível a maiuscula/minuscula 
    result = {} 
    vogais = 'aeiou' 
    for i in vogais: 
        if i in string: 
            result[i] = string.count(i) 
    return result 
 
print(conta_vogais(input('Digite uma palavra para eu contar as vogais: '))) 
