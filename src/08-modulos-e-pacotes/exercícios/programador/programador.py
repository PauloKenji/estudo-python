""" programador """

from funcionario.funcionario import Funcionario

class Programador(Funcionario):
    def __init__(self, nome, sobrenome, cpf, salario, bonus):
        super().__init__(nome, sobrenome, cpf, salario)
        self.bonus = bonus

    def calcular_pagamento(self):
        return super().calcular_pagamento() + self.bonus

    def __repr__(self):
        return f'Programador(nome={self.nome}, sobrenome={self.sobrenome}, cpf={self.cpf}, salario={self.salario}, bonus={self.bonus})'