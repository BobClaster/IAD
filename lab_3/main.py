import random
import copy


class Chromosome:
    def __init__(self, phenotype, generation=0, rate=None):
        self.phenotype = phenotype
        self.gene = bin(phenotype)
        self.calculated = 0
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
    def __init__(
            self, init_limit: int, final_limit: int, accuracy: float, population_number: int = 6,
            func: str = f"z / 7 + z ** 2 + z ** 3",
            given_accuracy: int = None, number_of_iterations: int = 100

    ):
        """

        :param init_limit:
        :param final_limit:
        :param accuracy:
        :param population_number:

        :param given_accuracy: value, for example [40]
        :param number_of_iterations: Default: 100
        """
        self.init_limit = init_limit
        self.final_limit = final_limit
        self.accuracy = accuracy
        self.population_number = population_number
        self.population = self._initial_population(init_limit, final_limit, population_number)

        self.func = func

        # if stop_condition and not number_of_iterations:
            # raise Exception("")
        #
        self.values = []
        self.max_value = 0
        self.average = 0
        self.probability_of_mutation = 0

    @staticmethod
    def _initial_population(init_limit: int, final_limit: int, n: int) -> list:
        population = []
        generation = 0
        for i in range(1, n + 1):
            instance = random.randint(init_limit, final_limit)
            if not (instance in population):
                population.append(
                    Chromosome(instance, generation)
                )
        return population

    # @staticmethod
    def calculation(self, z: float) -> float:
        return eval(self.func.replace("z", z))

    @staticmethod
    def roulette(population: list) -> list:
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

        point = random.randint(1, l - 1)
        if crossover:
            for i in range(len(bits) - point):
                bit_mask += bits[i]
        else:
            bit_mask = bits[point]

        return bit_mask

    def crossover(self, population: list) -> list:
        c_pop = copy.copy(population)
        partners = []
        new_populations = []
        while c_pop:
            pair = []
            # selection of partner for crossing
            numb = random.randint(0, len(c_pop) - 1)
            pair.append(c_pop.pop(numb))

            numb = random.randint(0, len(c_pop) - 1)
            pair.append(c_pop.pop(numb))

            partners.append(pair)

        for pair in partners:
            bitmask = self._create_bitmask()
            for instance in pair:
                instance.phenotype = instance.phenotype & bitmask
                instance.gene = bin(instance.phenotype)
                instance.update_generation()
                new_populations.append(instance)

        return new_populations

    def mutation(self, population: list) -> list:
        # bits_numb = self.population_number * 6
        # will_change_bit = round(bits_numb * self.probability_of_mutation)
        # TODO
        pass

    def do_live(self):
        c_population = copy.copy(self.population)
        for instance in c_population:
            instance.calculated = self.calculation(instance.phenotype)
            self.values.append(instance.calculated)

        self.max_value = max(self.values)

        after_roulete = self.roulette(c_population)
        new_population = self.crossover(after_roulete)
        return new_population

    def __call__(self, *args, **kwargs):
        cont = True
        final_limit = self.final_limit
        max_value = 0
        while cont:
            for instance in self.do_live():
                print(f"name: {instance.conventional_name}, "
                      f"phenotype: {instance.phenotype}, "
                      f"generation: {instance.generation}")
                print(f"max value: {self.max_value}")
                print(f"final_limit: {final_limit} ::: {instance.phenotype == final_limit}")

                if instance.phenotype == final_limit:
                    cont = False
                    break


obj = GeneticAlgorithm(20, 40, 0.00005)
obj()
