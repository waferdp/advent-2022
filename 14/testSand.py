import unittest
import fileReader
from sand import Sand

class TestSand(unittest.TestCase):
    
    def testMinMax(self):
        input = fileReader.read('test_input.txt')
        sand = Sand(input)
        minMax = sand.getMinMax()
        assert(minMax == (0, 4, 9, 9))

    def testRocks(self):
        input = fileReader.read('test_input.txt')
        sand = Sand(input)
        verify = fileReader.read('test_verify1.txt')
        drawn = sand.cave.draw()
        assert(drawn == verify)

    def testDropOne(self):
        input = fileReader.read('test_input.txt')
        sand = Sand(input)
        sand.dropOne()
        verify = fileReader.read('test_verify2.txt')
        drawn = sand.cave.draw()
        assert(drawn == verify)

    def testDropUntilDone(self):
        input = fileReader.read('test_input.txt')
        sand = Sand(input)
        count = sand.dropSand()
        verify = fileReader.read('test_verify3.txt')
        drawn = sand.cave.draw()
        assert(drawn == verify)
        assert(count == 24)

    def testDropBig(self):
        input = fileReader.read('test_input.txt')
        sand = Sand(input, True)
        count = sand.dropSand()
        verify = fileReader.read('test_verify4.txt')
        drawn = sand.cave.draw()
        assert(drawn == verify)
        assert(count == 93)

if __name__ == '__main__':
    unittest.main()