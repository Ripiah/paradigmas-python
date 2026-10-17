peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
elif imc < 35:
    classificacao = "Obesidade Grau I"
elif imc < 40:
    classificacao = "Obesidade Grau II"
else:
    classificacao = "Obesidade Grau III"

print("==== DADOS DO USUÁRIO ====")
print(f"Peso: {peso} kg")
print(f"Altura: {altura} m")
print("IMC = ", round(imc, 2))
print(f"Classificação: {classificacao}")
