class StableCaveException(Exception):
    pass


class Cave(object):
    def __init__(self, width, height, ratio, generations, history):
        self.width = width
        self.height = height
        self.generations = generations+1
        self.run(self.make_cave(ratio), history)

    def run(self, cave, should_print):
        for gen in range(1, self.generations):
            if should_print:
                self.print_cave(cave, gen)
            try:
                cave = self.mutate_cave(cave)
            except StableCaveException:
                if not should_print:
                    self.print_cave(cave)
                print(f"Cave mutations converged at generation {gen}")
                break

        if not should_print:
            self.print_cave(cave)

    def make_cave(self, ratio):
        from random import random
        cave = []
        for x in range(self.height):
            row = []
            for y in range(self.width):
                row.append(random() < ratio)
            cave.append(row)

        return cave

    def mutate_cave(self, cave):
        from copy import deepcopy
        new_cave = deepcopy(cave)
        for x in range(self.height):
            for y in range(self.width):
                new_cave[x][y] = self.check_neighbors(cave, x, y) > 4

        if new_cave == cave:
            raise StableCaveException

        return new_cave


    def print_cave(self, cave, generation = None):
        if generation is not None:
            print(f"Generation {generation}")
        for x in range(self.height):
            for y in range(self.width):
                print("#", end='') if cave[x][y] else print(" ", end='')
            print("")

    def check_neighbors(self, cave, x, y):
        live_neighbors = 0
        neighbor_range = range(-1, 2)
        for nx in neighbor_range:
            for ny in neighbor_range:
                try:
                    live_neighbors += 1*cave[x + nx][y + ny]
                except IndexError:
                    live_neighbors += .5

        return live_neighbors


def main(**kwargs):
    Cave(**kwargs)

def parse_arguments():
    import argparse

    parser = argparse.ArgumentParser(description='Generate a Cave Map via Cellular Automata')
    parser.add_argument('-W', '--width', type=int, default=80, help='Cave Width')
    parser.add_argument('-H', '--height', type=int, default=50, help='Cave Height')
    parser.add_argument('-R', '--ratio', type=float, default=0.5, help='Ratio of initially alive cells. 0.3-0.6 recommended')
    parser.add_argument('-G', '--generations', type=int, default=2, help='Mutation Generations')
    parser.add_argument('--history', type=bool, default=False, help='Print all Generations')

    args = parser.parse_args()
    return vars(args)


if __name__ == "__main__":
    arguments = parse_arguments()
    main(**arguments)
