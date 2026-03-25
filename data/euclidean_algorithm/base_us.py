def euclidean_gcd(first_number: int, second_number: int) -> int:
    """
    Compute the Greatest Common Divisor (GCD) of two positive integers
    using the classic subtraction-based Euclidean Algorithm.

    Args:
        first_number (int): First positive integer.
        second_number (int): Second positive integer.

    Returns:
        int: The GCD of first_number and second_number.

    Raises:
        ValueError: If either first_number or second_number is zero or negative.
    """
    # Validate that both inputs are strictly positive integers;
    # GCD is undefined for zero and not applicable to negative numbers.
    if first_number <= 0 or second_number <= 0:
        raise ValueError(
            "Both numbers must be strictly positive integers (> 0). "
            f"Received: first_number={first_number}, second_number={second_number}."
        )

    # Keep iterating as long as the two values differ.
    # When they become equal, that value is the GCD.
    while first_number != second_number:

        if first_number > second_number:
            # If first_number is larger, replace it with the difference (first_number - second_number).
            # This mirrors: GCD(first_number, second_number) = GCD(first_number - second_number, second_number)
            first_number = first_number - second_number
        else:
            # If second_number is larger (or they could be equal, handled by the while
            # condition), replace second_number with the difference (second_number - first_number).
            # This mirrors: GCD(first_number, second_number) = GCD(first_number, second_number - first_number)
            second_number = second_number - first_number

    # At this point first_number == second_number, so either variable holds the GCD.
    return first_number