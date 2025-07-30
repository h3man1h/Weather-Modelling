import numpy as np
import matplotlib.pyplot as plt

# Step 1: Input Data
time = np.array([0, 4, 8, 12, 16, 20])  # Time in hours
rainfall = np.array([0, 2, 8, 15, 10, 3])  # Rainfall in mm
humidity = np.array([95, 85, 70, 60, 75, 90])  # Humidity in %

# Step 2: Fit quadratic models
rain_coeff = np.polyfit(time, rainfall, 2)
hum_coeff = np.polyfit(time, humidity, 2)

a_r, b_r, c_r = rain_coeff
a_h, b_h, c_h = hum_coeff

print(f"\nDeveloped Quadratic Model for Rainfall:")
print(f"R(t) = {a_r:.4f}t² + {b_r:.4f}t + {c_r:.4f}\n")

print(f"Developed Quadratic Model for Humidity:")
print(f"H(t) = {a_h:.4f}t² + {b_h:.4f}t + {c_h:.4f}\n")

# Step 3: Predict for every hour from 0 to 24
t_values = np.arange(0, 25, 1)
predicted_rainfall = a_r * t_values**2 + b_r * t_values + c_r
predicted_humidity = a_h * t_values**2 + b_h * t_values + c_h

print("Predicted Rainfall (mm) and Humidity (%) for 24 Hours:\n")
for t, rain, hum in zip(t_values, predicted_rainfall, predicted_humidity):
    print(f"At {t:02d}:00 hrs -> Rainfall: {rain:.2f} mm, Humidity: {hum:.2f} %")

# Step 4: Plot
plt.figure(figsize=(12, 6))

# Rainfall Plot
plt.subplot(1, 2, 1)
plt.scatter(time, rainfall, color='blue', label='Original Rainfall Data', zorder=5)
plt.plot(t_values, predicted_rainfall, color='red', linestyle='--', label='Rainfall Prediction')
plt.title('Rainfall Prediction using Quadratic Model')
plt.xlabel('Time (Hours)')
plt.ylabel('Rainfall (mm)')
plt.xticks(np.arange(0, 25, 2))
plt.grid(True)
plt.legend()

# Humidity Plot
plt.subplot(1, 2, 2)
plt.scatter(time, humidity, color='green', label='Original Humidity Data', zorder=5)
plt.plot(t_values, predicted_humidity, color='orange', linestyle='--', label='Humidity Prediction')
plt.title('Humidity Prediction using Quadratic Model')
plt.xlabel('Time (Hours)')
plt.ylabel('Humidity (%)')
plt.xticks(np.arange(0, 25, 2))
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
