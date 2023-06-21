""" exercicio 04 """


class Aluno:
    def __init__(self, prontuario, nome, email):
        self.prontuario = prontuario
        self.nome = nome
        self.email = email

    @property
    def prontuario(self):
        return self.__prontuario

    @prontuario.setter
    def prontuario(self, value):
        if value == '' or value is None:
            raise ValueError('Prontuário não pode ser vazio')
        self.__prontuario = value

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        if value == '' or value is None:
            raise ValueError('Nome não pode ser vazio')
        self.__nome = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if value == '' or value is None:
            raise ValueError('Email não pode ser vazio')
        self.__email = value

    @classmethod
    def from_string(cls, rep_aluno):
        prontuario, nome, email = rep_aluno.split(',')
        return cls(prontuario, nome, email)

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.prontuario == value.prontuario
        return False

    def __str__(self):
        return f'Aluno[prontuario={self.prontuario}, nome={self.nome}, email={self.email}]'


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


class Participacoes:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = projeto

    def __str__(self):
        return f'Participacoes[codigo={self.codigo}, data_inicio={self.data_inicio}, data_fim={self.data_fim}, aluno={self.aluno}, projeto={self.projeto}]'

    def __repr__(self):
        return f'Participacoes({self.codigo}, {self.data_inicio}, {self.data_fim}, {self.aluno}, {self.projeto}))'


aluno1 = Aluno("12345", "João", "joao@example.com")
aluno2 = Aluno("67890", "Maria", "maria@example.com")
projeto1 = Projeto(1, "Projeto A", "João")
projeto2 = Projeto(2, "Projeto B", "Maria")

participacao1 = Participacoes(1, "2023-01-01", "2023-06-30", aluno1, projeto1)
participacao2 = Participacoes(2, "2023-02-01", "2023-07-31", aluno2, projeto2)

print(participacao1.codigo)
print(participacao1.data_inicio)
print(participacao1.data_fim)
print(participacao1.aluno)
print(participacao1.projeto)

print(participacao2.codigo)
print(participacao2.data_inicio)
print(participacao2.data_fim)
print(participacao2.aluno)
print(participacao2.projeto)

projeto1.add_participacao(participacao1)
projeto2.add_participacao(participacao2)

print(projeto1)
