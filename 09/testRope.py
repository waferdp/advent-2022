import unittest
import fileReader
from rope import Rope
from rope import Direction

class TestRope(unittest.TestCase):
    def testParseMoves(self):
        input = fileReader.read('test_input.txt')
        rope = Rope(input)
        assert(len(rope.moves) == 8)
        assert(rope.moves[7] == (Direction.RIGHT, 2))

    def testMoveHeadOnce(self):
        rope = Rope([])
        rope.moveHead((1, 0))
        assert(rope.head == (1,0))

    def testMoveHead(self):
        input = fileReader.read('test_input.txt')
        rope = Rope(input)
        rope.executeMoves()
        assert(rope.head == (2,2))
    
    def testFollowTail(self):
        input = fileReader.read('test_input.txt')
        rope = Rope(input)
        rope.executeMoves()
        assert(rope.tail == (1,2))

    def testCountVisited(self):
        input = fileReader.read('test_input.txt')
        rope = Rope(input)
        rope.executeMoves()
        assert(len(rope.visited) == 13)

if __name__ == '__main__':
    unittest.main()