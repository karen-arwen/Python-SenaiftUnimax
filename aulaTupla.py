import time
import sys
tupla_carros = 'gol', 'Celta', 'Corolla', 'Civic',  'palio', 'Opala', \
              'Tucson', 'Elantra'

while True:
    #solicita o caro q o usuario deseja vender
    carro_a_vender = input("Informe o nome do carro que deseja vender (ou 'Exit' para sair): ")
    carro_a_vender = carro_a_vender.strip().capitalize()

    if carro_a_vender == 'Exit':
        print("Saindo do programa...")
        bar_lenth = 30
        for i in range(bar_lenth +1):
            progress = "#" * i
            remaining = " " * (bar_lenth - i)

            #usa \r p retornar o cursor ao inicio da linha e sobrescrever
            sys.stdout.write(f"\r [{progress} {remaining}] {i * 100 // bar_lenth} % ")
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write("\n")
        break
    elif carro_a_vender in tupla_carros:
        venda = carro_a_vender
        print(f"Carro vendido: {venda}. Encontrado no estoque")
        print(f"Gerar Nota fiscal {tupla_carros.index(venda)} : {venda}")
    else:
        print(f"Carro '{carro_a_vender}' não encontrado")
