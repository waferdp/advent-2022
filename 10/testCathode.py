import unittest
import fileReader
from cathode import Cathode

class TestCathode(unittest.TestCase):

    def testInput(self):
        input = fileReader.read('test_input.txt')
        cathode = Cathode(input)
        assert(cathode.signal[20] == 420)
        assert(cathode.signal[60] == 1140)
        assert(cathode.signal[100] == 1800)
        assert(cathode.signal[140] == 2940)
        assert(cathode.signal[180] == 2880)
        assert(cathode.signal[220] == 3960)
        assert(cathode.getTotal() == 13140)

    def testPrint(self):
        input = fileReader.read('test_input.txt')
        expected = fileReader.read('test_expected.txt')
        cathode = Cathode(input)
        assert(expected == cathode.matrix.listOfStrings())

if __name__ == '__main__':
    unittest.main()