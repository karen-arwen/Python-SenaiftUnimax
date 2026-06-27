def verifica_numero(valor):
    try:
        numero = float(valor)
    except ValueError:
        return "Erro: valor digitado não é numérico."

    if numero > 0:
        return 'P'
    else:
        return 'N'


entrada = input("Digite um número: ")
resultado = verifica_numero(entrada)
print(f"Resultado: {resultado}")
