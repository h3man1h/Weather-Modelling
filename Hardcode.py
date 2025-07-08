import numpy as np

x_values = [6, 12, 18]
y_values = [20, 32, 22]

A = np.array([
    [x_values[0]**2, x_values[0], 1],
    [x_values[1]**2, x_values[1], 1],
    [x_values[2]**2, x_values[2], 1]
])

B = np.array(y_values)

a, b, c = np.linalg.solve(A, B)

print(f"Quadratic model: y = {a:.4f}x^2 + {b:.4f}x + {c:.4f}")

def temperature_at(hour):
    return a * hour**2 + b * hour + c

print("\nHourly forecast:")
for hour in range(0, 25):
    temp = temperature_at(hour)
    print(f"{hour:02d}:00 -> {temp:.2f}°C")
