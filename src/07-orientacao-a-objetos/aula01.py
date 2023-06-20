""" Aula 01 - Introdução a Orientação a objetos """

# paradigma de programação

# calcular a área e o perímetro de um retangulo
# estrutura para armazenar os valores necessários para os calculos
# area = base * altura
# perimetro = 2 * (base + altura)


retangulo1={
    'base': 10.0,
    'altura': 5.0
}
retangulo2={
    'base': 6.0,
    'altura': 3.0
}

# realizar os calculos  
def calcular_area(retangulo):
    return retangulo['base'] * retangulo['altura']

def calcular_perimetro(retangulo):
    return 2 * (retangulo['base'] + retangulo['altura'])

print(calcular_area(retangulo1))
print(calcular_area(retangulo2))
print(calcular_perimetro(retangulo1))
print(calcular_perimetro(retangulo2))

# Classe representa um conceito
# Classe representa um retangulo
# Classe possui atributos: base e altura
# Classe possui métodos: calcular_area e calcular_perimetro ( funções dentro da classe )
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

# Instanciando um objeto do tipo Retangulo
# chamando o método construtor
retangulo1 = Retangulo(10.0, 5.0)
retangulo2 = Retangulo(10.0, 5.0)

print(type(retangulo1), retangulo1.base, retangulo2.altura, retangulo2.calcular_area())
print(type(retangulo2), retangulo1.base, retangulo2.altura, retangulo2.calcular_area())
