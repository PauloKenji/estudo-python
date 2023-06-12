""" exercicio 04 - validação de indentificador com lista de erros """

identificador = input('Identificador: ')
erros = []

NUMERO_IDENTIFICADOR = ""

for caractere in identificador:
    if caractere.isdigit():
        NUMERO_IDENTIFICADOR += caractere

if len(identificador) != 7:
    erros.append('O identificador não possui 7 caracteres')
if not identificador.startswith('BR'):
    erros.append('O identificador não inicia com a sequencias "BR"')
if not identificador.endswith('X'):
    erros.append('O identificador não finaliza com o caractere "X"')
if len(NUMERO_IDENTIFICADOR) != 4:
    erros.append('O identificador não apresenta números inteiros com formato de 4 digitos')
if not identificador[2:6].isdigit(): # ex:BR0Y01X tem que ser inválido
    erros.append('O identificador não apresenta números inteiros entre 0001 e 9999')
elif not 1 <= int(NUMERO_IDENTIFICADOR) <= 9999:
    erros.append('O identificador não apresenta números inteiros entre 0001 e 9999')

if erros:
    print(erros)
else:
    print('Identificador válido')
