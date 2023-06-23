""" exercício 02 """

from aluno.aluno import Aluno
from projeto.projeto import Projeto
from participacoes.participacoes import Participacoes
from retangulo.retangulo import Retangulo
from pessoa.pessoa import Pessoa

# ============= Retangulo =============

retangulo1 = Retangulo(10.0, 5.0)
retangulo2 = Retangulo(10.0, 5.0)

print(type(retangulo1), retangulo1.base, retangulo2.altura, retangulo2.calcular_area())
print(type(retangulo2), retangulo1.base, retangulo2.altura, retangulo2.calcular_area())

# ============= Pessoas =============



# ============= Alunos, Projetos e Participações =============	

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
