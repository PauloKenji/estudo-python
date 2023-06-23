""" exercício 02 """

from aluno.aluno import Aluno
from projeto.projeto import Projeto
from participacoes.participacoes import Participacoes
from retangulo.retangulo import Retangulo
from pessoa.pessoa import Pessoa
from endereco.endereco import Endereco
from telefone.telefone import Telefone

# ============= Retangulo =============

retangulo1 = Retangulo(10.0, 5.0)
retangulo1.base = 20.0
retangulo1.altura = 10.0

retangulo1 = Retangulo(10.0, 5.0)
retangulo2 = Retangulo(6.0, 3.0)
retangulo3 = Retangulo.from_list([10.0, 5.0])
print(type(retangulo3), retangulo3.base, retangulo3.altura, retangulo3.calcular_area())

print(type(retangulo1), retangulo1.base, retangulo2.altura, retangulo2.calcular_area())
print(type(retangulo2), retangulo1.base, retangulo2.altura, retangulo2.calcular_area())

retangulo1 = Retangulo(10.0, 5.0)
retangulo2 = Retangulo(6.0, 3.0)

retangulo3 = eval('Retangulo(7.5,12.3)')
retangulo4 = eval(repr(retangulo3))

print(retangulo1.__repr__())
print(retangulo2)
print(retangulo3)
print(retangulo4)

# ============= Pessoas =============
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
