""" Projeto """

class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel
        self.participacoes = []

    def add_participacao(self, participacao):
        self.participacoes.append(participacao)

    def show_all_participacao(self):
        for participacao in self.participacoes:
            print(participacao)

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, value):
        if not isinstance(value, int) or value is None:
            raise ValueError('Código deve ser um inteiro')
        if value <= 0:
            raise ValueError('Código deve ser maior que zero')
        self.__codigo = value

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, value):
        if value == '' or value is None:
            raise ValueError('Título não pode ser vazio')
        self.__titulo = value

    @property
    def responsavel(self):
        return self.__responsavel

    @responsavel.setter
    def responsavel(self, value):
        if value == '' or value is None:
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
        return f'Projeto[codigo={self.codigo}, titulo={self.titulo}, responsavel={self.responsavel}, participacoes={self.participacoes}]'