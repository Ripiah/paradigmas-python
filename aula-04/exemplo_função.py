def preencher_lista(lista):
    print("\nPreenchimento da lista")
    for i in range(len(lista)):
        lista[i] = int (input(f"Digite o {1 + i}º numero: "))

def exibir_lista(lista):
    print(lista)

def ordenar_lista(lista):
    lista.sort()

def pesquisar_numero(lista, numero):
    return lista.count(numero)

quantidade = int(input("Informe a quantidade de elementos da lista: "))
numeros = [0] * quantidade
preencher_lista(numeros)

print("\n==== LISTA ORIGINAL ====")
exibir_lista(numeros)
ordenar_lista(numeros)

print("\n==== LISTA ORDENADA ====")
exibir_lista(numeros)
valor = int(input("\nDigite um número para pesquisar: "))
quantidade = pesquisar_numero(numeros, valor)

print(f"\nO número {valor} aparece {quantidade} vez(es) na lista.")
