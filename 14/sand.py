from matrix import Matrix2d
from cave import Cave
import fileReader
import json

class Sand:

    def __init__(self, input, big = False):
        self.rockVectors = self.parseRocks(input)
        minX = self.getMinMax()[0]
        self.rockVectors = self.translateRocksX(self.rockVectors, (minX * -1))
        self.origin = (500 - minX, 0)
        self.cave = self.makeCave(big)
        self.big = big
        #self.cave = Cave(width=maxX+1, height= maxY+1, default='.')
        self.cave.set(self.origin[0], self.origin[1], '+')
        self.cave.strokes(self.rockVectors, '#')


    def parseRocks(self, input):
        rockVectors = []
        for line in input:
            rockVectors += self.rockVectors(line)
        return rockVectors
        
    def translateRocksX(self, rocks, x):
        vectors = []
        for rock in rocks:
            vec = (rock[0] + x, rock[1], rock[2] + x, rock[3])
            vectors.append(vec)
        return vectors

    def makeCave(self, bigger = False):
        (maxx, maxy) = self.getMinMax()[2:]      
        # if bigger:
        #     # "pyramid" width will be (height + 2) * 2, add 2 extra on each side to match test picture
        #     height = maxy + 1 + 2
        #     width = height * 2 + 2
        #     padLeft = (self.origin[0] // (width // 2))
        #     padOrigin = self.origin[0] + pad
        #     self.translateRocksX(self.rockVectors, pad)
        #     self.origin[0] += padOrigin
        # else:
        height = maxy + 1
        width = maxx + 1
        return Cave(width=width, height= height, default='.', expando= bigger)

    def getMinMax(self):
        minX = min(min(list(zip(*self.rockVectors))[0]), min(list(zip(*self.rockVectors))[2]))
        minY = min(min(list(zip(*self.rockVectors))[1]), min(list(zip(*self.rockVectors))[3]))
        maxX = max(max(list(zip(*self.rockVectors))[0]), max(list(zip(*self.rockVectors))[2]))
        maxY = max(max(list(zip(*self.rockVectors))[1]), max(list(zip(*self.rockVectors))[3]))
        return (minX, minY, maxX, maxY)
            
    def rockVectors(self, line):
        stops = line.split(' -> ')
        rockLines = []
        for i in range(0, len(stops)-1):
            ax, ay = json.loads(f'[{stops[i]}]')
            bx, by = json.loads(f'[{stops[i+1]}]')
            rockLines.append(self.orderLines(ax,ay,bx,by))
        return rockLines
        
    def orderLines(self, ax, ay, bx, by):
        minx = min(ax,bx)
        miny = min(ay,by)
        maxx = max(ax,bx)
        maxy = max(ay,by)

        return (minx, miny, maxx, maxy)

    def dropOne(self):
        return self.cave.dropOne(self.origin)

    def dropSand(self):
        infinity = False
        count = 0
        while not infinity:
            infinity = self.dropOne()
            count += 1
        if self.big:
            return count
        # The last sand went to infinity, so remove it from the count
        return count-1

if __name__ == '__main__':
    input = fileReader.read('input.txt')
    input = fileReader.read('input.txt')
    sand = Sand(input)
    count = sand.dropSand()
    print(count)

    sand = Sand(input, True)
    count = sand.dropSand()
    print(count)