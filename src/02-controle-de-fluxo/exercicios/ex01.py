""" Exercício 01 - média de notas """

notas = []

for i in range(3):
    notas.append(int(input(f'Informe a {i+1}ª nota: ')))

media = sum(notas) / len(notas)
print( media )
