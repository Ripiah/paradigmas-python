codigo = int(input("Digite o código da categoria (1 à 5): "))

match codigo:
    case 1:
        categoria = "Ação"
    case 2:
        categoria = "Comédia"
    case 3:
        categoria = "Drama"
    case 4:
        categoria = "Ficção científica"
    case 5:
        categoria = "Animação"
    case _:
        categoria = "Categoria inválida"

print("\n=====CATEGORIA=====")
print(f"Código: {codigo}")
print(f"Categoria: {categoria}")
