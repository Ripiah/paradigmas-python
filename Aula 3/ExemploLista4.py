n = int(input("Quantos elementos terá a lista ? "))
lista = []
lista2 = []

for i in range(n):
    num = int(input(f"Digite o {i + 1} numero: "))
    lista.append(num)

lista2 = sorted(lista)

print(f"\nLista ordenada: {lista2}")

busca = int(input("\nDigite o número que deseja buscar: "))
posicoes = []

for i in range(len(lista)):
    if lista[i] == busca:
        posicoes.append(i)
        
if len(posicoes) > 0:
    print(f"\nO número {busca} foi encontrado nas posições: {posicoes}")
    print(f"Quantidade de vezes que aparece: {len(posicoes)}")
else:
    print(f"\nO número {busca} não foi encontrado na lista.")

print("\nFim do programa!")
