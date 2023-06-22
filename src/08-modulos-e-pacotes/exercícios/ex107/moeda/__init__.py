""" módulo moeda """

def metade(numero):
    return numero / 2

def dobro(numero):
    return numero * 2

def aumentar(numero, porcentagem):
    return numero + (numero * porcentagem / 100)

def diminuir(numero, porcentagem):
    return numero - (numero * porcentagem / 100)

def moeda(numero):
    return f'R$ {numero:.2f}'.replace('.', ',')