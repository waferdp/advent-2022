from heightMap import HeightMap
import fileReader

class Climbing:
    
    def __init__(self, input):
        self.start, self.finish, self.map = self.parseInput(input)
        self.paths = [[self.start]]
        self.visited = self.newVisited(self.paths)

    def newVisited(self, paths):
        visited = set()
        for path in paths:
            visited.add(path[-1])
        return visited

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

    def moreStarts(self):
        self.paths, self.visited = self.findLowStarts()

    def findLowStarts(self):
        starts = []
        visited = set()
        for y in range(0, self.map.height):
            for x in range(0, self.map.width):
                if self.map.get(x, y) == 0:
                    starts.append([(x,y)])
                    visited.add((x, y))
        return starts, visited


    def step(self):
        newPaths = []
        for path in self.paths:
            x,y = path[-1]
            possible = self.map.getPaths(x,y)
            for next in possible:
                if next in self.visited:
                    continue
                else:
                    newPaths.append(path + [next])
                    self.visited.add(next)
        self.paths = newPaths

    def climb(self):
        steps = 0
        while True:
            steps += 1
            self.step()
            finished = [path[-1] == self.finish for path in self.paths]
            if not len(finished):
                return f'Error after {steps} step'
            if any(finished):
                return (min(map(len, self.paths)) - 1)


if __name__ == '__main__':
    input = fileReader.read('input.txt')
    climbing = Climbing(input)
    climbing.moreStarts()
    shortestPath = climbing.climb()
    print(shortestPath)
