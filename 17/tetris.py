from shape import Shape
from matrix import Matrix2d
import fileReader


class Tetris:
    def __init__(self, input):
        self.movements = input[0]
        self.moveIndex = 0
        self.height = 30
        self.z = [0] * 7
        self.resting = Matrix2d(7,1, '.')
        for x in range(0,7):
            self.resting.set(x,0, '-')
        self.shapes = '-+LI#'
        self.shapeIndex = 0
        self.dropped = 0
        self.clearInterval = 100000

    def run(self, until) -> int:
        for i in range(until):
            self.drop()
            # if i > 0 and i % self.clearInterval == 0:
            #     print(f'{(i / until)*100}%')
            #     self.height += self.resting.maxY - 30
            #     self.resetResting()
        return self.resting.maxY


    def findCycle(self):
        ids = dict()
        while True:
            signature = self.drop()
            if signature in ids:
                lastTime = ids[signature]
                print(f'Cycle found {lastTime} to {self.dropped}: {signature}')
                return lastTime, self.dropped, signature
                break
            ids[signature] = self.dropped

    def calcHeight(input, bigNumber):
        cycleTet = Tetris(input)
        start, end, signature = cycleTet.findCycle()
        length = end-start
        startTet = Tetris(input)
        atStart = startTet.run(start)
        endTet = Tetris(input)
        atEnd = endTet.run(end)
        heightDiff = atEnd - atStart

        cycles = (bigNumber - start) // length
        remaining = bigNumber - (cycles * length)
        endTet = Tetris(input)
        endHeight = endTet.run(remaining)
        return cycles * heightDiff + endHeight

    def drop(self):
        dropping = True
        shape = self.getNextShape()
        while dropping:
            dropping = self.step(shape)
        for y,x in shape.shape:
            self.resting.set(x,y, '#')
            self.updateLowestPoint(shape)
            #self.z[x] = max(self.z[x], y)
        self.dropped += 1
        signature = self.getSignature(shape)
        return signature

    def updateLowestPoint(self, shape):
        for x in range(0, len(self.z)):
            y = self.z[x]
            ry = self
            if self.resting.get(y+1, x) == '#':
                self.z[x] = y+1

    def getSignature(self, shape: Shape):
        lowestPoint = min(self.z)
        sign = shape.sign
        index = self.moveIndex
        height = self.resting.maxY + 4 - lowestPoint
        return (sign, index, height)

    def resetResting(self):
        restingMap = [self.resting.drawLine(y) for y in range(self.resting.maxY-30, self.resting.maxY+1)]
        self.resting = Matrix2d(width=7, height=30, default='.')
        for y in range(0, len(restingMap)):
            for x in range(0, len(restingMap[y])):
                self.resting.set(x,y, restingMap[y][x])

    def step(self, shape: Shape):
        self.signMove(shape)
        return self.downMove(shape)
        
    def signMove(self, shape: Shape):
        sign = self.getNextMove()
        shape.move(sign=sign)

    def downMove(self, shape: Shape):
        return shape.move('')

    def getNextMove(self):
        sign = self.movements[self.moveIndex]
        self.moveIndex = self.nextIndex(self.moveIndex, self.movements)
        return sign

    def getNextShape(self) -> Shape:
        sign = self.shapes[self.shapeIndex]
        self.shapeIndex = self.nextIndex(self.shapeIndex, self.shapes)
        return Shape(sign, self.resting)

    def nextIndex(self, i, xs):
        return i + 1 if (i + 1) < len(xs) else 0

if __name__ == '__main__':
    input = fileReader.read('input.txt')
    tetris = Tetris(input)
    height = tetris.run(2022)
    print(height)

    height2 = Tetris.calcHeight(input, 1000000000000)
    print(height2)

