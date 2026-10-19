class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2
    def verificar_situacao(self):
        media = self.calcular_media()
        if media >= 7:
            return "Aprovado"
        elif media >= 4:
            return "Prova final"
        else:
            return "Reprovado"
    def exibir_resultado(self):
        print("\n--------------------------")
        print(f"Aluno: {self.nome}")
        print(f"Média: {self.calcular_media():.1f}")
        print(f"Situação: {self.verificar_situacao()}")

if __name__ == "__main__":
    quantidade = int(input("Quantos alunos deseja cadastrar ? "))
    for i in range(quantidade):
        print(f"\nAluno {i + 1}")
        nome = input("Nome: ")
        nota1 = float(input("Primeira nota: "))
        nota2 = float(input("Segunda nota: "))
        aluno = Aluno(nome, nota1, nota2)
        aluno.exibir_resultado()
