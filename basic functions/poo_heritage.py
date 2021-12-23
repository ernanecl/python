class Refeicao():    

    def __init__(self):
        print("Refeicao criada")

    def Identif(self):
        print("Refeicao")

    def comer(self):
        print("Comendo")


class Almoco(Refeicao):

    def __init__(self):
        Refeicao.__init__(self)
        print("Objeto Almoco criado")

    def Identif(self):
        print("Almoco")

    def servir(self):
        print("Almoco servido")


class cafe(Refeicao):    

    def __init__(self):
        Refeicao.__init__(self)
        print("Objeto cafe criado")

    def Identif(self):
        print("cafe")

    def servir(self):
        print("Cafe servido")


cafeManha = cafe()
cafeManha.servir()
cafeManha.comer()

Almoco = Almoco()
Almoco.servir()
Almoco.comer()