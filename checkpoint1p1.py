# Verificação da Propriedade de Operações Aritméticas: ab + ac = a(b + c)
a = 2
b = 3
c = 4

resultado_esquerda = a * b + a * c
resultado_direita = a * (b + c)

print(f"Para a={a}, b={b}, c={c}:")
print(f"Lado esquerdo (ab + ac): {resultado_esquerda}")
print(f"Lado direito (a(b + c)): {resultado_direita}")
print(f"Os resultados são iguais? {resultado_esquerda == resultado_direita}")
print("\n")

# Verificação da Propriedade de Expoentes: (a^n)^m = a^(nm)
a = 2
n = 3
m = 2

resultado_esquerda = (a**n)**m
resultado_direita = a**(n*m)

print(f"Para a={a}, n={n}, m={m}:")
print(f"Lado esquerdo ((a^n)^m): {resultado_esquerda}")
print(f"Lado direito (a^(nm)): {resultado_direita}")
print(f"Os resultados são iguais? {resultado_esquerda == resultado_direita}")
print("\n")

# Verificação da Propriedade de Radicais: sqrt(ab) = sqrt(a) * sqrt(b)
import math

a = 4
b = 9

resultado_esquerda = math.sqrt(a * b)
resultado_direita = math.sqrt(a) * math.sqrt(b)

print(f"Para a={a}, b={b}:")
print(f"Lado esquerdo (sqrt(ab)): {resultado_esquerda}")
print(f"Lado direito (sqrt(a) * sqrt(b)): {resultado_direita}")
print(f"Os resultados são iguais? {resultado_esquerda == resultado_direita}")
print("\n")

# Verificação da Propriedade de Desigualdades: Se a < b então a + c < b + c
a = 5
b = 10
c = 3

condicao_inicial = a < b
resultado_esquerda = a + c
resultado_direita = b + c

print(f"Para a={a}, b={b}, c={c}:")
print(f"Condição inicial (a < b): {condicao_inicial}")
print(f"Lado esquerdo (a + c): {resultado_esquerda}")
print(f"Lado direito (b + c): {resultado_direita}")
print(f"Os resultados são iguais? {resultado_esquerda < resultado_direita}")
print("\n")

# Verificação da Propriedade de Logaritmos: log_b(x^r) = r * log_b(x)
import math

b = 10
x = 100
r = 2

resultado_esquerda = math.log(x**r, b)
resultado_direita = r * math.log(x, b)

print(f"Para b={b}, x={x}, r={r}:")
print(f"Lado esquerdo (log_b(x^r)): {resultado_esquerda}")
print(f"Lado direito (r * log_b(x)): {resultado_direita}")
print(f"Os resultados são iguais? {resultado_esquerda == resultado_direita}")
print("\n")
