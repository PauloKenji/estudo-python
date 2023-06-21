""" exercício 01 """

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
        if value == '' or value == None:
            raise ValueError('Prontuário não pode ser vazio')
        self.__prontuario = value

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, value):
        if value == '' or value == None:
            raise ValueError('Nome não pode ser vazio')
        self.__nome = value
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        if value == '' or value == None:
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
    
aluno1 = Aluno("SP0101", "João", "joao@example.com")
aluno2 = Aluno("SP1111", "Pedro", "Pedro1@example.com")
aluno3 = Aluno("SP2222", "Pedro", "pedro@example.com")
aluno4 = Aluno.from_string("SP0101,João da Silva,joao@email.com")

print(aluno1 == aluno2)
print(aluno1 == aluno3)
print(aluno1 == aluno4)

print(aluno1)
print(aluno2)
print(aluno3)
print(aluno4)

