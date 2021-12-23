class Pessoa():

    def __init__(self, nome):
        self.nome = nome        

    def imprime(self, nome):
        print("Essa pessoa se chama %s" %nome)        


Pessoa1 = Pessoa("Ernane")

print(getattr(Pessoa1, "nome"))



class Pessoa0():

    def __init__(self, nome):
        self.nome = nome        

    def imprime(self, nome):
        print("Essa pessoa se chama %s" %nome)


Pessoa1 = Pessoa0("Ernane")

print(hasattr(Pessoa1, "nome"))



class Pessoa2():

    def __init__(self, nome):
        self.nome = nome        

    def imprime(self, nome):
        print("Essa pessoa se chama %s" %nome)


Pessoa1 = Pessoa2("Ernane")

setattr(Pessoa1, "nome", "Tony")



class Pessoa3():

    def __init__(self, nome):
        self.nome = nome        

    def imprime(self, nome):
        print("Essa pessoa se chama %s" %nome)        


Pessoa1 = Pessoa3("Ernane")

setattr(Pessoa1, "nome", "Tony")

print(getattr(Pessoa1, "nome"))



class Pessoa4():

    def __init__(self, nome):
        self.nome = nome        

    def imprime(self, nome):
        print("Essa pessoa se chama %s" %nome)

Pessoa1 = Pessoa4("Ernane")

print(delattr(Pessoa1, "nome"))