import unittest
import fileReader
from tetris import Tetris

class TestTetris(unittest.TestCase):
    def testCase1(self):
        input = fileReader.read('test_input.txt')
        tetris = Tetris(input)
        height = tetris.run(2022)
        assert(height == 3068)

    def testCase2(self):
        input = fileReader.read('test_input.txt')
        height = Tetris.calcHeight(input, 1000000000000)
        assert(height == 1514285714288)

if __name__ == '__main__':
    unittest.main()