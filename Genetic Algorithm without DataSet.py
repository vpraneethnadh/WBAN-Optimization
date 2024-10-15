import random
import math
from deap import base, creator, tools

# Define the number of sensors
N_SENSORS = 9

# Define the positions of the sensors (updated values)
SENSOR_POSITIONS = [
    (160, 270),  # Sensor 1
    (180, 210),  # Sensor 2
    (140, 300),  # Sensor 3
    (220, 180),  # Sensor 4
    (230, 290),  # Sensor 5
    (190, 110),  # Sensor 6
    (140, 410),  # Sensor 7
    (180, 400),  # Sensor 8
    (180, 160),  # Sensor 9
]

# Create Fitness and Individual classes
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

# Function to calculate the Euclidean distance between two sensors
def euclidean_distance(sensor1, sensor2):
    return math.sqrt((sensor1[0] - sensor2[0]) ** 2 + (sensor1[1] - sensor2[1]) ** 2)

# Fitness function: Minimize the total distance for the route
def evaluate(individual):
    total_distance = 0
    for i in range(len(individual) - 1):
        total_distance += euclidean_distance(SENSOR_POSITIONS[individual[i]], SENSOR_POSITIONS[individual[i + 1]])
    return total_distance,

# Function to create a random individual (a random route through all sensors)
def create_individual():
    individual = list(range(N_SENSORS))
    random.shuffle(individual)
    return creator.Individual(individual)

# Crossover: Ordered crossover to combine two routes
def crossover(ind1, ind2):
    return tools.cxOrdered(ind1, ind2)

# Mutation: Shuffle some part of an individual (route)
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
    # Create an initial population
    population = toolbox.population(n=100)
    N_GEN = 50  # Number of generations
    CXPB, MUTPB = 0.7, 0.2  # Crossover and mutation probabilities

    # Evolutionary loop
    for gen in range(N_GEN):
        # Evaluate the fitness of all individuals in the population
        fitnesses = list(map(toolbox.evaluate, population))
        for ind, fit in zip(population, fitnesses):
            ind.fitness.values = fit

        # Select individuals for the next generation
        offspring = toolbox.select(population, len(population))
        offspring = list(map(toolbox.clone, offspring))

        # Apply crossover and mutation to the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # Evaluate the fitness of new individuals
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        # Replace the old population with the new one
        population[:] = offspring

        # Print the best route and distance in the current generation
        fits = [ind.fitness.values[0] for ind in population]
        best_individual = tools.selBest(population, 1)[0]
        print(f"Generation {gen}: Best route: {best_individual}, Distance: {min(fits)}")

if __name__ == "__main__":
    main()
