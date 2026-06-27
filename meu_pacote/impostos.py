def somaImposto(taxaImposto, custo):
    """Retorna o custo final incluindo a taxa de imposto em porcentagem."""
    return custo * (1 + taxaImposto / 100)
