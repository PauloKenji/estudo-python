""" Aula 03 - loop for """

# 1. Iterar sobre uma colecao
# 2. Repetir instrucao

linguagens = ['c','python','java']

print(linguagens[0])
print(linguagens[1])
print(linguagens[2])

# for <variavel> in <colecao>:
#     <instrucao>

for linguagem in linguagens:
    print(linguagem.upper())

# Comportamento do operador in é diferente com base no contexto
print('java' in linguagens)

nota1 = 10.0
nota2 = 5.5
nota3 = 8.3

media = (nota1+nota2+nota3)/3
print(media)

notas = [10.0, 5.5, 8.3]

soma = 0.0
for nota in notas:
    soma = soma + nota

media = soma / len(notas)
print(media)

# range(start, stop, step)
# valores = range(10)
# valores = range(0,10)
# valores = range(0,10,2)
valores = range(10,0,-1)

print(valores, type(valores))

for valor in valores:
    print(valor)

# errado!
for i in range(len(linguagens)):
    print(linguagem[i])