from meu_pacote_pagamentos import valorPagamento

print("=== Sistema de Pagamento de Prestações ===")

total_prestacoes = 0
soma_total = 0.0

while True:
    entrada_valor = input("Informe o valor da prestação (0 para encerrar): ").strip()
    entrada_valor = entrada_valor.replace(",", ".")

    try:
        valor_prest = float(entrada_valor)
    except ValueError:
        print("Valor inválido. Tente novamente.")
        continue

    if valor_prest == 0:
        break

    entrada_dias = input("Informe o número de dias em atraso (0 se não houver): ").strip()
    try:
        dias_atraso = int(entrada_dias)
    except ValueError:
        print("Dias inválidos. Use um número inteiro. A entrada será reiniciada.")
        continue

    try:
        valor_a_pagar = valorPagamento(valor_prest, dias_atraso)
    except ValueError as e:
        print(f"Erro no cálculo: {e}")
        continue

    print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")
    total_prestacoes += 1
    soma_total += valor_a_pagar

print("\n=== Relatório do dia ===")
print(f"Quantidade de prestações pagas: {total_prestacoes}")
print(f"Valor total recebido: R$ {soma_total:.2f}")
print("Encerrando o programa. Obrigado.")
