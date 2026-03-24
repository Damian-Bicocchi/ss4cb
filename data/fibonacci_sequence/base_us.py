def nth_fibonacci(n: int) -> int:
    """
    Calculate the nth number in the Fibonacci sequence.

    The Fibonacci sequence is defined as:
        F(0) = 0
        F(1) = 1
        F(n) = F(n-1) + F(n-2) for n >= 2

    Parameters:
        n (int): The position in the Fibonacci sequence (must be >= 0).

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is a negative integer.
    """
    # Validate input
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Handle base cases directly
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Initialize the first two Fibonacci numbers
    prev, curr = 0, 1

    # Iteratively compute up to the nth number
    for _ in range(2, n + 1):
        # Update values: next = prev + curr
        prev, curr = curr, prev + curr

    return curr


# =========================
# Short test (correctness)
# =========================
if __name__ == "__main__":
    # Known Fibonacci values for testing
    test_cases = {
        0: 0,
        1: 1,
        2: 1,
        3: 2,
        5: 5,
        10: 55,
        15: 610,
    }

    for n, expected in test_cases.items():
        result = nth_fibonacci(n)
        print(f"F({n}) = {result} | Expected: {expected}")
        assert result == expected, f"Test failed for n={n}"

    print("All tests passed successfully!")