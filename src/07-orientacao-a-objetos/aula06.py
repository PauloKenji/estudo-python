""" Aula 06 - equal e hash code """

#sempre que for usar classes em coleções é importante sobrescrever os métodos equal e hash code
9

nome1 = 'joão'
nome2 = 'joão'

print(nome1 == nome2)

class Pessoa:
    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.cpf == value.cpf
        return False
    
    def __hash__(self):
        return hash(self.cpf)
    
    def __repr__(self):
        return f'Pessoa({self.cpf}, {self.nome})'
pessoa1 = Pessoa('111', 'joão')
pessoa2 = Pessoa('111', 'joão')
pessoa3 = Pessoa('222', 'maria')

pessoas = {pessoa1, pessoa2, pessoa3}
print(pessoas)
print(pessoa1 == pessoa2)

pessoas_lista = [pessoa1, pessoa2, pessoa3]
print(pessoas_lista)

print(pessoas_lista.count(pessoa1))