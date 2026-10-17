nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / (altura ** 2)

print("==== DADOS DO USUÁRIO ====")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Peso: {peso} kg")
print(f"Altura: {altura} m")

print("\n==== RESULTADO ====")
print(f"IMC = {round(imc, 2)}")
