# criando set
set1 = set(['a','b','c'])
print(set1)
# também pode ser criado com {}, exemplo:
# set1 = {'a','b','c'}

# adicionando elemento ao set
set1.add('d')
print(set1)

# removendo elemento do set
set1.discard('b')
print(set1)

# diferenças entre set normal e frozen set
set_normal = (['a','b','c'])
print('Set normal: ', set_normal)

# frozen set não possibilita alteração
frozen_set = frozenset(['d','e','f'])
print("\nFrozen set: ", frozen_set)

frozen_set.add('h')

# união de dois sets
pessoas1 = {'Ana', 'Bianca', 'Carla', 'Daniela'}
pessoas2 = {'Érika', 'Flávia', 'Gabriella', 'Hannah'}