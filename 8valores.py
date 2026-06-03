def potencia(x, y):
    resultado = 1

    # Regra: qualquer número elevado a 0 é 1
    if y == 0:
        return 1

    if y < 0:
        x = 1 / x
        y = -y

    # Multiplicações     for i in range(y):
        resultado *= x

    return resultado


# Programa principal
x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

print("Resultado de x^y =", potencia(x, y))