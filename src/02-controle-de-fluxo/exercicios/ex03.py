""" exercicio 03 - validação de indentificador """

identificador = input('Identificador: ')
NUMERO_IDENTIFICADOR = ""

for caractere in identificador:
    if caractere.isdigit():
        NUMERO_IDENTIFICADOR += caractere

if len(identificador) != 7:
    print('Identificador inválido')
elif not identificador.startswith('BR'):
    print('Identificador inválido')
elif not identificador.endswith('X'):
    print('Identificador inválido')
elif not identificador[2:6].isdigit(): # ex:BR0Y01X tem que ser inválido
    print('Identificador inválido')
elif not 1 <= int(NUMERO_IDENTIFICADOR) <= 9999:
    print('Identificador inválido')
else:
    print('Identificador válido')
