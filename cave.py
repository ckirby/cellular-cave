from __future__ import print_function

class Cave(object):
    def __init__(self, width=80, height=50, ratio=0.45, iterations=5, *args, **kwargs):
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
                neighbors = self.check_neighbors(x,y)
                if new_cave[x][y] and neighbors > 4:
	            new_cave[x][y] = True
	 	elif not new_cave[x][y] and neighbors > 5:
	            new_cave[x][y] = True
                else:
                    new_cave[x][y] = False
       if iteration == self.iterations:
           return
       self.cave = new_cave
       self.print_cave()
       self.mutate_cave(iteration+1)
        

    
    def print_cave(self):
        for x in range(self.height):
            for y in range(self.width):
                print("#", end='') if self.cave[x][y] else print(".", end='')
            print("")

    def check_neighbors(self, x, y) :
	live_neighbors = 0
        for neighbor in [[x+1, y],
			 [x-1, y],
			 [x, y+1],
			 [x, y-1],
                         [x+1, y+1],
                         [x+1, y-1],
                         [x-1, y+1],
                         [x-1, y-1]]:
	    try:
	        if self.cave[neighbor[0]][neighbor[1]]:
                    live_neighbors+=1
            except:
                live_neighbors+=1

        return live_neighbors 
