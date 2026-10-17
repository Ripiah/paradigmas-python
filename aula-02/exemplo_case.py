numero = int(input("Digite um númerode 1 à 7: "))

match numero:
    case 1:
        dia = "Domingo"
    case 2:
        dia = "Segunda-feira"
    case 3:
        dia = "Terça-feira"
    case 4:
        dia = "Quarta-feira"
    case 5:
        dia = "Quinta-feira"
    case 6:
        dia = "Sexta-feira"
    case 7:
        dia = "Sábado"
    case _:
        dia = "Dia inválido"

print(f"Dia da semana: {dia}")
