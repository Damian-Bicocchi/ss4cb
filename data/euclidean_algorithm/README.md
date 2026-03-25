# Algorithm name
Euclidean Greatest Common Divisor Algorithm

## Author
Andrés Murray Roppel (2026-03-23)

## Algorithm description
The subtraction-based form of the Euclidean algorithm is a simple method for computing the greatest common divisor (GCD) of two integers, the largest number that divides them both without a remainder. The algorithm is based on the principle that the greatest common divisor of two numbers does not change if the larger number is replaced by its difference with the smaller number. This process is repeated until the two numbers are equal, at which point that value is the GCD. While conceptually straightforward, this subtraction-based variant can require many iterations for very imbalanced inputs and is generally less efficient than the more common modulo-based Euclidean algorithm.


## Model used to create the base code
Claude Sonnet 4.6

### Prompt
```
Write a Python function to implement the original Euclidean Algorithm to find the Greatest Common Divisor (GCD) of two numbers a and b. Use the classic subtraction-based method instead of the modulo operator %. Please include descriptive comments in English explaining each step of the logic.

```

## Obfuscated version
manually obfuscated

