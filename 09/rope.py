from enum import Enum
import math
import fileReader

class Direction(str, Enum):
    UP = 'U'
    DOWN = 'D'
    LEFT = 'L'
    RIGHT = 'R'

class Rope:

    def __init__(self, input):
        self.rope = self.generateRope()
        self.visited = {self.rope[-1]}
        self.moves = self.parseMoves(input)

    def generateRope(self):
        rope = []
        for x in range(10):
            rope.append((0,0))
        return rope

    def parseMoves(self, input):
        moves = []
        for line in input:
            dir, steps = line.split(' ')
            moves.append((dir, int(steps)))
        return moves

    def executeMoves(self):
        for move in self.moves:
            self.makeMove(move)

    def makeMove(self, move):
        steps = move[1]
        inc = Rope.directionToMove(move[0])
        for x in range(steps):
            self.moveHead(inc)
            for i in range(1,len(self.rope)):
                self.rope[i] = self.followTail(self.rope[i], self.rope[i-1])
            self.visited.add(self.rope[-1])
        

    def directionToMove(dir):
        match dir:
            case Direction.UP: return (0,1)
            case Direction.DOWN: return (0,-1)
            case Direction.LEFT: return (-1,0)
            case Direction.RIGHT: return (1,0)

    def moveHead(self, dir):
        x,y = self.rope[0]
        dirX, dirY = dir
        self.rope[0] = (x + dirX, y + dirY)

    def followTail(self, tail, head):
        if tail == head:
            return tail
        direction = (head[0] - tail[0], head[1] - tail[1])
        dx, dy = direction

        if abs(dx) <= 1 and abs(dy) <= 1:
            return tail

        nx, ny = 0 if dx == 0 else dx//abs(dx), 0 if dy == 0 else dy//abs(dy)
        tx,ty = tail
        tail = tx + nx, ty + ny
        return tail
        
if __name__ == '__main__':
    input = fileReader.read('input.txt')
    rope = Rope(input)
    rope.executeMoves()
    print(len(rope.visited))