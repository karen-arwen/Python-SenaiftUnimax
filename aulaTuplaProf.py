# Para verificar se um elemento específico está contido em uma tupla e gerar a variável venda
import time # Importa o módulo time para usar a função sleep
import sys # Importa o módulo sys para controle de saída

tupla_carros = ('Golf','Corolla','Civic','Opala','Fiat 147',\
                'Tempra','Tucson','Elantra','Chevette','Brasília',\
                'Kadett','Marea')

while True:
  # Solicita o carro que o usuário deseja vender
  carro_a_vender = input('Digite o carro que deseja vender (ou "Exit" para sair): ')
  carro_a_vender = carro_a_vender.strip().capitalize()

  if carro_a_vender == 'Exit':
    print('Saindo do programa.')
    # Simulação de barra de progresso
    bar_length = 30 # Define o tamanho da barra
    for i in range(bar_length + 1):
      progress = "." * i
      remaining = " " * (bar_length - i)
      # Usa \r para retornar o cursor ao início da linha e sobrescrever a saída anterior
      sys.stdout.write(f"\r[{progress}{remaining}] {i * 100 // bar_length}%")
      sys.stdout.flush() # Garante que a saída seja mostrada imediatamente
      time.sleep(0.1) # Pequeno atraso para simular o preenchimento
    sys.stdout.write("\n") # Adiciona uma nova linha após a barra de progresso terminar
    break

   # Verifica se o carro está na tupla e gera a variável 'venda'
  elif carro_a_vender in tupla_carros:
    venda = carro_a_vender
    print(f'Carro "{venda}" encontrado em estoque')
    print(f'Gerar Nota Fiscal {tupla_carros.index(venda)}: {venda}')
  else:
    print(f'Carro "{carro_a_vender}" não encontrado no estoque.')
    venda = None # A variável 'venda' será None se o carro não for encontrado
  print('-' * 30) # Separador para a próxima iteração

print("Fim do programa!")
time.sleep(2)