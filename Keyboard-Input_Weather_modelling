import numpy as np

x_values = []
y_values = []

for i in range(3):
    x = float(input(f"Enter hour x{i+1}: "))
    y = float(input(f"Enter temperature at hour {x}: "))
    x_values.append(x)
    y_values.append(y)

A = np.array([
    [x_values[0]**2, x_values[0], 1],
    [x_values[1]**2, x_values[1], 1],
    [x_values[2]**2, x_values[2], 1]
])

B = np.array(y_values)

a, b, c = np.linalg.solve(A, B)

print(f"\nQuadratic model: y = {a:.4f}x^2 + {b:.4f}x + {c:.4f}\n")

def temperature_at(hour):
    return a * hour**2 + b * hour + c

print("Hourly forecast:")
for hour in range(0, 25):
    temp = temperature_at(hour)
    print(f"{hour:02d}:00 -> {temp:.2f}°C")
