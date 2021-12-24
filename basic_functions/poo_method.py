class quadrado():

    def __init__(self, lado):
        self.lado = lado

    def area(self,):
        return (self.lado * self.lado)

    def setLado(self, novo_lado):
        self.lado = novo_lado

    def getLado(self):
        return self.lado

Quadradinho = quadrado(2)

Quadrado = quadrado(4)

print('Area igual a: ', Quadradinho.area())

print('Area igual a: ', Quadrado.area())

class quadrado():

    def __init__(self, lado):

        self.lado = lado 

    def area(self):

        return (self.lado * self.lado)

    def setLado(self, novo_lado):

        self.lado = novo_lado

    def getLado(self):

        return self.lado

Quadradinho = quadrado(2)

Quadrado = quadrado(3)

print('Lado igual a: ', Quadradinho.area())

print('Lado igual a: ', Quadrado.area())

Quadradinho.setLado(3)

Quadrado.setLado(5)

print('Novo lado igual a: ', Quadradinho.area())

print('Novo lado igual a: ', Quadrado.area())

print(Quadradinho.getLado())



class Pessoa():

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade    

    def __str__(self):
        return "Nome: %s ,idade: %s " %(self.nome, self.idade)

    def __len__(self):
        return self.idade    

    def len(self):
        return print("Idade da pessoa: ", self.idade)

Pessoa1 = Pessoa("Ernane", 21)
print(Pessoa1)
print(str(Pessoa1))

class Pessoa():

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return "Nome: %s ,idade: %s " %(self.nome, self.idade)

    def __len__(self):
        return self.idade

    def len(self):
        return print("Idade da pessoa: ", self.idade)

Pessoa1 = Pessoa("Ernane", 21)
print(len(Pessoa1))
Pessoa1.len()

class Pessoa():

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return "Nome: %s ,idade: %s " %(self.nome, self.idade)

    def __len__(self):
        return self.idade

    def len(self):
        return print("Idade da pessoa: ", self.idade)

Pessoa1 = Pessoa("Ernane", 21)
print(hasattr(Pessoa1, "idade"))
del Pessoa1.idade
print(hasattr(Pessoa1, "idade"))