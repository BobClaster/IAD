import random
import copy

GENE = "bin"
PHENOTYPE = "dec"


class Chromosome:
    def __init__(self, phenotype, generation=0, rate=None):
        self.phenotype = phenotype
        self.gene = bin(phenotype)
        self.generation = generation
        self.conventional_name = ""
        self.rate = rate

        # set chromosome name
        self.new_name()

    def new_name(self, old_name=""):
        self.generation += 1
        if not old_name:
            self.conventional_name = f"x{self.generation}-{self.phenotype}-{random.randint(1, 9)}"
        else:
            self.conventional_name = f"x{self.generation}-{self.phenotype}-{old_name[-1]}"

    def __str__(self):
        return self.conventional_name

    def __call__(self, *args, **kwargs):
        return self.phenotype, self.gene


class GeneticAlgorithm:
    def __init__(self):
        self.min = 20
        self.max = 40
        self.step = 0.00001
        self.init_pop = self._initial_population(self.min, self.max, 6)

    @staticmethod
    def _initial_population(init_limit: int, final_limit: int, n: int) -> list:
        population = []
        generation = 0
        for i in range(1, n+1):
            instance = random.randint(init_limit, final_limit)
            if not (instance in population):
                population.append(
                    Chromosome(instance, generation)
                )
        return population

    @staticmethod
    def _calculation(z: float) -> float:
        return z / 7 + z ** 2 + z ** 3

    @staticmethod
    def _roulette(population: list) -> list:
        instances_sum = 0
        new_population = []
        roulette = []
        result = []

        # full rate
        for instance in population:
            instances_sum += instance.phenotype

        # set chromosome rate
        for instance in population:
            instance.rate = round(instance.phenotype / instances_sum * 100)

        # creating data for roulette
        for instance in population:
            roulette += [instance.conventional_name] * instance.rate

        # Natural selection
        for i in range(len(population)):
            result.append(random.choice(roulette))

        # creating new population
        for x_name in result:
            chromosome = None
            # If the gene is repeated, copy it
            for instance in new_population:
                if x_name == instance.conventional_name:
                    chromosome = copy.copy(instance)
                    chromosome.new_name(instance.conventional_name)

            if chromosome:
                new_population.append(chromosome)
            else:
                for instance in population:
                    if x_name == instance.conventional_name:
                        new_population.append(instance)

        return new_population

    @staticmethod
    def _crossover(population: dict) -> list:
        list_pop = list(population.keys())
        partners = []
        for i in range(len(list_pop) // 2):
            partners.append([
                list_pop.pop(random.choice(list_pop)),
                list_pop.pop(random.choice(list_pop)),
            ])
        return partners

    def mutation(self, x1, x2):
        pass



    def genetic(self):
        pass


obj = GeneticAlgorithm()
a = {"x1": 200, "x2":320, "x3":54, "x4": 76}
# print(obj._initial_population(a))
# print([i.conventional_name for i in obj.init_pop])
print([i.conventional_name for i in obj._roulette(obj.init_pop)])