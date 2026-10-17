nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print("==== RESULTADO ====")
print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Média: {media:.1f}")

if media >= 6:
    print("Aprovado")
elif media >= 4:
    print("Exame final")
else:
    print("Reprovado")
