# Linear Regression using Gradient Descent (y = w * x)

# Example data: y = 2x
X = [1, 2, 3, 4, 5]
Y = [2, 4, 6, 8, 10]

w = 0.0           # initial weight
lr = 0.01         # learning rate
epochs = 100      # training iterations
n = len(X)


def predict(x, w):
    return w * x


def cost(X, Y, w):
    """Mean Squared Error"""
    return sum((predict(x, w) - y) ** 2 for x, y in zip(X, Y)) / n


def gradient(X, Y, w):
    """Derivative of MSE with respect to w"""
    return sum(2 * (predict(x, w) - y) * x for x, y in zip(X, Y)) / n


# Training loop
for epoch in range(epochs):
    grad = gradient(X, Y, w)
    w -= lr * grad

    if epoch % 10 == 0:
        print(f"Epoch {epoch:3d} | Cost: {cost(X, Y, w):.6f} | w: {w:.6f}")

print(f"\nFinal weight: {w:.6f}")
print(f"Expected: 2.0")

# Test prediction
test_x = 7
print(f"\nPrediction for x={test_x}: {predict(test_x, w):.4f} (expected {2 * test_x})")