""" exercício 03 """

def linha_para_dict(linha, chaves):
    valores = linha.strip().split(',')
    dicionario = {}
    for i in range(len(chaves)):
        dicionario[chaves[i]] = valores[i]

    return dicionario

def carregar_dados(nome_arquivo, chaves):
    dados = []
    
    arquivo = open('06-arquivos/exercícios/'+nome_arquivo, 'r')
    linhas = arquivo.readlines()

    for linha in linhas:
        dados.append(linha_para_dict(linha, chaves))
        
    arquivo.close()

    return tuple(dados)

dados_alunos = carregar_dados('dados_alunos.txt', ['prontuario', 'nome', 'email'])
dados_projetos = carregar_dados('dados_projetos.txt', ['codigo', 'titulo', 'responsavel'])

print('dados_alunos: ', dados_alunos)
print('dados_projetos: ', dados_projetos)



