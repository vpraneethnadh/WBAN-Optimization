# USING GA ALGORITHM

import random
import math
import pandas as pd
import matplotlib.pyplot as plt
from deap import base, creator, tools

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

# Create Fitness and Individual classes for GA
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)


# Calculate Euclidean distance between two points
def euclidean_distance(sensor1, sensor2):
    return math.sqrt((sensor1[0] - sensor2[0]) ** 2 + (sensor1[1] - sensor2[1]) ** 2)


# Fitness function for GA
def evaluate(individual):
    total_energy = 0
    for i in range(len(individual) - 1):
        distance = euclidean_distance(SENSOR_POSITIONS[individual[i]], SENSOR_POSITIONS[individual[i + 1]])
        total_energy += distance * P_TX
    return total_energy,


# Create a random individual (route)
def create_individual():
    individual = list(range(N_SENSORS))
    random.shuffle(individual)
    return creator.Individual(individual)


# Crossover, mutation, and selection functions for GA
def crossover(ind1, ind2):
    return tools.cxOrdered(ind1, ind2)


def mutate(individual):
    return tools.mutShuffleIndexes(individual, indpb=0.2)


def select(population, k):
    return tools.selTournament(population, k, tournsize=3)


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


# GA simulation using DEAP
def ga_route():
    toolbox = base.Toolbox()
    toolbox.register("individual", create_individual)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("evaluate", evaluate)
    toolbox.register("mate", crossover)
    toolbox.register("mutate", mutate)
    toolbox.register("select", select)

    # Create initial population
    population = toolbox.population(n=100)
    N_GEN = 15
    CXPB, MUTPB = 0.7, 0.2  # CrossOver and Mutation values

    for gen in range(N_GEN):
        # Evaluate all individuals
        fitnesses = list(map(toolbox.evaluate, population))
        for ind, fit in zip(population, fitnesses):
            ind.fitness.values = fit

        # Select the next generation
        offspring = toolbox.select(population, len(population))
        offspring = list(map(toolbox.clone, offspring))

        # Apply crossover and mutation
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # Evaluate fitness of the new individuals
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        population[:] = offspring

    # Get the best individual (route)
    best_individual = tools.selBest(population, 1)[0]
    return best_individual, best_individual.fitness.values[0]


def main():
    best_individual_ga, min_energy_ga = ga_route()
    plot_route(best_individual_ga, "GA-Optimized Route", min_energy_ga)

    print(f"GA-Optimized Minimum Energy: {min_energy_ga}")


if __name__ == "__main__":
    main()

# X-axis: Represents the horizontal positions of the sensors in a scaled format.
# Y-axis: Represents the vertical positions of the sensors in a scaled format.
# Blue dot: Represents the sensors
# Red line: Represents the route between sensors
# We are calculating the best route energy efficiency.
# Plotting is done using MatPlot
# This is Using GA(Genetic Algorithm).
