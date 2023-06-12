""" Aula 05 - break e continue """

for i in range(10):
    if i == 4:
        break
    print(i)

# encontrar a posicao de um numero em uma lista de inteiros
# caso nao encontre posicao é igual a -1

busca = 5
numeros = [1, 4, 9, 5, 7, 3, 2, 3, 1, 7] 
posicao = -1

contador = 0
for numero in numeros:
    print("procurando na posicao: ", contador)
    if numero == busca:
        posicao = numeros.index(numero)
        break

print(posicao)

# for i in range(len(numeros)):
#     print("procurando na posicao: ", i)
#     if numeros[i] == busca:
#         posicao = numeros.index(i)
#         break

# print(posicao)

#continue
# pular a interação atua

for numero in numeros:
    if numero == 3:
        continue
    print("numero: ", numero)


