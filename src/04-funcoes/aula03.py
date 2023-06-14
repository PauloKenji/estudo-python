""" Aula 03 - *args e **kwargs """

# *args é um parâmetro em Python que permite que 
# uma função receba um número variável de argumentos 
# posicionais em forma de tupla.

def world_cup_titles(country, *args):
    print('Country: ', country)
    for title in args:
        print('year: ', title)

world_cup_titles('Espanha', '2010')
world_cup_titles('Brasil', '1958', '1962', '1970', '1994', '2002')

# **kwargs é um parâmetro em Python que permite que
# uma função receba um número variável de argumentos
# nomeados em forma de dicionário.

def calculate_price(value, **kwargs):
    tax_percentage = kwargs.get('tax_percentage')
    discount = kwargs.get('discount')
    if tax_percentage:
        value += value * (tax_percentage / 100)
    if discount:
        value -= discount
    return value

print(calculate_price(100, tax_percentage=10, discount=10))
print(calculate_price(100, tax_percentage=10))
print(calculate_price(100, discount=10))
