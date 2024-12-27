numero = int(input("Digite um numero para ver a tabuada do mesmo: "))

# usando for para gerar a tabuada do 1 ao 10
print(f"Tabuada do {numero}:")
for i in range(1, 11):  # gera numeros de 1 a 10
    resultado = numero * i  # multiplicacao do numero pelo indice atual do for
    print(f"{numero} x {i} = {resultado}") # resultado formatado
