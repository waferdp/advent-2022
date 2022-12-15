import unittest
import fileReader
from beacon import Beacon

class testBeacon(unittest.TestCase):
    
    def testCaves(self):
        input = fileReader.read('test_input.txt')
        beacon = Beacon(input)
        verify = fileReader.read('test_verify.txt')
        assert(beacon.caves.draw() == verify)

    def testSensorRange(self):
        input = fileReader.read('test_input.txt')
        beacon = Beacon(input)
        assert(beacon.sensors[8][2] == 3)

    def testAddOneDiamond(self):
        input = fileReader.read('test_input.txt')
        beacon = Beacon(input)
        beacon.addDiamond(beacon.sensors[6])
        verify = fileReader.read('test_verify2.txt')
        assert(beacon.caves.draw() == verify)

    def testSensorRow(self):
        input = fileReader.read('test_input.txt')
        beacon = Beacon(input)
        beacon.addSensors()
        count = beacon.getRow(10)
        assert(count == 26)

    def testSpecificSensorRow(self):
        input = fileReader.read('test_input.txt')
        beacon = Beacon(input)
        beacon.addSensors(10)
        count = beacon.getRow(10)
        assert(count == 26)

    def testFindMissing(self):
        input = fileReader.read('test_input.txt')
        beacon = Beacon(input)
        #beacon.fixCaves((0,20))
        #beacon.addSensors()
        index = beacon.findBeacon(0, 20)
        freq = beacon.getFrequency(0, 20)
        assert(index == (14,11))
        assert(freq == 56000011)

if __name__ == '__main__':
    unittest.main()