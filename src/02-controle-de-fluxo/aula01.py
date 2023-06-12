""" Aula 01 - Operadores """

# Operadores aritméticos

n1 = 10.2
n2 = 3.5
resultado = n1 + n2 + 8.5

print(' 1 + 1 ', 1 + 1, type(1 + 1))
print('1.2 + 1.3', 1.2 + 1.3, type(1.2 + 1.3))
print(f'resultado: {resultado} - {type(resultado)}')
print(3-1)
print(3*2, type(3*2))
print(3/2, type(3/2))
print(3 % 3)
print(10 // 3)
print(10 ** 3)

# operador atribuição

numero_x = 10.0
print(numero_x)

# operadores de comparação

resultado = numero_x > 10
print(resultado, type(resultado))

if numero_x > 20.0:
    print('numero_x é maior que 20')

print('10 == 10',10 == 10, type(10 == 10))
print('10 != 10',10 != 10, type(10 != 10))
print('10 > 10',10 > 10, type(10 > 10))
print('10 >= 10',10 >= 10, type(10 >= 10))
print('10 < 10',10 < 10, type(10 < 10))
print('10 <= 10',10 <= 10, type(10 <= 10))

# condicao = numero_x > 10.0 and resultado < 3.0

# if condicao:
#     pass

# operadores lógicos	

print("True and True", True and True, type(True and True))
print("True and False", True and False, type(True and False))
print("False and True", False and True, type(False and True))
print("False and False", False and False, type(False and False))

print("True or True", True or True, type(True or True))
print("True or False", True or False, type(True or False))
print("False or True", False or True, type(False or True))
print("False or False", False or False, type(False or False))

condicao = False

print('not condicao', not condicao, type(not condicao))

# Operadores especiais

# is
# == comprar se dois valores são iguais
# is verificar se as variaveis apontam para o objeto em memória

a = 10
b = 10.0
c = b

print(a == b, a == c, b == c)
print(a is b, a is c, b is c)

# in
# str, list, touple, set, dic (chave)

frase = 'você é um palavrão!'
print('palavrão' in frase,type('palavrão' in frase))
print('Palavrão' in frase,type('palavrão' in frase))


# mesmo comportamento para listas, tuplas e sets
numeros = [1,5,2,6]
print(1 in numeros, type(1 in numeros))

pessoa = {
    'nome': 'João',
    'idade': 20,
    'email': 'João@email.com',
}

print('nome' in pessoa, type('nome' in pessoa))