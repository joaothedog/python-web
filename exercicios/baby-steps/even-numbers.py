limite = int(input("Digite um número limite: "))

# usando for exibe os pares ate o numero digitado
print("Numeros pares:")
for i in range(1, limite + 1):  # inclui o limite no intervalo "+1" do for
    if i % 2 == 0:  # verifica divisao por 2 resto 0, operador de modulo
        print(i) # resultado
