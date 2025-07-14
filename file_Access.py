import numpy as np
import os

filename = "temperature_data.txt"

if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write("6 20\n")
        f.write("12 32\n")
        f.write("18 22\n")

def read_temperature_data(filename):
    x_vals = []
    y_vals = []
    with open(filename, 'r') as f:
        for line in f:
            hour, temp = map(float, line.strip().split())
            x_vals.append(hour)
            y_vals.append(temp)
    return x_vals, y_vals

def find_quadratic_coefficients(x, y):
    A = []
    for xi in x:
        A.append([xi**2, xi, 1])
    A = np.array(A)
    y = np.array(y)
    coeffs = np.linalg.solve(A, y)
    return coeffs

def predict_temperature(coeffs, x):
    a, b, c = coeffs
    return a * x**2 + b * x + c

if __name__ == "__main__":
    x_vals, y_vals = read_temperature_data(filename)
    coeffs = find_quadratic_coefficients(x_vals, y_vals)

    print(f"\nQuadratic Model: y = {coeffs[0]:.4f}x² + {coeffs[1]:.4f}x + {coeffs[2]:.4f}\n")
    print("Hourly Temperature Predictions:\n")

    for hour in range(0, 25):
        temp = predict_temperature(coeffs, hour)
        print(f"Hour {hour:02d}:00 → {temp:.2f}°C")
