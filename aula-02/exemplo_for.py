soma = 0

print("===== Soma de números =====\n")

for i in range(1, 11):
    numero = int(input(f"Digite o {i} número: "))
    soma += numero

print("\n================================")
print(f"A soma dos 10 números é: {soma}")
