""" exercicio 02 - input do numero do mes e exibir o nome do mes ( tupla )"""

numeros_mes = input('Digite o número do mês: ')

nomes_meses = (
    'janeiro',
    'fevereiro',
    'março',
    'abril',
    'maio',
    'junho',
    'julho',
    'agosto',
    'setembro',
    'outubro',
    'novembro',
    'dezembro'
)

print(f'O mês é {nomes_meses[int(numeros_mes) - 1]}')
print(type(nomes_meses))