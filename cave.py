
import click
class StableCaveException(Exception):
    pass


class Cave(object):
    def __init__(self, width, height, ratio, generations, print):
        self.width = width
        self.height = height
        self.generations = generations+1
        self.run(self.make_cave(ratio), print)

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


@click.command()
@click.option('-w', '--width', default=80, help='Cave Width')
@click.option('-h', '--height', default=50, help='Cave Height')
@click.option('-r', '--ratio', default=0.5, help='Ratio of initially alive cells. 0.3-0.6 recommended')
@click.option('-g', '--generations', default=2, help='Mutation Generations')
@click.option('-p', '--print', is_flag=True, default=False, help='Print all Generations')
def cave(**kwargs):
    Cave(**kwargs)


if __name__ == "__main__":
    cave()
