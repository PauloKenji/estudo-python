from pessoa.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf):
        super().__init__(nome, sobrenome, cpf)
        self.compras = []

    def salvar_compras(self, *values):
        self.compras.extend(values)

    def __repr__(self):
        return f'Cliente(nome={self.nome}, sobrenome={self.sobrenome}, cpf={self.cpf}, compras={self.compras})'