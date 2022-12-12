import unittest
import fileReader
from climbing import Climbing

class TestClimbing(unittest.TestCase):

    def testParseMap(self):
        input = fileReader.read('test_input.txt')
        climbing = Climbing(input)
        assert(climbing.start == (0,0))
        assert(climbing.finish == (5,2))

    def testClimbOnce(self):
        input = fileReader.read('test_input.txt')
        climbing = Climbing(input)
        climbing.step()
        assert(len(climbing.paths) == 2)

if __name__ == '__main__':
    unittest.main()