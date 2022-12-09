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
        assert(rope.rope[0] == (1,0))

    def testMoveHead(self):
        input = fileReader.read('test_input.txt')
        rope = Rope(input)
        rope.executeMoves()
        assert(rope.rope[0] == (2,2))
    
    def testFollowTail(self):
        input = fileReader.read('test_input.txt')
        rope = Rope(input)
        rope.executeMoves()
        assert(rope.rope[-1] == (0,0))

    def testCountVisited(self):
        input = fileReader.read('test_input.txt')
        rope = Rope(input)
        rope.executeMoves()
        assert(len(rope.visited) == 1)

    def testCountVisited2(self):
        input = fileReader.read('test_input2.txt')
        rope = Rope(input)
        rope.executeMoves()
        assert(len(rope.visited) == 36)

if __name__ == '__main__':
    unittest.main()