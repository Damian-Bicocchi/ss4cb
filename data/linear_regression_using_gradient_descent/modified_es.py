# Regresión Lineal usando Descenso del Gradiente (y = w * x)

# Datos de ejemplo: y = 2x
X = [1, 2, 3, 4, 5]
Y = [2, 4, 6, 8, 10]

w = 0.0           # peso inicial
lr = 0.01         # ritmo de aprendizaje
epocas = 100      # iteraciones de entrenamiento
n = len(X)


def predecir(x, w):
    return w * x


def costo(X, Y, w):
    """Error Cuadrático Medio"""
    return sum((predecir(x, w) - y) ** 2 for x, y in zip(X, Y)) / n


def gradiente(X, Y, w):
    """Derivada del ECM con respecto a w"""
    return sum(2 * (predecir(x, w) - y) * x for x, y in zip(X, Y)) / n


# Bucle de entrenamiento
for epoca in range(epocas):
    grad = gradiente(X, Y, w)
    w -= lr * grad

    if epoca % 10 == 0:
        print(f"Época {epoca:3d} | Costo: {costo(X, Y, w):.6f} | w: {w:.6f}")

print(f"\nPeso final: {w:.6f}")
print(f"Esperado: 2.0")

# Predicción de prueba
x_de_prueba = 7
print(f"\nPredicción para x={x_de_prueba}: {predecir(x_de_prueba, w):.4f} (esperado {2 * x_de_prueba})")