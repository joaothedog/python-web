# write mode (w)
with open("./exercicios/baby-steps/numeros.txt", "w", encoding="utf-8") as arquivo:
    # for para escrever no arquivo uma contagem de um a cem
    for numero in range(1, 101):
        arquivo.write(f"{numero}\n")

print("'numeros.txt' criado com sucesso!")
