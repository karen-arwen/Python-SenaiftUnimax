def validar_faixa(numero, inicio, fim):
    return inicio <= numero <= fim

inicio = 1
fim = 10

while True:
    entrada = input(f"Informe um número inteiro entre {inicio} e {fim}: ")
    try:
        numero = int(entrada)
    except ValueError:
        print("Valor inválido. Informe um número inteiro.")
        continue

    if validar_faixa(numero, inicio, fim):
        print("Número válido!")
        break

    print("Número fora da faixa. Tente novamente.")
