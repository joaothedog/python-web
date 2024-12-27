# solicita no console uma lista de numeros
numeros = input("Digite uma lista de numeros separados por espaco: ")

# map converte o elemento p inteiro split divide a string nos espacos criando substrings
numeros = list(map(int, numeros.split()))

# calculo da soma com a funcao sum()
soma = sum(numeros)

# len(numeros) retorna qtd de numeros na lista (tamanho do vetor), e soma eh o total da soma dos numeros da lista.
media = soma / len(numeros)

# minimo e maximo com min e max dentro de um vetor
minimo = min(numeros)
maximo = max(numeros)

# resultados
print(f"Soma: {soma}")
print(f"Media: {media}")
print(f"Minimo: {minimo}")
print(f"Maximo: {maximo}")
