""" exercicio 05 - calculadora IMC """

individuo = {
    'altura': float(input('Digite a altura: ')),
    'peso': float(input('Digite o peso: '))
}

def calcular_imc(individuo):
    return individuo['peso'] / (individuo['altura'] ** 2)

def obter_classificacao(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc >= 18.5 and imc < 25:
        return 'Peso normal'
    elif imc >= 25 and imc < 30:
        return 'Excesso de peso'
    elif imc >= 30 and imc < 35:
        return 'Obesidade grau 1'
    elif imc >= 35 and imc < 40:
        return 'Obesidade grau 2'
    else:
        return 'Obesidade grau 3'

def situacao_individuo(imc):
    if imc < 18.5:
        return 'Ganhar peso'
    elif imc >= 25:
        return 'Perder peso'
    else:
        return 'Normal'    

print(f'IMC: {calcular_imc(individuo)}')
print(f'Classificação: {obter_classificacao(calcular_imc(individuo))}')
print(f'Situação: {situacao_individuo(calcular_imc(individuo))}')
