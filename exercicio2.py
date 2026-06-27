from meu_pacote import somaImposto


taxa = float(input("Informe a taxa de imposto (%): "))
Custo = float(input("Informe o custo do item: "))
resultado = somaImposto(taxa, Custo)
print(f"Valor final com imposto: {resultado:.2f}")
