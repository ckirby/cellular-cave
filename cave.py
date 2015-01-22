from __future__ import print_function

class Cave(object):
    def __init__(self, width=80, height=50, ratio=0.5, iterations=3, *args, **kwargs):
        self.width = width
        self.height = height
        self.iterations = iterations
        self.cave = self.make_cave(ratio)
        self.mutate_cave(0)

    def make_cave(self, ratio):
       from random import random
       cave = []
       for x in range(self.height):
           row = []
           for y in range(self.width):
               row.append(random() < ratio)
           cave.append(row)

       return cave

    def mutate_cave(self, iteration):
        new_cave = list(self.cave)
        for x in range(self.height):
            for y in range(self.width):
                neighbors = self.check_neighbors(x, y)
                if neighbors > 4:
                   new_cave[x][y] = True
                else:
                    new_cave[x][y] = False

        if iteration == self.iterations:
            return
        self.cave = new_cave
        self.mutate_cave(iteration + 1)

    def print_cave(self):
        for x in range(self.height):
            for y in range(self.width):
                print("#", end='') if self.cave[x][y] else print(" ", end='')
            print("")

    def check_neighbors(self, x, y) :
        live_neighbors = 0
        neighbor_range = range(-1, 2)
        for nx in neighbor_range:
            for ny in neighbor_range:
                try:
                    if self.cave[x + nx][y + ny]:
                        live_neighbors += 1
                except:
                    live_neighbors += .5

        return live_neighbors

def main():
    c = Cave()
    c.print_cave()

if __name__ == "__main__":
    main()

