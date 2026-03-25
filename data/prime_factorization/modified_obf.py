def factorizacion_en_primos(n: int) -> list[int]:
    factores = []

    
    if n < 2:
        return factores

    
    
    while n % 2 == 0:
        factores.append(2)
        n //= 2 

    
    divisor = 3
    while divisor * divisor <= n:
        
        while n % divisor == 0:
            factores.append(divisor)
            n //= divisor
        divisor += 2  

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