n = int(input("Quantos elementos a lista terá ? "))

lista = [0] * n

for i in range(n):
    lista[i] = int(input(f"Dgite o {1 + i} número: "))

pares = 0
impares = 0

for num in lista:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"\nLista digitada: {lista}")
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
