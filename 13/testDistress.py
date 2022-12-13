import unittest
import fileReader
from distress import Distress

class TestDistress(unittest.TestCase):

    def testDistress(self):
        input = fileReader.read('test_input.txt')
        distress = Distress(input)
        assert(len(distress.pairs) == 9)
        assert(len(distress.pairs[0][0]) == 5)

    def testOrder1(self):
        input = fileReader.read('test_input.txt')
        distress = Distress(input)
        comparison = distress.compareTo(distress.pairs[0][0], distress.pairs[0][1])
        assert(comparison == -1)

    def testOrder2(self):
        input = fileReader.read('test_input.txt')
        distress = Distress(input)
        comparison = distress.compareTo(distress.pairs[1][0], distress.pairs[1][1])
        assert(comparison == -1)

    def testOrder3(self):
        input = fileReader.read('test_input.txt')
        distress = Distress(input)
        comparison = distress.compareTo(distress.pairs[2][0], distress.pairs[2][1])
        assert(comparison == 1)

    def testOrder4(self):
        input = fileReader.read('test_input.txt')
        distress = Distress(input)
        comparison = distress.compareTo(distress.pairs[3][0], distress.pairs[3][1])
        assert(comparison == -1)

    def testOrder5(self):
        input = fileReader.read('test_input.txt')
        distress = Distress(input)
        comparison = distress.compareTo(distress.pairs[4][0], distress.pairs[4][1])
        assert(comparison == 1)

    def testOrder6(self):
        input = fileReader.read('test_input.txt')
        distress = Distress(input)
        comparison = distress.compareTo(distress.pairs[5][0], distress.pairs[5][1])
        assert(comparison == -1)

    def testOrder7(self):
        input = fileReader.read('test_input.txt')
        distress = Distress(input)
        comparison = distress.compareTo(distress.pairs[6][0], distress.pairs[6][1])
        assert(comparison == 1)

    def testOrder8(self):
        input = fileReader.read('test_input.txt')
        distress = Distress(input)
        comparison = distress.compareTo(distress.pairs[7][0], distress.pairs[7][1])
        assert(comparison == 1)

    def testSumIndices(self):
            input = fileReader.read('test_input.txt')
            distress = Distress(input)
            sum = distress.goodPairs()
            assert(sum == 22)

    def testFindPackets(self):
            input = fileReader.read('test_input.txt')
            distress = Distress(input)
            product = distress.findDividers()
            assert(product == 140)

if __name__ == '__main__':
    unittest.main()