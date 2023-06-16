""" exercício 02 """

def carregar_dados_projetos(nome_arquivo):

    projetos = []

    arquivo = open('06-arquivos/exercícios/'+nome_arquivo, 'r')
    linhas = arquivo.readlines()

    for linha in linhas:
        dados_projeto = linha.strip().split(',')
        projeto = {
            'codigo': int(dados_projeto[0]),
            'titulo': dados_projeto[1],
            'responsavel': dados_projeto[2],
        }
        projetos.append(projeto)
    
    arquivo.close()

    return tuple(projetos)

projetos = carregar_dados_projetos('dados_projetos.txt')

print(projetos)
print(type(projetos))
