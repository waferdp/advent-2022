from matrix import Matrix2d
import fileReader
import re

class Beacon:
    def __init__(self, input):
        parsed = self.parseRows(input)
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
        

