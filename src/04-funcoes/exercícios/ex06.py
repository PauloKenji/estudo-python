""" exercicio 06 - calculadora aquário """

aquario = {
    'comprimento': float(input('Digite o comprimento: ')),
    'altura': float(input('Digite a altura: ')),
    'largura': float(input('Digite a largura: '))
}

temperatura = {
    'desejada': float(input('Digite a temperatura desejada: ')),
    'ambiente': float(input('Digite a temperatura ambiente: '))
}

def calcular_volume(aquario):
    return (aquario['comprimento'] * aquario['altura'] * aquario['largura']) / 1000


def calcular_potencia_termostato(aquario, temperatura):
    return calcular_volume(aquario) * 0.5 * (temperatura['desejada'] - temperatura['ambiente'])

def calcular_filtragem_hora(aquario):
    return calcular_volume(aquario) * 2, calcular_volume(aquario) * 3

print(f'Volume é {calcular_volume(aquario)} litros')
print(f'Potência do termostato deve ser de {calcular_potencia_termostato(aquario, temperatura)}')
print(f'Filtragem por hora deve ser pelo menos {calcular_filtragem_hora(aquario)[0]} litros a {calcular_filtragem_hora(aquario)[1]} litros')
