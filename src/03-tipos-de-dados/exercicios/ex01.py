""" exercício 01 - input de 3 numeros e exibir o maior e o menor """

lista_numeros = []

for i in range(3):
    lista_numeros.append(int(input('Digite um número: ')))

maior = None
menor = None

for numero in lista_numeros:
    if maior is None or maior < numero:
        maior = numero
    if menor is None or numero < menor:
        menor = numero

print(f'O maior número é {maior}')
print(f'O menor número é {menor}')