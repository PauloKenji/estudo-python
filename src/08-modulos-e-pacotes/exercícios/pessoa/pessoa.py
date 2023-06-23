""" Pessoa """

class Pessoa:
    def __init__(self, nome, sobrenome, cpf, telefone=None, enderecos=None):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.telefone = telefone
        self.enderecos = enderecos if enderecos is not None else []

    def add_endereco(self, endereco):
        self.enderecos.append(endereco)

    def print_enderecos(self):
        for endereco in self.enderecos:
            print(endereco)

    def __str__(self):
        return f'Pessoa[cpf={self.cpf},nome={self.nome},sobrenome={self.sobrenome}, telefone={self.telefone},enderecos={self.enderecos}]'