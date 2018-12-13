import random
import copy


class Chromosome:
    def __init__(self, phenotype, generation=0, rate=None):
        self.phenotype = phenotype
        self.calculated = 0
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

    def update_generation(self):
        self.generation += 1

    def __str__(self):
        return self.conventional_name

    def __call__(self, *args, **kwargs):
        return self.phenotype, self.gene


class GeneticAlgorithm:
    def __init__(self, init_limit: int, final_limit: int, accuracy: float):
        self.min = init_limit
        self.max = final_limit
        self.step = accuracy
        self.population = self._initial_population(self.min, self.max, 6)
        self.half_value = 0

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
    def _create_bitmask(l=6, crossover=True) -> int:
        bits = [32, 16, 8, 4, 2, 1]
        bit_mask = 0

        point = random.randint(1, l)
        if crossover:
            for i in range(len(bits)-point):
                bit_mask += bits[i]
        else:
            bit_mask = bits[point]

        return bit_mask

    def _crossover(self, population: list) -> list:
        c_pop = copy.copy(population)
        partners = []
        new_populations = []
        while c_pop:
            pair = []
            # selection of partner for crossing
            numb = random.randint(0, len(c_pop)-1)
            pair.append(c_pop.pop(numb))

            numb = random.randint(0, len(c_pop)-1)
            pair.append(c_pop.pop(numb))

            partners.append(pair)

        for pair in partners:
            bitmask = self._create_bitmask()
            for instance in pair:
                instance.phenotype = instance.phenotype & bitmask
                instance.update_generation()
                new_populations.append(instance)

        return new_populations

    def mutation(self, x1, x2):
        pass

    def do_live(self):
        pass


obj = GeneticAlgorithm()
# a = {"x1": 200, "x2":320, "x3":54, "x4": 76}
# print(obj._initial_population(a))
# print([i.conventional_name for i in obj.population])
# print([i.conventional_name for i in obj._roulette(obj.population)])
# obj.population = obj._roulette(obj.population)
# pairs = [pair for pair in obj._crossover(obj.population)]
# # print(pairs)
# for pair in pairs:
#     print([i.conventional_name for i in pair])
#     mx = pair[0].phenotype if pair[0].phenotype >= pair[1].phenotype else pair[1].phenotype
#     print(obj._create_bitmask(mx))

