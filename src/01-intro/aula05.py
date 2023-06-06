""" aula 05 - Tipos de dados """

# Númericos
# int, float

idade = 20
peso = 70.5

print(idade, type(idade))
print(peso, type(peso))

# String

nome = 'Maria'
sobrenome = "Silva"
nome_completo = nome + ' ' + sobrenome

produto = 'Notebook'

print(f'O cliente {nome_completo} comprou um {produto}')

print(nome[0], nome[1], nome[-1])

print(nome.lower())
print(nome.upper())

print(1,3,7,"aaaaa", sep='-', end='')

# Booleanos
ligado = True
print(ligado, type(ligado))
print(True, type(True))

resultado = 10 > 20
print(resultado, type(resultado))

# Lista

frutas = ['banana', 'maçã', 'uva', 'morango', 'abacaxi']
print(frutas)
print(frutas[0], frutas[1], frutas[2])
# print(frutas[10]) # IndexError: list index out of range´

frutas[0] = 'banana nanica'
frutas.append('melancia')
print(frutas)
print(len(frutas))

for fruta in frutas:
    print(fruta.upper())

# Tuplas

codigos = ('SP01','SP02','SP03')
print(codigos[0])

#codigos[0] = 'sp04' # TypeError: 'tuple' object does not support item assignment
print(len(codigos))

# Conjuntos (set)

resultado_sorteio = {10,4,3,55,9}
print(resultado_sorteio)

resultado_sorteio.add(20)
print(resultado_sorteio)

# dicionario

funcionario = {
    'codigo': 123,
    'nome': 'Maria da Silva',
    'salario': 7000.00
}

print(funcionario)
print(funcionario['codigo'])
print(funcionario['nome'])
print(funcionario['salario'])

print(funcionario.keys())   
print(funcionario.values())

funcionario['salario'] = 10000.00
print(funcionario)



