""" exercicio 01 -  recebe uma tupla de números como parâmetro
(numeros) e retorna a soma dos números """

numeros = (10, 20, 30)

def somar(numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

print(somar(numeros))