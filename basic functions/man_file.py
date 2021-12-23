# Read
# Se o arquivo não existir no mesmo diretório que o código, ocorre um erro de arquivo não encontrado
arq = open('arquivo.txt','r')
dados = arq.read()
print("Leitura do Arquivo:\n" + dados)

# Write
# Se o arquivo não existir no mesmo diretório que o código, um novo de mesmo nome será criado
arq = open('arquivo.txt','w')
arq.write("Novo conteudo do arquivo")

# Verificando o arquivo após a escrita
arq = open('arquivo.txt','r')
dados = arq.read()
print("Arquivo apos escrita:\n" + dados)

# Append
arq = open('arquivo.txt','a')
arq.write("\nConteudo acrescentado")

# Verificando o arquivo após o append
arq = open('arquivo.txt','r')
dados = arq.read()
print(dados)

# Depois de terminar de manipular o arquivo, é necessário fechá-lo
arq.close()

# UTILIZANDO WITH OPEN
# Read
with open('arquivo.txt','r') as arq:
    dados = arq.read()
    print(dados)
    arq.close()
    
# Write
with open('arquivo.txt','w') as arq:
    arq.write("Novo conteudo do arquivo")
    
# ARQUIVOS EM OUTROS DIRETÓRIOS
# Sem especificar o diretório
arq = open('arquivo2.txt','r')
dados = arq.read()
print("Leitura do Arquivo:\n" + dados)

# Especificando o diretório
arq = open('C:/Users/user_name/Desktop/files/arquivo2.txt','r')
dados = arq.read()
print("Leitura do Arquivo:\n" + dados)