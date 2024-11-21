from flask import Flask, request, jsonify
from flask_cors import CORS
import math
import random
from deap import base, creator, tools

app = Flask(__name__)
CORS(app)

# Create GA-related classes
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))  # Minimize total distance
creator.create("Individual", list, fitness=creator.FitnessMin)

# Constants
POWER = 1.6e-9  # Joules

# Function to calculate Euclidean distance
def euclidean_distance(sensor1, sensor2):
    return math.sqrt(
        (sensor1[0] - sensor2[0]) ** 2 +
        (sensor1[1] - sensor2[1]) ** 2 +
        (sensor1[2] - sensor2[2]) ** 2
    )

# Non-Genetic distance calculation
def calculate_non_genetic_distance(sensor_positions):
    total_distance = 0
    for i in range(len(sensor_positions) - 1):
        total_distance += euclidean_distance(sensor_positions[i], sensor_positions[i + 1])
    total_distance += euclidean_distance(sensor_positions[-1], sensor_positions[0])  # Return to start
    return total_distance

# GA evaluation function
def evaluate(individual, sensor_positions):
    total_distance = 0
    for i in range(len(individual) - 1):
        total_distance += euclidean_distance(sensor_positions[individual[i]], sensor_positions[individual[i + 1]])
    total_distance += euclidean_distance(sensor_positions[individual[-1]], sensor_positions[individual[0]])
    return total_distance,  # Fitness value must be a tuple

def create_individual(n_sensors):
    individual = list(range(n_sensors))
    random.shuffle(individual)
    return creator.Individual(individual)

# Set up the DEAP toolbox
toolbox = base.Toolbox()
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.2)  # Mutation probability

toolbox.register("select", tools.selTournament, tournsize=3)

@app.route("/optimize", methods=["POST"])
def optimize():
    data = request.get_json()
    sensor_positions = data["sensor_positions"]
    n_sensors = len(sensor_positions)

    # Non-Genetic calculation
    non_genetic_route = list(range(n_sensors))
    non_genetic_distance = calculate_non_genetic_distance(sensor_positions)
    non_genetic_energy = POWER * non_genetic_distance
    non_genetic_energy_formatted = f"{non_genetic_energy:.2e}".replace("e", " x 10^")

    # GA-based calculation
    toolbox.register("individual", lambda: create_individual(n_sensors))
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("evaluate", lambda ind: evaluate(ind, sensor_positions))

    population = toolbox.population(n=300)  # Increased population size
    ngen = 200  # Number of generations
    cxpb = 0.7  # Crossover probability
    mutpb = 0.2  # Mutation probability

    for gen in range(ngen):
        offspring = toolbox.select(population, len(population))
        offspring = list(map(toolbox.clone, offspring))
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < cxpb:
                toolbox.mate(child1, child2)
                del child1.fitness.values, child2.fitness.values
        for mutant in offspring:
            if random.random() < mutpb:
                toolbox.mutate(mutant)
                del mutant.fitness.values
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        population[:] = offspring

    best_individual = tools.selBest(population, k=1)[0]
    ga_route = list(best_individual)
    ga_distance = best_individual.fitness.values[0]
    ga_energy = POWER * ga_distance
    ga_energy_formatted = f"{ga_energy:.2e}".replace("e", " x 10^")

    return jsonify({
        "non_genetic": {
            "route": non_genetic_route,
            "distance": non_genetic_distance,
            "energy": non_genetic_energy_formatted
        },
        "ga": {
            "route": ga_route,
            "distance": ga_distance,
            "energy": ga_energy_formatted
        }
    })

if __name__ == "__main__":
    app.run(debug=True)
