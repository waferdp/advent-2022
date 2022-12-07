import fileReader
from enum import Enum
from files import File


class Space:

    totalSpace = 70000000
    neededSpace = 30000000

    def __init__(self, input):
        self.root, self.filetree = self.parseCommands(input)

    def parseCommands(self, input):
        current = None
        root = None
        for line in input:
            (lineType, data) = Space.parseLine(line)
            if lineType == 'cd':
                current = self.changeFolder(data, current)
                if root is None:
                    root = current
            elif lineType == 'dir':
                current.addChild(self.addFolder(data, current))
            elif lineType == 'file':
                current.addChild(self.addFile(data, current))
        return root, current

    def changeFolder(self, data, current):
        if '..' in data:
            current = current.parent
        else:
            name = data
            if current is None:
                folder = File(name=name, type='dir', parent=current)
                current = folder
            else:
                current = current.children[name]
        return current

    def addFolder(self, data, current):
        newFolder = File(name=data, type='dir', parent=current)
        return newFolder

    def addFile(self, data, parent):
        size,name = data
        newFile = File(name=name, type='file', size=int(size), parent=parent)
        return newFile

    def parseLine(line):
        if line[0:4] == '$ cd':
            return ('cd', line[4:].strip()) 
        elif line[0:4] ==  '$ ls':
            return ('ls', None)
        elif line[0:3] == 'dir':
            return ('dir', line[4:])
        else:
            return ('file', line.split(' '))

    def getSizeWithLimit(self, limit):
        belowLimit = []
        self.root.getSize(limit= limit, belowLimit= belowLimit)
        totalSize = Space.sumSizeTuples(belowLimit)
        return totalSize

    def getAllSizes(self):
        sizes = []
        self.root.getSize(belowLimit= sizes)
        sizes = sorted(sizes, key=lambda x: x[1] )
        return sizes

    def sumSizeTuples(sizeTuples):
        return sum(list(zip(*sizeTuples))[1])

    def findSmallestDirSize(self):
        sortedSizeTuples = self.getAllSizes()
        totalSize = sortedSizeTuples[-1][1]
        for sizeTuple in sortedSizeTuples:
            if self.totalSpace - totalSize + sizeTuple[1] >= self.neededSpace:
                return sizeTuple

if __name__ == '__main__':
    input = fileReader.read('input.txt')
    space = Space(input)
    hundredK = 100000
    totalSize = space.getSizeWithLimit(hundredK)
    print(totalSize)

    smallestDir = space.findSmallestDirSize()
    print(smallestDir[1])