""" Aula 06 - Conversão de Tipos """

# Conversão de tipo implícita e explícita

# Conversão implícita

leitura = 5.53
peso = 3

total = leitura + peso
print(total, type(total))

# Conversão explícita (type casting)
soma = 3.4 + float('3.5') 
print(soma, type(soma))

idade = int('32')
print(idade, type(idade))

nome = 'Maria'
altura = 1.7

# mensagem = nome + ' tem altura de ' + str(altura) + ' metros'
mensagem = f'{nome} tem altura de {altura} metros'
print(mensagem)

