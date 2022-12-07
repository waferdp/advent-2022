import unittest
import fileReader
from space import Space

class TestTuning(unittest.TestCase):
    def testTree(self):
        input = fileReader.read('test_input.txt')
        space = Space(input)
        assert(space.root is not None)

    def testSize(self):
        input = fileReader.read('test_input.txt')
        space = Space(input)
        assert(space.root.getSize() > 0)

    def testBelow10k(self):
        input = fileReader.read('test_input.txt')
        space = Space(input)
        below100K = []
        space.root.getSize(100000, below100K)
        assert(len(below100K) == 2)

    def testSumDirs(self):
        input = fileReader.read('test_input.txt')
        space = Space(input)
        hundredK = 100000
        totalSize = space.getSizeWithLimit(hundredK)
        assert(totalSize == 95437)
    
    def testSortDirs(self):
        input = fileReader.read('test_input.txt')
        space = Space(input)
        sorted = space.getAllSizes()
        assert(sorted[0][1] < sorted[1][1])

    def testSpaceRemoval(self):
        input = fileReader.read('test_input.txt')
        space = Space(input)
        smallestDir = space.findSmallestDirSize()
        assert(smallestDir[0] == 'd')
        assert(smallestDir[1] == 24933642)

if __name__ == '__main__':
    unittest.main()