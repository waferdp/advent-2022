import unittest
import fileReader
from beacon import Beacon

class testBeacon(unittest.TestCase):
    
    def testCaves(self):
        input = fileReader.read('test_input.txt')
        beacon = Beacon(input)
        verify = fileReader.read('test_verify.txt')
        assert(beacon.caves.draw() == verify)

if __name__ == '__main__':
    unittest.main()