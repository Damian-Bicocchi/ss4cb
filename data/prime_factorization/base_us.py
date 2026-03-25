def prime_factorization(n: int) -> list[int]:
    """
    Compute the prime factorization of a given integer.

    This function returns a list containing the prime factors of the
    integer `n`. Each factor appears in the list as many times as it
    divides `n` (i.e., multiplicity is preserved).

    If `n` is less than 2, the function returns an empty list.

    Args:
        n (int): The integer to factorize.

    Returns:
        list[int]: A list of prime factors of `n`.
    """
    factors = []

    # Return empty list for invalid inputs
    if n < 2:
        return factors

    # Step 1: Extract all factors of 2 (the only even prime)
    while n % 2 == 0:
        factors.append(2)
        n //= 2  # Reduce n by dividing by 2

    # Step 2: Check for odd factors starting from 3
    divisor = 3
    while divisor * divisor <= n:
        # While divisor divides n, add it and reduce n
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 2  # Only check odd numbers

    # Step 3: If remaining n is greater than 1, it is a prime
    if n > 1:
        factors.append(n)

    return factors

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
        result = prime_factorization(n)
        assert result == expected, (
            f"Test failed for n={n}: expected {expected}, got {result}"
        )

    print("All tests passed successfully!")


if __name__ == "__main__":
    test_prime_factorization()