endereco = input("Digite o endereço do terreno: ")
comprimento = float(input("Digite o comprimento do terreno (m): "))
largura = float(input("Digite a largura do terreno (m): "))
area = comprimento * largura

print("\n==== DADOS DO TERRENO ====")
print(f"Endereço: {endereco}")
print(f"Comprimento: {comprimento:.1f} m")
print(f"Largura: {largura:.1f} m")
print(f"\nÁrea do terreno: {area:.1f} m²")
