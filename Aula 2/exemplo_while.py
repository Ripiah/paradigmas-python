print("===== REGISTRO DE VENDAS =====")
print("Digite o valor de cada venda.")
print("Para encerrar o processo, digite 'fim'.\n")

total_vendas = 0
quantidade_vendas = 0

entrada = input("Digite o valor da venda: R$")

while entrada.lower() != 'fim':
    valor = float(entrada)

    if valor > 0:
        total_vendas += valor
        quantidade_vendas += 1

        print("Venda registrada com sucesso.\n")
    else:
        print("O valor da venda deve ser maior que 0.\n")

    entrada = input("Digite o valor da venda ou 'fim' para encerrar o processo: R$")

print("===== RESULTADO =====")
print(f"Quantidade de vendas: {quantidade_vendas}")
print(f"Valor total arrecadado: R${total_vendas:.2f}")

if quantidade_vendas > 0:
    media = total_vendas / quantidade_vendas
    print(f"Valor médio das vendas: R${media:.2f}")
else:
    print("Nenhuma venda válida foi registrada.")
print("\nRegistro encerrado. Obrigado por utilizar o sistema.")
