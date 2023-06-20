""" Aula 03 - Métodos de class """

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    @classmethod
    def from_string(cls, rep_retangulo):
        base, altura = rep_retangulo.split(',')
        return cls(float(base), float(altura))    

    @classmethod
    def from_list(cls, lista):
        return cls(lista[0], lista[1])

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

retangulo1 = Retangulo(10.0, 5.0)
retangulo2 = Retangulo(6.0, 3.0)
retangulo3 = Retangulo.from_list([10.0, 5.0])
print(type(retangulo3), retangulo3.base, retangulo3.altura, retangulo3.calcular_area())

retangulo3 = Retangulo.from_string("10.0,5.0")
print(type(retangulo3), retangulo3.base, retangulo3.altura, retangulo3.calcular_area())

# print(Retangulo.calcular_area()) # TypeError: calcular_area() missing 1 required positional argument: 'self'
# print(retangulo1.calcular_area())
# print(retangulo2.calcular_area())