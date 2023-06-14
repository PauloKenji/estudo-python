""" exercicio 01 - recebe vários argumentos numéricos através
do *args retorna a soma dos números """

numeros = [10, 20, 30]
numeros2 = [40, 50, 60, 70, 80, 90]


def somar(*args): # forma mais flexível, com return e *args
    soma = 0
    for numero in args:
        soma += numero
    return soma


print(somar(*numeros))
print(somar(*numeros2))
