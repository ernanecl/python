# Acessando elementos individualmente de uma lista
lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista1[0], lista1[2])


# Acessando listas de trás para frente
lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista1[-1], lista1[-3])


# Usando slicing em listas
lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista1[1:])   # A partir do segundo elemento
print(lista1[:-1])  # Até o último elemento
print(lista1[1:-1]) # Menos o primeiro e o último elementos


# Usando o método append()
lista2 = [34, 54, 2, 0, 2324, 4, -2]
lista2.append(100)
print(lista2)


# Usando o método count()
lista2 = [34, 54, 2, 0, 2324, 4, -2, 0]
contar = lista2.count(0)
print(contar, lista2.count(0))


# Usando o método sort()
lista2 = [34, 54, 2, 0, 2324, 4, -2]
lista2.sort()
print(lista2)


# Usando o método sort() de forma reversa
lista2 = [34, 54, 2, 0, 2324, 4, -2]
lista2.sort(reverse=True)
print(lista2)


# Usando o método remove()
lista2 = [34, 54, 2, 0, 2324, 4, -2]
lista2.remove(0)
print(lista2)


# Usando o método clear()
lista2 = [34, 54, 2, 0, 2324, 4, -2]
lista2.clear()
print(lista2)


# Usando len para verificar o tamanho de uma lista
lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2 = [34, 54, 2, 0, 2324, 4, -2]
print(len(lista1))
print(len(lista2))