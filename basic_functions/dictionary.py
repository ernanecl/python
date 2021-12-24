'''
Dicionários
Sempre definido com chaves '{}', contendo a chave e valor, sendo separados por dois pontos ':'
As chaves dos dicionarios sao imutaveis, entao nao podemos fazer uma chave como lista
'''

# Definindo e imprimindo um dicionário
estudantes = {'Jonas': 20, 'Pedro': 22, 'Leticia': 25}
print(estudantes)

# Acessando um item(valor) do dicionário
# dictionary[key] busca o valor da chave correspondente
estudantes = {'Jonas': 20, 'Pedro': 22, 'Leticia': 25}
print(estudantes['Jonas'])

# Visualizando as chaves de um dicionário
# dicionário.keys()
estudantes = {'Jonas': 20, 'Pedro': 22, 'Leticia': 25}
print(estudantes.keys())

# Visualizando os valores de um dicionário
# dicionário.values()
estudantes = {'Jonas': 20, 'Pedro': 22, 'Leticia': 25}
print(estudantes.values())

# Adicionando itens num dicionário
# dicionário['novo item'] = 'novo valor'
estudantes = {'Jonas': 20, 'Pedro': 22, 'Leticia': 25}
estudantes['Carlos'] = 23
print(estudantes)

# Adicionando usando o método update
# dicionário.update({'chave': 'valor', ...})
estudantes = {'Jonas':20, 'Pedro': 22, 'Beto': 25}
estudantes.update({'Isadora': 21, 'Carlos': 23})
print(estudantes)

# Se uma chave já estiver inserida dentro do dicionário, ela irá receber o novo valor atribuído
estudantes = {'Jonas': 20, 'Pedro': 23, 'Leticia': 25}
estudantes['Pedro'] = 26
print(estudantes)

# Removendo um item de um dicionário
# del dicionario['item']
estudantes = {'Jonas': 20, 'Pedro': 22, 'Leticia': 25}
del estudantes['Pedro']
print(estudantes)

# Removendo usando o método pop(), metodos usamos () e nao {}
# dicionario.pop('chave')
estudantes = {'Jonas': 20, 'Pedro': 22, 'Leticia': 25}
estudantes.pop('Jonas')
print(estudantes)

# Removendo todos os elementos de um dicionário (Método clear())
# dicionario.clear()
estudantes = {'Jonas': 20, 'Pedro': 22, 'Leticia': 25}
estudantes.clear()
print(estudantes)

# Copiar um dicionário (método copy())
# dicionario.copy()
estudantes = {'Jonas': 20, 'Pedro': 22, 'Leticia': 25}
alunos = estudantes.copy()
print(estudantes)
print(alunos)

# Um dicionário pode receber diversos tipos
dic = {50 : 'numero', 3.14 : '1pi', False : 0, 'lista': [1,2,3,4]}
print(dic)

# Um dicionário, no entanto, não pode ter chaves repetidas.
# A chave repetida é ignorada, mas o valor é atualizado
estudantes = {'Jonas': 20, 'Pedro': 22, 'Leticia': 25, 'Jonas': 26}
print(estudantes)

# As chaves de um dicionário não podem ser de objetos mutáveis

# Usando tuplas como chaves
dicionario1 = {(1, 1): 'a', (1, 2): 'b', (2, 1): 'c', (2, 2): 'd'}
print(dicionario1)

# Usando listas como chaves
dicionario2 = {[1, 1]: 'a', [1, 2]: 'b', [2, 1]: 'c', [2, 2]: 'd'}
print(dicionario2)      