# Tratando uma exceção geral
def Divisao(valor1, valor2):
    result = valor1 / valor2
    print(result)
    
try:
    numero2 = 0
    Divisao(1, numero2)
except:
    print("Numero invalido")
    
# Tratando uma exceção específica
def Divisao(valor1, valor2):
    result = valor1 / valor2
    print(result)

try:
    numero2 = "e"
    Divisao(1, numero2)
except NameError:
    print("caracteres devem ser numeros")
except:
    print("Numero invalido")