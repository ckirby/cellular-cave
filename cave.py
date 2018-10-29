class Cave(object):
    def __init__(self, width, height, ratio, generations, *args, **kwargs):
        self.width = width
        self.height = height
        self.generations = generations
        self.cave = self.make_cave(ratio*10)
        self.mutate_cave()

    def make_cave(self, ratio):
        from random import random
        cave = []
        random_integers = None
        for x in range(self.height):
            row = []
            for y in range(self.width):
                try:
                    cell_integer = random_integers.pop()
                except (IndexError, AttributeError):
                    random_integers = [int(ri) for ri in str(random()).split('.')[1].split('e')[0]]
                    cell_integer = random_integers.pop()
                finally:
                    row.append(cell_integer < ratio)
            cave.append(row)

        return cave

    def mutate_cave(self, generation=0):
        if generation > self.generations:
            return

        new_cave = list(self.cave)
        for x in range(self.height):
            for y in range(self.width):
                new_cave[x][y] = self.check_neighbors(x, y) > 4

        self.cave = new_cave
        self.mutate_cave(generation + 1)

    def print_cave(self):
        for x in range(self.height):
            for y in range(self.width):
                print("#", end='') if self.cave[x][y] else print(" ", end='')
            print("")

    def check_neighbors(self, x, y):
        live_neighbors = 0
        neighbor_range = range(-1, 2)
        for nx in neighbor_range:
            for ny in neighbor_range:
                try:
                    live_neighbors += 1*self.cave[x + nx][y + ny]
                except IndexError:
                    live_neighbors += .5

        return live_neighbors


def main(**kwargs):
    c = Cave(**kwargs)
    c.print_cave()


def parse_arguments():
    import argparse

    parser = argparse.ArgumentParser(description='Generate a Cave Map via Cellular Automata')
    parser.add_argument('-W', '--width', type=int, default=80, help='Cave Width')
    parser.add_argument('-H', '--height', type=int, default=50, help='Cave Height')
    parser.add_argument('-R', '--ratio', type=float, default=.5, help='Ratio of initially alive cells')
    parser.add_argument('-G', '--generations', type=int, default=3, help='Cellullar Generations')

    args = parser.parse_args()
    return vars(args)


if __name__ == "__main__":
    arguments = parse_arguments()
    main(**arguments)
