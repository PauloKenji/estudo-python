""" Aula 01 - introdução a funções """

# Função é um bloco de que realiza uma tarefa específica
# dividir o problema em pequenas partes
# evitar repetição de código

# 1. Standard library functions - built-in functions
# ex. print(), input(), len(), type(), int(), float(), str(), list(), dict(), etc.

print('Hello World')

nomes = ['Guilherme', 'João', 'Maria']
tamanho_lista = len(nomes)
print(nomes, tamanho_lista)

# 2. User-defined functions
# Definidas pelo desenvolvedor
# Fazerem parte da solução do problema

# Declara
# nome da função: hello
# parâmetros: nenhum	
# corpo: print('Hello World')
# retorno: nenhum

def hello():
    print('Hello World')

# chamada
hello()
hello()
hello()

# Declara
# nome da função: hello
# parâmetros: nome	
# corpo: print('Hello World')
# retorno: nenhum

def hello(nome):
    print(f'Hello {nome}')

# chamada
# valores, variáveis, expressões => argumentos
# 'Maria' é um argumento para o parâmetro nome
hello('Guilherme')
hello('João')
nome = 'Maria'
hello(nome)

# Declara
# nome da função: calcular_media
# parâmetros: nota1, nota2, nota3
# corpo: calcular a média
# retorno: nenhum
def calcular_media(nota1,nota2,nota3):
    media = (nota1 + nota2 + nota3) / 3
    print(f'A média é {media}')

# chamada	
# argumentos litarais
calcular_media(10,9,8)
n1 = 10
n2 = 9
n3 = 8
# argumentos variáveis
calcular_media(n1,n2,n3)

# Declara
# nome da função: calcular_media
# parâmetros: nota1, nota2, nota3
# corpo: calcular a média
# retorno: média
def calcular_media(nota1,nota2,nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

media = calcular_media(10,9,8)
print(f'A média é {media}')
# enviar no email
# salvar em um arquivo
# enviar para um banco de dados

