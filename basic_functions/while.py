numero_impar = 0
counter = 0
list = []

# este programa le e imprime 4 valores impares em uma lista

while (counter < 4):
    numero_impar = int(input('digite um numero impar:'))
    if (numero_impar%2!=0):
        list.append(numero_impar)
        counter+=1
    else:
        pass
print("list: ", list)