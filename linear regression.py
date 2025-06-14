# LINEAR REGRESSION 
#we have data points x ,y and we have to predict y by mx+c  by taking m and c as any value
#and then find error by mean square error between actual y and predicted y 
# and then tweek m and c to minimize error.
# Sample data: X = years of experience, Y = salary


X = [1, 2, 3, 4, 5]
Y = [15000, 18000, 21000, 24000, 27000]

# Function to predict y values
def predict_y(X, m=0, c=0):
    return [m * x + c for x in X]

# Function to calculate Mean Squared Error
def mean_square_error(X, Y, m, c):
    y_pred = predict_y(X, m, c)
    return sum((y_pred[i] - Y[i]) ** 2 for i in range(len(Y))) / len(Y)

# Function to compute derivative
def diff(f, x):
    delta = 1e-6
    return (f(x + delta) - f(x)) / delta

# Gradient Descent function
def gradient_descent(X, Y, iterations=1000, learning_rate=0.01):
    m, c = 0, 0  # Initial parameters
    for i in range(iterations):
        d_m = diff(lambda m: mean_square_error(X, Y, m, c), m)
        d_c = diff(lambda c: mean_square_error(X, Y, m, c), c)
        m -= learning_rate * d_m
        c -= learning_rate * d_c
    print(f"Iteration {i}: m={m}, c={c}")
    return m, c


X = [1, 2, 3, 4, 5]
Y = [15000, 18000, 21000, 24000, 27000]
m, c = gradient_descent(X, Y)