def factorizacion_en_primos(n: int) -> list[int]:
    """
    Computa la factorización en números primos de un entero dado.
    Esta función devuelve una lista que contiene los factores primos del
    entero `n`. Cada factor aparece en la lista tantas veces como
    divide a `n` (es decir, se conserva la multiplicidad).

    Si `n` es menor a 2, la función retorna una lista vacía

    Argumentos:
        n (int): El entero a factorizar.

    Returns:
        list[int]: Una lista de los factores primos de`n`.
    """
    factores = []

    # Retorna una lista vacia para inputs inválidos
    if n < 2:
        return factores

    
    # Paso 1: Extraer todos los factores de dos (El único primo par)
    while n % 2 == 0:
        factores.append(2)
        n //= 2  # Reducir n dividiendo entre 2

    # Paso 2: Chequea por factores impares empezando por el 3
    divisor = 3
    while divisor * divisor <= n:
        # Mientras el divisor divida a n, añadirlo y reducir n
        while n % divisor == 0:
            factores.append(divisor)
            n //= divisor
        divisor += 2  # Solo chequear números impares

    # Paso 3: Si queda un n remanente mayor a 1, entonces es un primo
    if n > 1:
        factores.append(n)

    return factores

def test_prime_factorization():
    """
    Basic test cases for the prime_factorization function.
    """

    test_cases = [
        (0, []),
        (1, []),
        (2, [2]),
        (3, [3]),
        (4, [2, 2]),
        (6, [2, 3]),
        (12, [2, 2, 3]),
        (25, [5, 5]),
        (49, [7, 7]),
        (60, [2, 2, 3, 5]),
        (97, [97]),  # prime number
        (100, [2, 2, 5, 5]),
    ]

    for n, expected in test_cases:
        result = factorizacion_en_primos(n)
        assert result == expected, (
            f"Test failed for n={n}: expected {expected}, got {result}"
        )

    print("All tests passed successfully!")


if __name__ == "__main__":
    test_prime_factorization()