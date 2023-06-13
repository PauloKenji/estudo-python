""" 04 - Tipos de dados - Dicionários """

# dicionários
# key:value
# colecao de chave e valor
# key é única
# mutável

# criação de um dicionário
carro = {
    'marca': 'Toyota',
    'modelo': 'Supra MK4',
    'ano': 1993
}

print(carro, type(carro))

print(carro['marca'])
# pegar todas as chaves, valores e itens
print(carro.keys())
print(carro.values())
print(carro.items())

# verificar se uma chave existe
print('marca' in carro)

# adicionar chave/valor de forma dinâmica
carro['cor'] = 'preto'
print('cor' in carro)
print(carro, type(carro))

# remover chave/valor
marca = carro.pop('marca')
print(marca)
print(carro, type(carro))

# loop em dicionários
for key in carro: # pode melhorar para for key, value in carro.items():
    print(key, carro[key], type(carro[key]))

for value in carro.values():
    print(value)

for key in carro.keys(): # pode melhorar para for key in carro:
    print(key)

for key, value in carro.items():
    print(key, value)

# lista de dicionarios

aluno1 = {
    'nome': 'Guilherme',
    'email': 'Guilherme@email.com',    
    'notas': [10, 9, 8, 7, 6],
}

aluno2 = {
    'nome': 'João',
    'email': 'João@email.com',
    'notas': [10, 9, 8, 7, 6],
}

alunos = [
    aluno1,
    aluno2
]

for aluno in alunos:
    print(aluno['nome'], aluno['email'])
    for nota in aluno['notas']:
        print(nota)