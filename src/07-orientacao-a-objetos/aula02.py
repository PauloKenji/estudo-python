""" Aula 02 - Atributos de classe e instância """

#classe pessoa possui
#atributos de instancia: nome, email
#atributos de classe: especie
class Pessoa:

    especie = 'Humana'

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

pessoa1 = Pessoa('Maria da Silva', 'maria@email.com')
pessoa2 = Pessoa('João Santos', 'joao@email.com')
pessoa3 = Pessoa('Pedro Santos','Pedro@email.com')
#alterando o valor do atributo de classe na instancia
# altera somente na instancia
pessoa1.especie = 'Alienigena'

#alterando o valor do atributo de classe na classe
# altera em todas as instancias e na classe também
Pessoa.especie = 'Alienigenas do Passado'

print(pessoa1.nome, pessoa1.email, pessoa1.especie)
print(pessoa2.nome, pessoa2.email, pessoa2.especie)
print(pessoa3.nome, pessoa3.email, pessoa3.especie)

print(Pessoa.especie)