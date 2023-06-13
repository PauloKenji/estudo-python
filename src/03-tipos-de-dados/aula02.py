""" Aula 02 - Tipos de dados - Tuplas """

# tuplas
# ordenadas
# imutáveis
# indexaveis

# criação da tupla
nomes = ('Guilherme', 'João', 'Maria', 'Ana')
print(nomes, type(nomes))

#acessando elementos
print(nomes[0])
print(nomes[0:2])
print(nomes[:2])
print(nomes[1:])

#modificando valores ( não é possível por ser imutável)
# nomes[0] = 'Guilherme Silveira' # TypeError

# iterando sobre uma tupla
for nome in nomes:
    print(nome)
print('------------------')
for i in range(len(nomes)):
    print(nomes[i])

nomes2 = 'Ana', 'Carlos', 'Caio'
print(nomes2, type(nomes2))

# desempacotamento de tuplas (unpacking)

# nome1 = nomes2[0]
# nome2 = nomes2[1]
# nome3 = nomes2[2]
# nome1, nome2 = nomes2 # too many values to unpack (expected 2)
nome1, nome2, nome3 = nomes2

print(nome1, nome2, nome3)


# juntas duas tuplas

todos_nomes = nomes + nomes2
print(todos_nomes)