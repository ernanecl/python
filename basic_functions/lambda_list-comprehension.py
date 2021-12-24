 #LAMBDA
def f(x):
    print(x**2)
f(10)
g = lambda x : print(x**2)
g(10)
     
nomeCompleto = lambda nome,sobrenome: print("Nome completo:", nome, sobrenome)
nomeCompleto('Leonardo','Ferrari')

# LIST COMPREHENSION
numeros = range(100)
lista_lc = [n for n in numeros if n % 2 == 0]
print(lista_lc)

numeros = range(100)
lista_fun = []
def pares(x):
    for el in x:
        if x[el]%2 == 0:
            lista_fun.append(x[el])
    print(lista_fun)
pares(numeros)

potencia = [i * i for i in range(10)]
print(potencia)