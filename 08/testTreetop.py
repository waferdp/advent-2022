import unittest
import fileReader
from treetop import Treetop

class TestTreetop(unittest.TestCase):
    def testParseMatrix(self):
        input = fileReader.read('test_input.txt')
        treetop = Treetop(input)
        assert(treetop.trees.get(2, 2) == 3)

    def testAbove(self):
        input = fileReader.read('test_input.txt')
        treetop = Treetop(input)
        assert(treetop.trees.getAbove(2, 2) == [3, 5])

    def __testVisibilityGeneric(self, x, y, expected):
        input = fileReader.read('test_input.txt')
        treetop = Treetop(input)
        visible = treetop.isVisible(x,y)
        assert(visible == expected)

    def testTopLeftVisible(self):
        aboveAndLeft = (True, False, True, False )
        self.__testVisibilityGeneric(1,1, aboveAndLeft)

    def testTopMiddleVisible(self):
        aboveAndRight = (True, False, False, True)
        self.__testVisibilityGeneric(x=2,y=1, expected= aboveAndRight)

    def testMiddleLeftVisible(self):
        right = (False, False, False, True)
        self.__testVisibilityGeneric(x= 1,y= 2, expected= right)

    def testBottomRightNotVisible(self):
        notVisible = (False, False, False, False)
        self.__testVisibilityGeneric(3, 3, expected= notVisible)

    def testVisibleTrees(self):
        input = fileReader.read('test_input.txt')
        treetop = Treetop(input)
        assert(treetop.getVisibleTrees() == 21)

    def testTopMiddleScore(self):
        input = fileReader.read('test_input.txt')
        treetop = Treetop(input)
        assert(treetop.getTreeScore(x=2, y=1) == 4)

    def testBottomMiddleScore(self):
        input = fileReader.read('test_input.txt')
        treetop = Treetop(input)
        assert(treetop.getTreeScore(x=2, y=3) == 8)


    def testTopScore(self):
        input = fileReader.read('test_input.txt')
        treetop = Treetop(input)
        assert(treetop.getTopScore() == 8)


if __name__ == '__main__':
    unittest.main()