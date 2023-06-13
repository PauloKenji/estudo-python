""" exercicio 02 - input do numero do mes e exibir o nome do mes { dicionario } """

numeros_mes = int(input('Digite o número do mês: '))

nomes_meses = {
    1: 'janeiro',
    2: 'fevereiro',
    3: 'março',
    4: 'abril',
    5: 'maio',
    6: 'junho',
    7: 'julho',
    6: 'agosto',  
    9: 'setembro',
    10: 'outubro',
    11: 'novembro',
    12: 'dezembro'
}

print(f'O mês é {nomes_meses[numeros_mes]}')

nomes_meses = {
    'janeiro': 1,
    'fevereiro': 2,
    'março': 3,
    'abril': 4,
    'maio': 5,
    'junho': 6,
    'julho': 7,
    'agosto': 8,
    'setembro': 9,
    'outubro': 10,
    'novembro': 11,
    'dezembro': 12
}

for key, value in nomes_meses.items():
    if value == numeros_mes:
        print(f'O mês é {key}')
        break

print(type(nomes_meses))