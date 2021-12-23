vetor = []

'''Armazenando os valores por meio do loop for'''
for i in range(5):
    valor = int(input("Insira um valor: "))
    vetor.append(valor)

'''Imprimindo os valores da lista "vetor"'''
print(vetor)

'''Mostrando os valores na ordem inversa com a função reverse'''
vetor.reverse()
print(vetor)