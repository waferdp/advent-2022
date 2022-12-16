import unittest
import fileReader
from pressure import Pressure

class testPressure(unittest.TestCase):
    def testGetPairs(self):
        input = fileReader.read('test_input.txt')
        pressure = Pressure(input)
        routes = pressure.graph.findRoutes()
        assert(len(routes) == 36)

    def testSearch(self):
        input = fileReader.read('test_input.txt')
        pressure = Pressure(input)
        pressure.graph.setFlowValves()
        flowed = pressure.maxPressure()
        assert(flowed == 1651)

    # def testWithElephant(self):
    #     input = fileReader.read('test_input.txt')
    #     pressure = Pressure(input)
    #     pressure.graph.setFlowValves()
    #     flowed = pressure.maxPressure()
    #     assert(flowed == 1651)

if __name__ == '__main__':
    unittest.main()