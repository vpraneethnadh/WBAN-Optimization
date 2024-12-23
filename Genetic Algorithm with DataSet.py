import random
import math
import pandas as pd
from deap import base, creator, tools

# Load dataset with the correct delimiter and clean column names
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

# Replace commas with dots and convert to float
for col in columns_to_convert:
    data[col] = data[col].str.replace(',', '.').astype(float)

# Extract relevant coordinates from the cleaned dataset
SENSOR_POSITIONS = list(zip(
    data['Calculated atomic coordinates u'],
    data['Calculated atomic coordinates v']
))

# Number of nanotube structures
N_SENSORS = len(SENSOR_POSITIONS)

# Create Fitness and Individual classes for GA
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)


# Function to calculate Euclidean distance between two points
def euclidean_distance(sensor1, sensor2):
    return math.sqrt((sensor1[0] - sensor2[0]) ** 2 + (sensor1[1] - sensor2[1]) ** 2)


# Fitness function: Minimize total distance of the route
def evaluate(individual):
    total_distance = 0
    for i in range(len(individual) - 1):
        total_distance += euclidean_distance(SENSOR_POSITIONS[individual[i]], SENSOR_POSITIONS[individual[i + 1]])
    return total_distance,


# Create a random individual (route)
def create_individual():
    individual = list(range(N_SENSORS))
    random.shuffle(individual)
    return creator.Individual(individual)


# Crossover: Ordered crossover to combine two routes
def crossover(ind1, ind2):
    return tools.cxOrdered(ind1, ind2)


# Mutation: Shuffle some part of the individual (route)
def mutate(individual):
    return tools.mutShuffleIndexes(individual, indpb=0.2)


# Selection: Tournament selection based on fitness
def select(population, k):
    return tools.selTournament(population, k, tournsize=3)


# GA setup using DEAP
toolbox = base.Toolbox()
toolbox.register("individual", create_individual)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", evaluate)
toolbox.register("mate", crossover)
toolbox.register("mutate", mutate)
toolbox.register("select", select)


def main():
    # Create initial population
    population = toolbox.population(n=100)
    N_GEN = 15  # Number of generations
    CXPB, MUTPB = 0.7, 0.2  # Crossover and mutation probabilities

    # Evolutionary loop
    for gen in range(N_GEN):
        # Evaluate fitness of all individuals
        fitnesses = list(map(toolbox.evaluate, population))
        for ind, fit in zip(population, fitnesses):
            ind.fitness.values = fit

        # Select next generation individuals
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

        # Evaluate fitness of new individuals
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        # Replace old population with new offspring
        population[:] = offspring

        # Print the best route and distance in the current generation
        fits = [ind.fitness.values[0] for ind in population]
        best_individual = tools.selBest(population, 1)[0]
        print(f"Generation {gen}: Best route: {best_individual}, Distance: {min(fits)}")


if __name__ == "__main__":
    main()
