import sqlite3
banco15 = sqlite3.connect("escola_curso.db")
cursor = banco15.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS alunos(nome TEXT, idade INTEGER)''')

while True:
    nome = input("\nNome: ").strip()

    try:
        idade = int(input("Idade: "))
    except ValueError:
        print("Erro: digite apenas números para a idade.")
        continue

    cursor.execute(
        "INSERT INTO alunos(nome, idade) VALUES (?, ?)",
        (nome, idade)
    )

    banco15.commit()

    resposta = input("Deseja cadastrar outra pessoa ? (S/N): ").strip().upper()

    if resposta == "N":
        break

print("\n===ALUNOS CADASTRADOS ===")
cursor.execute("SELECT nome, idade FROM alunos")

for nome, idade in cursor.fetchall():
    print(f"Nome: {nome} | Idade: {idade}")

banco15.close()
