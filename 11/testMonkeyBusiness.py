import unittest
import fileReader
from monkeyBusiness import MonkeyBusiness

class TestMonkeyBusiness(unittest.TestCase):
    
    def testFindMonkeys(self):
        input = fileReader.read('test_input.txt')
        mb = MonkeyBusiness(input)
        assert(len(mb.monkeys) == 4)

    def testOneRound(self):
        input = fileReader.read('test_input.txt')
        mb = MonkeyBusiness(input)
        mb.round()
        assert(mb.monkeys['0'].items == [20, 23, 27, 26])
        assert(mb.monkeys['1'].items == [2080, 25, 167, 207, 401, 1046])

    def testTwentyRounds(self):
        input = fileReader.read('test_input.txt')
        mb = MonkeyBusiness(input)
        for i in range(20):
            mb.round()
        assert(mb.monkeys['0'].items == [10, 12, 14, 26, 34])
        assert(mb.monkeys['1'].items == [245, 93, 53, 199, 115])

    def testMostActive(self):
        input = fileReader.read('test_input.txt')
        mb = MonkeyBusiness(input)
        for i in range(20):
            mb.round()
        actives = mb.getMostActive()
        assert(actives[0] * actives[1] == 10605)

    def testTenKRounds(self):
        input = fileReader.read('test_input.txt')
        mb = MonkeyBusiness(input, divideBy= 1)
        for i in range(10):
            mb.round()
        actives = mb.getMostActive()
        assert(actives[0] * actives[1] == 10197)

if __name__ == '__main__':
    unittest.main()