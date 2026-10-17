print("===== SOMA DE NÚMEROS =====")

soma = 0
quantidade = 0

continuar = "S"

while continuar.upper() == "S":
    numero = int(input("Digite o número: "))

    soma += numero
    quantidade += 1

    continuar = input("Deseja informar outro número ? {S/N}: ")

print("\n===== RESULTADO =====")
print(f"Quantidade de números digitados: {quantidade}")
print(f"Soma de números: {soma}")
