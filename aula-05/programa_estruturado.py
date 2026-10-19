produtos = {}
while True:
    print("\n====== CADASTRO DE PRODUTOS ======")
    codigo = input("Digite o código do produto: ").strip()
    if codigo == "":
        print("Erro: o código não pode ficar vazio.")
        continue
    if codigo in produtos:
        print("Erro: o produto já foi cadastrado.")
        continue
    nome = input("Digite o nome do produto: ").strip()
    if nome == "":
        print("Erro: o nome não pode ficar vazio.")
        continue
    try:
        preco = float(input("Digite o preço: R$").replace(",", "."))
        if preco <= 0:
            print("Erro: o preço deve ser maior que zero.")
            continue
    except ValueError:
        print("Erro: digite um valor válido.")
        continue
    try:
        quantidade = int(input("Digite a quantidade: "))
        if quantidade < 0:
            print("Erro: a quantidade não pode ser negativa.")
            continue
    except ValueError:
        print("Erro: digite um número inteiro.")
        continue
    total = preco * quantidade
    produtos[codigo] = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade,
        "total": total
    }
    print("Produto cadastrado com sucesso!")
    continuar = input("Cadastrar outro produto ? (S/N): ").upper()
    if continuar != "S":
        break

print("\n===== RELATÓRIO DE ESTOQUE =====")
valor_geral = 0
for codigo, produto in produtos.items():
    print("\nCódigo:", codigo)
    print("Nome:", produto["nome"])
    print("Preço: R$", f'{produto["preco"]:.2f}')
    valor_geral += produto["total"]
print("\nValor geral do estoque: R$", "f{valor_geral:.2f}")
