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