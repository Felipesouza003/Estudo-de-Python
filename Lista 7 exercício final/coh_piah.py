import re
import string
def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    i = 0
    soma = 0
    while i != len(as_a):
        soma += abs(as_a[i] - as_b[i])
        i += 1
    Sa_b = soma / 6
    return Sa_b

def soma_char_alfa_sentenca(sentencas):
    soma = 0

    for sentenca in sentencas:
        sentenca_sem_separadores = re.sub(r'[.]+', '', sentenca)
        for caractere in sentenca_sem_separadores:
            soma += 1

    return soma

def soma_char_alfa_frase(frases):
    soma = 0

    for frase in frases:
        frase_sem_separadores = re.sub(r'[,:;]+', '', frase)
        for caractere in frase_sem_separadores:
            soma += 1

    return soma
def calcula_assinatura(texto):
    sentencas = separa_sentencas(texto)
    frases = []
    for sentenca in sentencas:
        for frase in separa_frases(sentenca):
            frases.append(frase) 
    palavras = []
    for frase in frases:
        for palavra in separa_palavras(frase):
            palavras.append(palavra)


    wal = sum(len(palavra) for palavra in palavras)/ len(palavras)
    ttr = n_palavras_diferentes(palavras) / len(palavras)
    hlr = n_palavras_unicas(palavras) / len(palavras)
    sal = soma_char_alfa_sentenca(sentencas) / len(sentencas)
    sac = len(frases) / len(sentencas)
    pal = soma_char_alfa_frase(frases) / len(frases)
    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    if len(textos) == 0:
        print("A lista de textos está vazia. Não é possível avaliar.")
        return -1
    GrauMin = float('inf')
    infectado = -1
    for i, texto in enumerate(textos):
        as_texto = calcula_assinatura(texto)
        grauSimilaridade = compara_assinatura(ass_cp, as_texto)
        if grauSimilaridade < GrauMin:
            GrauMin = grauSimilaridade
            infectado = i + 1
    return infectado

as_cp = le_assinatura()
textos = le_textos()
print("O autor do texto", avalia_textos(textos, as_cp), "está infectado com COH-PIAH")
