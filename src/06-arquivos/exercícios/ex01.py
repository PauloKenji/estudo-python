""" exercício 01 """

def carregar_dados_alunos(nome_arquivo):
    alunos = []
    
    arquivo = open('06-arquivos/exercícios/'+nome_arquivo, 'r')
    linhas = arquivo.readlines()

    for linha in linhas:
        prontuario,nome,email = linha.strip().split(',')
        aluno = {
            'prontuario': prontuario,
            'nome': nome,
            'email': email
        }
        alunos.append(aluno)

    arquivo.close()

    return tuple(alunos)

alunos = carregar_dados_alunos('dados_alunos.txt')

print(alunos)
print(type(alunos))

