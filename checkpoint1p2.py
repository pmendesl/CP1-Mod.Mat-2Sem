# Erro 1: Divisão por zero
print("Erro 1: Divisão por zero (1/0)")
try:
    resultado = 1 / 0
    print(f"1 / 0 = {resultado}")
except ZeroDivisionError:
    print("Erro: Divisão por zero é indefinida!")
print("\n")

# Erro 2: -3^2 != 9
print("Erro 2: -3^2 != 9 (Watch parenthesis!)")
valor_errado = -3**2
valor_correto = (-3)**2
print(f"-3^2 = {valor_errado}")
print(f"(-3)^2 = {valor_correto}")
print(f"-3^2 é igual a 9? {valor_errado == 9}")
print("\n")

# Erro 3: (x + a)^2 != x^2 + a^2
print("Erro 3: (x + a)^2 != x^2 + a^2")
x = 2
a = 3

resultado_esquerda = (x + a)**2
resultado_direita = x**2 + a**2

print(f"Para x={x}, a={a}:")
print(f"Lado esquerdo ((x + a)^2): {resultado_esquerda}")
print(f"Lado direito (x^2 + a^2): {resultado_direita}")
print(f"Os resultados são iguais? {resultado_esquerda == resultado_direita}")
print("\n")
