import itertools
import math
import random
import time


def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def generate_cities(n, seed=None):
    if seed is not None:
        random.seed(seed)
    return [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n)]


def compute_distance_matrix(cities):
    n = len(cities)
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = euclidean_distance(cities[i], cities[j])
    return dist


def tsp_brute_force(distance):
    n = len(distance)
    best_cost = float('inf')
    best_path = None
    for perm in itertools.permutations(range(1, n)):
        current_cost = distance[0][perm[0]]
        for i in range(len(perm) - 1):
            current_cost += distance[perm[i]][perm[i + 1]]
        current_cost += distance[perm[-1]][0]
        if current_cost < best_cost:
            best_cost = current_cost
            best_path = (0,) + perm + (0,)
    return best_cost, best_path


def nearest_neighbor(distance, start=0):
    n = len(distance)
    unvisited = set(range(n))
    unvisited.remove(start)
    path = [start]
    current = start
    total_cost = 0
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance[current][city])
        total_cost += distance[current][next_city]
        path.append(next_city)
        current = next_city
        unvisited.remove(next_city)
    total_cost += distance[current][start]
    path.append(start)
    return total_cost, path


def genetic_algorithm_tsp(distance, population_size=100, generations=500, mutation_rate=0.1):
    n = len(distance)

    def create_individual():
        ind = list(range(1, n))
        random.shuffle(ind)
        return ind

    def route_cost(individual):
        cost = distance[0][individual[0]]
        for i in range(len(individual) - 1):
            cost += distance[individual[i]][individual[i + 1]]
        cost += distance[individual[-1]][0]
        return cost

    def crossover(parent1, parent2):
        size = len(parent1)
        a, b = sorted(random.sample(range(size), 2))
        child = [None] * size
        child[a:b + 1] = parent1[a:b + 1]
        pos = (b + 1) % size
        for gene in parent2:
            if gene not in child:
                child[pos] = gene
                pos = (pos + 1) % size
        return child

    def mutate(individual):
        a, b = random.sample(range(len(individual)), 2)
        individual[a], individual[b] = individual[b], individual[a]
        return individual

    def tournament_selection(pop):
        k = 5
        selected = random.sample(pop, k)
        selected.sort(key=lambda ind: route_cost(ind))
        return selected[0]

    population = [create_individual() for _ in range(population_size)]
    best_individual = min(population, key=route_cost)
    best_cost = route_cost(best_individual)

    for _ in range(generations):
        new_population = []
        new_population.append(best_individual.copy())
        while len(new_population) < population_size:
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child = crossover(parent1, parent2)
            if random.random() < mutation_rate:
                child = mutate(child)
            new_population.append(child)
        population = new_population
        current_best = min(population, key=route_cost)
        current_cost = route_cost(current_best)
        if current_cost < best_cost:
            best_cost = current_cost
            best_individual = current_best.copy()

    best_path = [0] + best_individual + [0]
    return best_cost, best_path


def main():
    city_counts = [4, 6, 8]
    for n in city_counts:
        print(f"\n--- {n} cidades ---")
        cities = generate_cities(n, seed=42)
        distance = compute_distance_matrix(cities)


        start_time = time.time()
        cost_exact, path_exact = tsp_brute_force(distance)
        end_time = time.time()
        print("Solução exata (força bruta):")
        print("  Custo:", cost_exact)
        print("  Rota:", path_exact)
        print("  Tempo de execução: {:.6f} segundos".format(end_time - start_time))

        start_time = time.time()
        cost_greedy, path_greedy = nearest_neighbor(distance)
        end_time = time.time()
        print("\nHeurística gulosa (vizinho mais próximo):")
        print("  Custo:", cost_greedy)
        print("  Rota:", path_greedy)
        print("  Tempo de execução: {:.6f} segundos".format(end_time - start_time))

        start_time = time.time()
        cost_ga, path_ga = genetic_algorithm_tsp(distance, population_size=100, generations=500, mutation_rate=0.1)
        end_time = time.time()
        print("\nAlgoritmo Genético:")
        print("  Custo:", cost_ga)
        print("  Rota:", path_ga)
        print("  Tempo de execução: {:.6f} segundos".format(end_time - start_time))


if __name__ == "__main__":
    main()
