""" funcionario """

from pessoa.pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, salario):
        super().__init__(nome, sobrenome, cpf)
        self.salario = salario

    def calcular_pagamento(self):
        return self.salario - ((10/100) * self.salario)

    def __repr__(self):
        return f'Funcionario(nome={self.nome}, sobrenome={self.sobrenome}, cpf={self.cpf}, salario={self.salario})'