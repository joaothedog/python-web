frase = input("Digite uma frase: ")

# split() para dividir a frase em palavras
palavras = frase.split()

# len(palavras) ira retornar o numero de elementos que possuem no vetor, separadas por split() sera equivalente ao numero de palavras
total_palavras = len(palavras)

print(f"A frase possui {total_palavras} palavras.")
