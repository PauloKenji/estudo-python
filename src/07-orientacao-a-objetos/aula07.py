""" aula 07 - Relacionamentos entre classes """

class Endereco:
    def __init__(self, cep, numero):
        self.cep = cep
        self.numero = numero

    def __str__(self):
        return f'Endereco[cep={self.cep},numero={self.numero}]'
class Telefone:
    def __init__(self, ddd, numero):
        self.ddd = ddd
        self.numero = numero
    
    def __str__(self):
        return f'Telefone[ddd={self.ddd},numero={self.numero}]'

class Pessoa:
    def __init__(self, cpf, nome, telefone, endereco):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.enderecos = [endereco]

    def add_endereco(self, endereco):
        self.enderecos.append(endereco)

    def print_enderecos(self):
        for endereco in self.enderecos:
            print(endereco)

    def __str__(self):
        return f'Pessoa[cpf={self.cpf},nome={self.nome},telefone={self.telefone},enderecos={self.enderecos}]'

telefone = Telefone('11', '1111-1111')
pessoa1 = Pessoa('4132', 'joão', telefone, Endereco('02156185', 123))

pessoa1.add_endereco(Endereco('02123125', 456))

pessoa2 = Pessoa('4512', 'Pedro', telefone, Endereco('02123663', 426))

pessoa3 = Pessoa('4112', 'Maria', telefone, Endereco('11123663', 526))

print(pessoa1)
print(pessoa1.nome)
print(pessoa1.cpf)
print(pessoa1.telefone.ddd, pessoa1.telefone.numero)

pessoa1.print_enderecos()
pessoa2.print_enderecos()
pessoa3.print_enderecos()
