print("===== CÁLCULO DE MÉDIA DA TURMA =====")

quantidade = int(input("Digite a quantidade de alunos: "))
soma_media = 0

for i in range(1, quantidade + 1):
    media = float(input(f"Digite a nota do {i} aluno: "))
    soma_media += media

media_turma = soma_media / quantidade

print("===== RESULTADO =====")
print(f"Quantidade de alunos: {quantidade}")
print(f"Média da turma: {media_turma:.1f}")
print("Cálculo concluído com sucesso !")
