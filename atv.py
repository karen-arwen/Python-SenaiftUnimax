#O código abaixo realiza a soma de números dentro de um intervalo informado pelo usuário.
#Sua tarefa é apenas modificar o range do laço for, para que:


#- O número final (fim) também seja incluído na soma
#- Sem altera nenhuma outra parte do código


# Somando numeros do intervalo informado limitando o maior numero
inicio = int(input("Informe o primeiro número: "))
fim = int(input("Informe o número final: "))
salto = int(input("Informe o salto: "))

texto = "Cálculo: "
soma = 0

for numero in range(inicio, fim + 1, salto):
    soma = soma + numero
    texto = texto + str(numero)

    if numero > 50:
        texto = texto + "\nPassou de 50"
        break

    if numero != fim-1:
        texto = texto + " + "

print(f"{texto}")
print(f"Soma: {soma}")