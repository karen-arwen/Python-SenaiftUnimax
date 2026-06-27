import operacoes

lista = []

while True:
    entrada = input("Informe um número inteiro ou 0 para sair: ")

    try:
        numero = int(entrada)
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        continue

    if numero == 0:
        break

    lista.append(numero)

soma = operacoes.soma(lista)
media = operacoes.media(lista)

print(f"Soma: {soma}")
print(f"Média: {media}")
