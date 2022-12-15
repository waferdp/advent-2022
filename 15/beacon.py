from matrix import Matrix2d
from matrix import FixMatrix2d
import fileReader
import re

class Beacon:
    def __init__(self, input):
        parsed = self.parseRows(input)
        self.sensors = self.parseSensorRanges(parsed)
        self.caves = self.mapCaves(parsed)

    def fixCaves(self, fix):
        if fix is not None:
            self.caves = FixMatrix2d(self.caves)
            self.caves.min(fix[0])
            self.caves.max(fix[1])


    def parseRows(self, input):
        return list(map(self.parseLine, input))

    def parseLine(self, line):
        return list(map(int, re.findall('-?[0-9]+', line)))
        
    def mapCaves(self, parsed):
        caves = Matrix2d(width=1, height=1, default='.')
        for sb in parsed:
            sx, sy, bx, by =  sb
            caves.set(sx, sy, 'S')
            caves.set(bx, by, 'B')
        return caves
        
    def parseSensorRanges(self, parsed):
        return list(map(self.parseSensor, parsed))

    def parseSensor(self, sb):
        sx, sy, bx, by =  sb
        return (sx, sy, self.getDist(sx, sy, bx, by))
        
    def getDist(self, ax, ay, bx, by):
        return (abs(bx - ax) + abs(by-ay))

    def addSensors(self, y = None):
        count = 0
        for sensor in self.sensors:
            # count += 1
            # print(f'{count}: {sensor}')
            if y is None:
                self.addDiamond(sensor)
            elif abs(sensor[1] - y) <= sensor[2]:
                self.addDiamond(sensor, y)

    def getRow(self, y):
        row = list(self.caves.matrix[y].values())
        return row.count('#')

    def getFrequency(self, low, high):
        index = self.findBeacon(low, high) 
        return index[0] * 4000000 + index[1]

    def findBeacon(self, low, high):
        count = 0
        for sensor in self.sensors:
            sx, sy, d = sensor
            count += 1
            print(f'{count}/{len(self.sensors)}')
            
            p = (sx - d - 1, sy)
            #9-12
            while p[0] < sx+1 and p[1] > sy-d-1:
                if p[0] >= low and p[1] >= low and self.notCovered(p[0], p[1]):
                        return p
                p = (p[0] + 1, p[1] - 1)
            #12-3
            while p[0] < sx+d+1 and p[1] < sy+1:
                if p[0] <= high and p[1] >= low and self.notCovered(p[0], p[1]):
                        return p
                p = (p[0] + 1, p[1] + 1)
            #3-6
            while p[0] >= sx-1 and p[1] < sy+d+1:
                if p[0] <= high and p[1] <= high and self.notCovered(p[0], p[1]):
                        return p
                p = (p[0] - 1, p[1] + 1)
            #6-9
            while p[0] >= sx-d-1 and p[1] > sy-1:
                if p[0] >= low and p[1] <= high and self.notCovered(p[0], p[1]):
                        return p
                p = (p[0] - 1, p[1] - 1)

    def findBeacon_old(self, low, high, onlyLimits = False):
        count = 0
        print(f'Total (in million): { pow((high-low), 2) // 1000000}')
        for y in range (low, low+1):
            for x in range(low, high+1):
                count += 1
                if(count % 1000000 == 0):
                    print(count // 1000000)
                if self.notCovered(x,y):
                    return x,y
        raise Exception("Not found")

    def notCovered(self, x, y):
        for (sx,sy,d) in self.sensors:
            if self.getDist(x,y,sx,sy) <= d:
                found = False
                return False
        return True

    def addDiamond(self, sensor, row = None):
        #top:
        ox, oy, sensorRange = sensor
        for y in range(oy-sensorRange, oy+sensorRange+1):
            if row is not None and row != y:
                continue
            if self.caves.minY <= y <= self.caves.maxY:
                for x in range(ox-sensorRange, ox+sensorRange+1):
                    if self.caves.minX <= x <= self.caves.maxX:
                        if self.getDist(ox,oy, x, y) <= sensorRange:
                            if(self.caves.get(x, y) == '.'):
                                self.caves.set(x, y, '#')

if __name__ == '__main__':
    input = fileReader.read('input.txt')
    beacon = Beacon(input)
    #y = 2000000
    #beacon.fixCaves((0, 4000000))
    #beacon.addSensors()
    #count = beacon.getRow(y)
    #print(count)

    freq = beacon.getFrequency(0, 4000000)
    print(freq)