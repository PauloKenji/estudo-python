""" Aula 01- Tipo de Dados - Listas """

# lista
# ordenadas
# mutáveis
# indexaveis

# criação da lista
nomes = ['Guilherme', 'João', 'Maria', 'Ana']
print(nomes, type(nomes))

print(nomes[0])
print(nomes[0:2])
print(nomes[:2])
print(nomes[1:])

# alterando valores
nomes[0] = 'Guilherme Silveira'
nomes[1:] = ['João da Silva', 'Maria da Silva']
print(nomes)

# tamanho da lista
tamanho = len(nomes)
print(tamanho)

# adicionar elementos na lista

nomes.append('Marta Gomes')
print(nomes)

# metodo insert

nomes.insert(2, 'José')
print(nomes)

# metodo extend
print(len(nomes))
nomes2 = ['Caio Silva', 'Carlos Gomes']
nomes.extend(nomes2)
print(len(nomes))
print(nomes)

# remover elementos

# remove

nomes.remove('José')
print(nomes)

# del

del nomes[0]
print(nomes)	

# del nomes
# print(nomes) # NameError

# limpar lista
# clear

# nomes.clear()
print(nomes)

# iterar sobre listas
for nome in nomes:
    print(nome)

for i in range(len(nomes)):
    print(nomes[i])