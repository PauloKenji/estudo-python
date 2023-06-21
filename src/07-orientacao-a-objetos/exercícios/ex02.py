""" exercício 02 """

class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, value):
        if type(value) != int or value == None:
            raise ValueError('Código deve ser um inteiro')
        if value <= 0:
            raise ValueError('Código deve ser maior que zero')
        self.__codigo = value
    
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, value):
        if value == '' or value == None:
            raise ValueError('Título não pode ser vazio')
        self.__titulo = value

    @property
    def responsavel(self):
        return self.__responsavel
    
    @responsavel.setter
    def responsavel(self, value):
        if value == '' or value == None:
            raise ValueError('Responsável não pode ser vazio')
        self.__responsavel = value
    
    @classmethod
    def from_string(cls, rep_projeto):
        codigo, titulo, responsavel = rep_projeto.split(',')
        return cls(int(codigo), titulo, responsavel)

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.codigo == value.codigo
        return False
    
    def __str__(self):
        return f'Projeto[codigo={self.codigo}, titulo={self.titulo}, responsavel={self.responsavel}]'

projeto1 = Projeto(1, "Projeto A", "João")
projeto2 = Projeto(2, "Projeto B", "Maria")
projeto3 = Projeto(3, "Projeto C", "Pedro")

print(projeto1 == projeto2)
print(projeto1 == projeto3)

print(projeto1)
print(projeto2)
print(projeto3)

rep_projeto = "4,Projeto D,Ana"
projeto4 = Projeto.from_string(rep_projeto)

print(projeto4 == projeto1)
print(projeto4)

projeto5 = Projeto(projeto1.codigo, "Projeto E", "Samuel")

print(projeto5 == projeto1)
print(projeto5)