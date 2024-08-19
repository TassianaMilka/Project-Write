# Solicita ao usuário que insira o valor do produto e o percentual de desconto

valor_produto = float(input())

percentual_desconto = float(input())

 

# Verifica se o percentual de desconto está dentro dos limites aceitáveis (0-100%)

if percentual_desconto < 0 or percentual_desconto > 100:

    print("Erro de percentual")

else:

    # Calcula o valor do desconto

    desconto = valor_produto * (percentual_desconto / 100)

 

    # Calcula o valor final da compra

    valor_final = valor_produto - desconto

 

    # Exibe o valor final da compra

    print(f{valor_final:.2f})