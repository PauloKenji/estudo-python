""" exercicio 02 - calculo de média e situação do aluno """

notas = input('notas ex(n1, n2, ...): ').split(', ')

media = sum(float(nota) for nota in notas) / len(notas)

print("Média: ", media)

# aprovado (maior que 6.0), recuperação (entre 4.0 e 6.0) e reprovado (menor que 4.0)
if media > 6:
    print('Aprovado')
elif media >= 4:
    print('Recuperação')
else:
    print('Reprovado')
