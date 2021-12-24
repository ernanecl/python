# Biblioteca (Library)
# Para utilizar uma biblioteca, deve-se usar import
import math

# Utilizando um método da biblioteca
print(math.sqrt(100))

# Para importar uma função específica
from math import sqrt

# Ao importar um método de uma biblioteca, não é necessário utilizar o nome do módulo para utilizar a função
print(sqrt(100))

# Visualizando todos os métodos e atributos de uma biblioteca
import math
print(dir(math))

# Para saber o que um método faz
import math
help(math.sqrt)

from math import sqrt
help(sqrt)