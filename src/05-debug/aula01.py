""" Aula 01 - Debug """

def somar(n1, n2, n3):
    soma = n1 + n2 + n3
    return soma

def calcular_media(n1,n2,n3):
    soma = somar(n1,n2,n3)
    media = soma / 3
    return media


breakpoint()
n1 = 10.0
n2 = 8.0
n3 = 9.0

media = calcular_media(n1,n2,n3)
print(media)