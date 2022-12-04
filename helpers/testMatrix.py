import unittest
from matrix import Matrix2d

class TestMatrix(unittest.TestCase):
    def testBelowZero(self):
        matrix = Matrix2d(2,2)
        value = matrix.get(-1, 0)
        assert(value == None)
    
    def testOutOfBounds(self):
        matrix = Matrix2d(2,2)
        value = matrix.get(2, 0)
        assert(value == None)

    def testGet_NotSet_ReturnsDefault(self):
        matrix = Matrix2d(2, 2, 0)
        value = matrix.get(1, 0)
        assert(value == 0)

    def testSet(self):
        matrix = Matrix2d(2, 2)
        matrix.set(1, 0, 'Anything')
        value = matrix.get(1, 0)
        assert('Anything' == value)

if __name__ == '__main__':
    unittest.main()