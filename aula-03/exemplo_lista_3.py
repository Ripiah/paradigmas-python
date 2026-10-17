idade = []

while True:
    id = int(input("Digite a idade do aluno: "))
    idade.append(id)

    while True:
        continua = input("Deseja continuar cadastrando ? (S/N): ").strip().lower()

        if continua in ["s", "n"]:
            break
        print("Opção inválida! Digite apenas 'S' para sim e 'N' para não.\n")

    if continua == "n":
        break

if idade:
    soma_idade = sum(idade)
    n = len(idade)
    media_idade = soma_idade / n
    
    print(f"Esta turma possui {n} alunos e a média de idade é: {media_idade:.2f}")
else:
    print("\nNenhuma idade foi cadastrada.")
