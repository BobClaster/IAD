import random

BINARY = "bin"
DECIMAL = "dec"


class GeneticAlgorithm:
    def __init__(self):
        self.min = 20
        self.max = 40
        self.step = 0.00001

    @staticmethod
    def _initial_population(init_limit: int, final_limit: int, n: int) -> dict:
        population = {}
        for i in range(1, n+1):
            instance = random.randint(init_limit, final_limit)
            if not (instance in population):
                population[f"x{i}"] = {DECIMAL: instance, BINARY: bin(instance)}

        return population

    @staticmethod
    def _calculation(z: float) -> float:
        return z / 7 + z ** 2 + z ** 3

    @staticmethod
    def _roulette(population: dict) -> list:
        instances_sum = 0
        population_rate = {}
        roulette = []
        result = []

        for instance in population:
            instances_sum += population[instance]

        for instance in population:
            population_rate[instance] = round(population[instance] / instances_sum * 100)

        for instance in population_rate:
            roulette += [instance] * population_rate[instance]

        for i in range(len(population)):
            result.append(random.choice(roulette))

        return result

    def mutation(self, x1, x2):
        pass

    def crossover(self):
        pass

    def genetic(self):
        pass


obj = GeneticAlgorithm()
a = {"x1": 200, "x2":320, "x3":54, "x4": 76}
print(obj._initial_population(20, 40, 5))