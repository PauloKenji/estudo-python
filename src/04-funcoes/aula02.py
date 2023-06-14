""" Aula 02 - Argumentos: positional, keyword, default value """

# declara uma funcao que soma dois numeros

def somar (n1, n2):
    return n1 + n2

def dividir(dividendo, divisor):
    return dividendo / divisor

# argumentos posicionais
print(somar(10, 20))
print(dividir(10, 2))

# argumentos nomeados (keyword arguments)
print(somar(n2=10, n1=20))
print(dividir(divisor=3, dividendo=10))

# unpack list e unpack tuple

numeros = (10, 20)
print(somar(numeros[0], numeros[1]))
print(somar(*numeros))

# unpack dict (keyword arguments)
numeros = {
    'n1': 10,
    'n2': 20
}

print(somar(numeros['n1'], numeros['n2']))
print(somar(**numeros))

# default value
# nome: hello
# parametros: nome, saudacao
# corpo: print(saudacao, nome)
# retorno: string

def hello(nome, saudacao='oi'):
    return f'{saudacao}, {nome}'

print(hello('Guilherme', 'Olá'))
print(hello('João', 'Oi'))
print(hello('Pedro'))

print(hello(nome='Maria', saudacao='Olá'))
print(hello(nome='Maria'))
