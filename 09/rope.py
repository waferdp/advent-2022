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
        self.head = (0,0) 
        self.tail = (0,0) 
        self.visited = {self.tail}
        self.moves = self.parseMoves(input)

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
            self.followTail()
            self.visited.add(self.tail)
        

    def directionToMove(dir):
        match dir:
            case Direction.UP: return (0,1)
            case Direction.DOWN: return (0,-1)
            case Direction.LEFT: return (-1,0)
            case Direction.RIGHT: return (1,0)

    def moveHead(self, dir):
        x,y = self.head
        dirX, dirY = dir
        self.head = (x + dirX, y + dirY)

    def followTail(self):
        if self.tail == self.head:
            return
        direction = (self.head[0] - self.tail[0], self.head[1] - self.tail[1])
        dx, dy = direction

        if abs(dx) <= 1 and abs(dy) <= 1:
            return

        nx, ny = 0 if dx == 0 else dx//abs(dx), 0 if dy == 0 else dy//abs(dy)
        tx,ty = self.tail
        self.tail = tx + nx, ty + ny
        
if __name__ == '__main__':
    input = fileReader.read('input.txt')
    rope = Rope(input)
    rope.executeMoves()
    print(len(rope.visited))