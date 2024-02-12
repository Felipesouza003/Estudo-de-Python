def remove_repetidos(lista):
    novaLista = []
    for x in lista:
        if x not in novaLista:
            novaLista.append(x)
    return sorted(novaLista)


