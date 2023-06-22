""" aula 01 - modularizacao """

from uteis import numeros

num = int(input('Digite um numero: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')