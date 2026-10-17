quantidade = int(input("Quantos números desejas inserir na lista ? "))
numeros = []

for i in range(quantidade):
    numero = int(input(f"Digite o {i + 1} número: "))
    numeros.append(numero)

print("\nLISTA ORIGINAL")
print(numeros)

print("\nOPERAÇÕES COM LISTA")
print(f"Quantidade de elementos: {len(numeros)}")
print(f"Maior valor: {max(numeros)}")
print(f"Menor valor: {min(numeros)}")
print(f"Soma dos elementos: {sum(numeros)}")
print(f"Média dos elementos: {sum(numeros) / len(numeros):.2f}")

numeros.sort()

print("\nLista em ordem crescente:")
print(numeros)

numeros.reverse()

print("\nLista em ordem decrescente")
print(numeros)
