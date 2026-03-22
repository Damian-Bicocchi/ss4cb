# Algorithm name
Linear Regression using Gradient Descent

## Author
Salvador Karakachoff (2026-03-22)

## Algorithm description
Linear regression is a method for modeling the relationship between an input variable and an output variable by fitting a straight line (y = w * x). This algorithm finds the optimal weight w using gradient descent, an iterative optimization technique. It starts with an initial weight of zero, computes the Mean Squared Error (MSE) as a measure of prediction quality, and calculates its derivative with respect to w to determine the direction of steepest cost reduction. On each iteration, the weight is adjusted by subtracting the gradient scaled by a learning rate, progressively reducing the error. After a fixed number of epochs, the weight converges to the value that best fits the data.

## Model used to create the base code
opus-4.6

### Prompt
```
Generate a code snippet in Python that implements linear regression using gradient descent.

Requirements:
- Do not use external libraries.
- Use a cost function (mean squared error).
- Train a single parameter model (y = w * x).
- Include simple example data (e.g., y = 2x).
- Add brief comments explaining each part.
```

## Obfuscated version
manually obfuscated