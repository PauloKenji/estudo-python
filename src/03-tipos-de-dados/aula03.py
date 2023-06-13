""" aula 03 - Tipos de Dados - sets """

# sets (conjuntos)
# não ordenados
# mutáveis
# não indexados
# não aceitam valores duplicados

# criação de um set

numeros = {1, 2, 11, 3, 4, 5, 6, 7, 8, 9, 10}
print(numeros, type(numeros))

for numero in numeros:
    print(numero)

print(3 in numeros)
print(14 not in numeros)

# adicionar elementos
numeros.add(11)
print(numeros)

# adicionar elementos de um set em outro set	
numeros2 = {1,2,3,4,12, 13, 14, 15}
numeros.update(numeros2)

print(numeros, type(numeros))
