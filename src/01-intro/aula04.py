""" aula 04 - Variaveis, Constantes e Literais """

# Variáveis container para armazenar valores
# inferência de tipo

numero = 10
print(numero, type(numero))

# alturar o valor de uma variavel

numero = 20
print(numero, type(numero))

# multiplas atribuições

nome, idade, endereco = 'Maria', 20, 'Rua 1'

print(nome, idade, endereco)

nome = 'Maria'
idade = 20
endereco = 'Rua 1'

print(nome, idade, endereco)

# atribuir o mesmo valor para várias variaveis

nome_1 = nome_2 = nome_3 = 'João'
print(nome_1, nome_2, nome_3)

nome_2 = 'Pedro'
print(nome_1, nome_2, nome_3)

# Variáveis
# snake_case

id_funcionario = 209
salario_atual = 5000.00

print(id_funcionario, salario_atual)

# Constantes
# UPPER_CASE snake_case

PI = 3.1415
GRAVIDADE = 9.8
MAIORIDADE_CIVIL = 21
MAIORIDADE_PENAL = 18

print(PI, GRAVIDADE, MAIORIDADE_CIVIL, MAIORIDADE_PENAL)

# Literais

idade = 27
print(idade)
print(27)

# Númericos

print(10, type(10))
print(10, type(-10))
print(10.5, type(10.5))

# String

print('Maria', type('Maria'))
print("Maria", type("Maria"))
print("Jhon's house")
print('O filme estava "excelente"')

# Booleanos

print(True, type(True))
print(False, type(False))

# None
print(None, type(None))

# coleções

# Listas (list)

numeros = [10, 20, 30, 40, 50]
print(numeros, type(numeros))

# Tuplas (tuple)

emails = ('joao@email.com','maria@emal.com')
print(emails, type(emails))
    
# Conjuntos (set)

nomes = {'João', 'Maria', 'Pedro', 'João'}

print(nomes, type(nomes))

# Dicionários (dict)

aluno = {
    'prontuario' : 123456,
    'nome' : 'João',
    'idade': 20,
}

print(aluno, type(aluno))
