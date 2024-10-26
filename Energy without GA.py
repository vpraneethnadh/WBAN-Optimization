# WITHOUT USING GA ALGORITHM

import random
import math
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset and clean it
data = pd.read_csv("carbon_nanotubes.csv", delimiter=',', skipinitialspace=True)
data.columns = data.columns.str.strip().str.replace("'", "")
columns_to_convert = [
    "Initial atomic coordinate u",
    "Initial atomic coordinate v",
    "Initial atomic coordinate w",
    "Calculated atomic coordinates u",
    "Calculated atomic coordinates v",
    "Calculated atomic coordinates w",
]
for col in columns_to_convert:
    data[col] = data[col].str.replace(',', '.').astype(float)

# Extract relevant coordinates from the dataset
SENSOR_POSITIONS = list(zip(
    data['Calculated atomic coordinates u'],
    data['Calculated atomic coordinates v']
))

# Number of sensors
N_SENSORS = len(SENSOR_POSITIONS)

# Energy model parameters
P_TX = 0.1  # Power consumption per distance unit (Joules per unit distance)


# Calculate Euclidean distance between two points
def euclidean_distance(sensor1, sensor2):
    return math.sqrt((sensor1[0] - sensor2[0]) ** 2 + (sensor1[1] - sensor2[1]) ** 2)


# Non-GA method to calculate the shortest route (brute force)
def non_ga_route():
    best_route = list(range(N_SENSORS))
    random.shuffle(best_route)
    min_energy = float('inf')

    for _ in range(1000):  # Simulate random attempts (brute force style)
        random.shuffle(best_route)
        total_energy = 0
        for i in range(len(best_route) - 1):
            total_energy += euclidean_distance(SENSOR_POSITIONS[best_route[i]],
                                               SENSOR_POSITIONS[best_route[i + 1]]) * P_TX
        if total_energy < min_energy:
            min_energy = total_energy
            optimal_route = best_route[:]

    return optimal_route, min_energy


# Plotting the best route
def plot_route(route, title, energy):
    plt.figure(figsize=(10, 5))

    # Plot sensor positions
    x, y = zip(*SENSOR_POSITIONS)
    plt.scatter(x, y, color="blue", label="Sensors")

    # Plot route between sensors
    route_loop = route + [route[0]]
    for i in range(len(route_loop) - 1):
        sensor1 = SENSOR_POSITIONS[route_loop[i]]
        sensor2 = SENSOR_POSITIONS[route_loop[i + 1]]
        plt.plot([sensor1[0], sensor2[0]], [sensor1[1], sensor2[1]], 'r-', label="Route" if i == 0 else "")

    plt.title(f"{title}: Total Energy = {energy}")
    plt.legend()
    plt.show()


def main():
    optimal_route_non_ga, min_energy_non_ga = non_ga_route()
    plot_route(optimal_route_non_ga, "Non-GA Route", min_energy_non_ga)

    print(f"Non-GA Minimum Energy: {min_energy_non_ga}")


if __name__ == "__main__":
    main()

# X-axis: Represents the horizontal positions of the sensors in a scaled format.
# Y-axis: Represents the vertical positions of the sensors in a scaled format.
# Blue dot: Represents the sensors
# Red line: Represents the route between sensors
# Plotting is done using MatPlot
# We are calculating the best route energy efficiency.
# This is Using Non-GA.