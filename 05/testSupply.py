import unittest
import readFile as file
from supply import Supply

class testSupply(unittest.TestCase):
    def testCreatesLocations(self):
        lines = file.read('test_input.txt')
        supply = Supply(lines)
        assert(len(supply.stackLocations) == 3)

    def testParsesStacks(self):
        lines = file.read('test_input.txt')
        supply = Supply(lines)
        assert(len(supply.stacks) == 3)

    def testStacks(self):
        lines = file.read('test_input.txt')
        supply = Supply(lines)
        assert(supply.topCrates() == 'NDP')

    def testReadsInstructions(self):
        lines = file.read('test_input.txt')
        supply = Supply(lines)
        assert(len(supply.instructions) == 4)

    def testPart1(self):
        lines = file.read('test_input.txt')
        supply = Supply(lines)
        supply.executeInstructions()
        assert(supply.topCrates() == 'CMZ')

    def testPart2(self):
        lines = file.read('test_input.txt')
        supply = Supply(lines, True)
        supply.executeInstructions()
        assert(supply.topCrates() == 'MCD')

if __name__ == '__main__':
    unittest.main()