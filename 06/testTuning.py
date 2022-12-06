import unittest
import readFile as file
from tuning import Tuning

class TestTuning(unittest.TestCase):
    
    def testStringMutation(self):
        text = 'abcc'
        areDifferent = Tuning.areAllDifferent(text)
        assert('abcc' == text)
        assert(False == areDifferent)

    def testFindStartFirstMessage(self):
        testData = file.read('test_input.txt')[0]
        tuning = Tuning(testData)
        assert(tuning.startOfStream == 7)

    def testFindStartSecondMessage(self):
        testData = file.read('test_input.txt')[1]
        tuning = Tuning(testData)
        assert(tuning.startOfStream == 5)

    def testFindStartThirdMessage(self):
        testData = file.read('test_input.txt')[2]
        tuning = Tuning(testData)
        assert(tuning.startOfStream == 6)

    def testFindStartFourthMessage(self):
        testData = file.read('test_input.txt')[3]
        tuning = Tuning(testData)
        assert(tuning.startOfStream == 10)

    def testFindStartFifthMessage(self):
        testData = file.read('test_input.txt')[4]
        tuning = Tuning(testData)
        assert(tuning.startOfStream == 11)

    def testFindFirstMessageStart(self):
        testData = file.read('test_input.txt')[0]
        tuning = Tuning(testData,14)
        assert(tuning.startOfStream == 19)

    def testFindSecondMessageStart(self):
        testData = file.read('test_input.txt')[1]
        tuning = Tuning(testData, 14)
        assert(tuning.startOfStream == 23)

    def testFindThirdMessageStart(self):
        testData = file.read('test_input.txt')[2]
        tuning = Tuning(testData, 14)
        assert(tuning.startOfStream == 23)

    def testFindFourthMessageStart(self):
        testData = file.read('test_input.txt')[3]
        tuning = Tuning(testData, 14)
        assert(tuning.startOfStream == 29)

    def testFindFifthMessageStart(self):
        testData = file.read('test_input.txt')[4]
        tuning = Tuning(testData, 14)
        assert(tuning.startOfStream == 26)


if __name__ == '__main__':
    unittest.main()