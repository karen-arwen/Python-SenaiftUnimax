def media(lista_numeros):
    if not lista_numeros:
        return 0

    total = 0
    for numero in lista_numeros:
        total += numero

    return total / len(lista_numeros)


def soma(lista_numeros):
    total = 0
    for numero in lista_numeros:
        total += numero

    return total
