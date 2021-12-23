class Pessoa():

    def __init__(self):
        self.nome = "Ernane"
        print("Construtor chamado para criar um objeto desta classe")

    def imprime(self, nome):
        print("Essa pessoa se chama %s" %nome)

Pessoa1 = Pessoa()

print(Pessoa1.nome)



class Pessoa0():

    def __init__(self, nome):
        self.nome = nome
        print("Construtor chamado para criar um objeto desta classe")

    def imprime(self, nome):
        print("Essa pessoa se chama %s" %nome)

Pessoa1 = Pessoa0("Ernane")

Pessoa1.imprime(Pessoa1.nome)