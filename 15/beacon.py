from matrix import Matrix2d
import fileReader
import re

class Beacon:
    def __init__(self, input):
        parsed = self.parseRows(input)
        self.sensors = self.parseSensorRanges(parsed)
        self.caves = self.mapCaves(parsed)

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
        distance= (abs(bx - sx) + abs(by-sy))
        return (sx, sy, distance)
        