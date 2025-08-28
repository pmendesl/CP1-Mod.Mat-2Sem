import numpy as np

# Propriedade 1: Fechamento sob adição (u + v está em V)
print("Propriedade 1: Fechamento sob adição (u + v)")
u = np.array([1, 2, 3])
v = np.array([4, 5, 6])
w = u + v
print(f"u = {u}, v = {v}, u + v = {w}")
print("\n")

# Propriedade 2: Comutatividade da adição (u + v = v + u)
print("Propriedade 2: Comutatividade da adição (u + v = v + u)")
u = np.array([1, 2, 3])
v = np.array([4, 5, 6])
print(f"u + v = {u + v}")
print(f"v + u = {v + u}")
print(f"São iguais? {np.array_equal(u + v, v + u)}")
print("\n")

# Propriedade 3: Associatividade da adição (u + (v + w) = (u + v) + w)
print("Propriedade 3: Associatividade da adição (u + (v + w) = (u + v) + w)")
u = np.array([1, 2, 3])
v = np.array([4, 5, 6])
w = np.array([7, 8, 9])
print(f"u + (v + w) = {u + (v + w)}")
print(f"(u + v) + w = {(u + v) + w}")
print(f"São iguais? {np.array_equal(u + (v + w), (u + v) + w)}")
print("\n")

# Propriedade 4: Existência do vetor zero (u + 0 = u)
print("Propriedade 4: Existência do vetor zero (u + 0 = u)")
u = np.array([1, 2, 3])
zero_vector = np.array([0, 0, 0])
print(f"u + 0 = {u + zero_vector}")
print(f"São iguais? {np.array_equal(u + zero_vector, u)}")
print("\n")

# Propriedade 5: Existência do inverso aditivo (u + (-u) = 0)
print("Propriedade 5: Existência do inverso aditivo (u + (-u) = 0)")
u = np.array([1, 2, 3])
print(f"u + (-u) = {u + (-u)}")
print(f"São iguais? {np.array_equal(u + (-u), zero_vector)}")
print("\n")

# Propriedade 6: Fechamento sob multiplicação por escalar (c * u)
print("Propriedade 6: Fechamento sob multiplicação por escalar (c * u)")
c = 5
u = np.array([1, 2, 3])
result = c * u
print(f"c = {c}, u = {u}, c * u = {result}")
print("\n")

# Propriedade 7: Distributividade da multiplicação por escalar em relação à adição de vetores (c * (u + v) = c * u + c * v)
print("Propriedade 7: Distributividade da multiplicação por escalar em relação à adição de vetores (c * (u + v) = c * u + c * v)")
c = 2
u = np.array([1, 2, 3])
v = np.array([4, 5, 6])
print(f"c * (u + v) = {c * (u + v)}")
print(f"c * u + c * v = {c * u + c * v}")
print(f"São iguais? {np.array_equal(c * (u + v), c * u + c * v)}")
print("\n")

# Propriedade 8: Distributividade da multiplicação por escalar em relação à adição de escalares ((c + d) * u = c * u + d * u)
print("Propriedade 8: Distributividade da multiplicação por escalar em relação à adição de escalares ((c + d) * u = c * u + d * u)")
c = 2
d = 3
u = np.array([1, 2, 3])
print(f"(c + d) * u = {(c + d) * u}")
print(f"c * u + d * u = {c * u + d * u}")
print(f"São iguais? {np.array_equal((c + d) * u, c * u + d * u)}")
print("\n")

# Propriedade 9: Associatividade da multiplicação por escalar (c * (d * u) = (c * d) * u)
print("Propriedade 9: Associatividade da multiplicação por escalar (c * (d * u) = (c * d) * u)")
c = 2
d = 3
u = np.array([1, 2, 3])
print(f"c * (d * u) = {c * (d * u)}")
print(f"(c * d) * u = {(c * d) * u}")
print(f"São iguais? {np.array_equal(c * (d * u), (c * d) * u)}")
print("\n")

# Propriedade 10: Existência do elemento neutro da multiplicação por escalar (1 * u = u)
print("Propriedade 10: Existência do elemento neutro da multiplicação por escalar (1 * u = u)")
u = np.array([1, 2, 3])
print(f"1 * u = {1 * u}")
print(f"São iguais? {np.array_equal(1 * u, u)}")
print("\n")
