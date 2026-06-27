def valorPagamento(prestacao, dias_atraso):
    try:
        valor = float(prestacao)
    except (TypeError, ValueError):
        raise ValueError("Prestação deve ser um número válido.")

    try:
        dias = int(dias_atraso)
    except (TypeError, ValueError):
        raise ValueError("Dias de atraso deve ser um inteiro válido.")

    if dias <= 0:
        return round(valor, 2)

    multa = 0.03 * valor
    juros = 0.001 * valor * dias
    total = valor + multa + juros
    return round(total, 2)
