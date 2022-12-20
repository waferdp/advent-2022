import unittest
import fileReader
from pressure import Pressure

class testPressure(unittest.TestCase):
    def testGetPairs(self):
        input = fileReader.read('test_input.txt')
        pressure = Pressure(input)
        routes = pressure.graph.findRoutes()
        assert(len(routes) == 7)

    def testSearch(self):
        input = fileReader.read('test_input.txt')
        pressure = Pressure(input)
        pressure.graph.setFlowValves()
        flowed = pressure.maxPressure()
        assert(flowed == 1651)

    def testGetFlow(self):
        input = fileReader.read('test_input.txt')
        pressure = Pressure(input)
        opened = {
            'DD': 2,
            'BB': 5,
            'JJ': 9,
            'HH': 17,
            'EE': 21,
            'CC': 24
        }
        flowed = pressure.getFlow(opened)
        assert(flowed == 1651)

    # def testWithElephant(self):
    #     input = fileReader.read('test_input.txt')
    #     pressure = Pressure(input)
    #     pressure.graph.setFlowValves()
    #     flowed = pressure.maxPressure()
    #     assert(flowed == 1651)

if __name__ == '__main__':
    unittest.main()