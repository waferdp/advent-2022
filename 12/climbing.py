from heightMap import HeightMap

class Climbing:
    
    def __init__(self, input):
        self.start, self.finish, self.map = self.parseInput(input)
        self.paths = [[self.start]]
        self.deadEnds = set()

    def parseInput(self, input):
        start = None
        finish = None
        a = 0
        z = ord('z') - ord('a')
        map = HeightMap(height=len(input), width=len(input[0]), default=z+2)
        for y in range(0, len(input)):
            for x in range(len(input[y])):
                letter = input[y][x]
                if letter == 'S':
                    start = (x, y)
                    map.set(x, y, 0)
                elif letter == 'E':
                    finish = (x, y)
                    map.set(x, y, 25)
                else:
                    map.set(x, y, ord(letter)-97)
        return start, finish, map

        
    def step(self):
        newPaths = []
        for path in self.paths:
            x,y = path[-1]
            possible = self.map.getPaths(x,y)
            if len(path) > 1:
                possible.remove(path[-2])
            for deadEnd in self.deadEnds:
                possible.remove(deadEnd)
            if not len(possible):
                self.deadEnds.add(path[-1])
            else:
                for next in possible:
                    newPaths.append(path + [next])
        self.paths = newPaths


