# abrir o text modo read
with open("archive.txt", "r", encoding="utf-8") as arquivo:
    # le o conteudo
    conteudo = arquivo.read()

# split para dividir o conteudo do archive.txt em palavras
palavras = conteudo.split()

# armazena as palavras dentro de um dicionario chave/valor chave = palavra valor = numero de vezes que a palavra aparece
contagem = {}

for palavra in palavras:
    # converte todas as palavras p minusculas, sem distincao e a funcao strip remove os simbolos
    palavra = palavra.lower().strip(",.!?;:\"()[]")
    # adiciona as palavras no dicionario
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

# contagem de palavras
for palavra, quantidade in contagem.items():
    print(f"'{palavra}': {quantidade} vezes")
