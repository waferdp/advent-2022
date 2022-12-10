import fileReader
from matrix import Matrix2d
from enum import Enum

class Op(Enum):
    NOOP = 'noop'
    ADD = 'addx'

class Cathode:

    def __init__(self, input):
        self.x = 1
        self.nextInstruction = 1
        self.signal = {}
        self.moveSprite()
        self.cycles = 0
        self.matrix = Matrix2d(height=6, width=40, default='.')
        self.cycleFor(240, input)

    def cycleFor(self, cycles, lines):
        value = 0
        for cycle in range(1, 240):
            #pre-cycle: update class cycle value
            self.cycles = cycle
            subCycles = (self.cycles - 20) % 40

            #Beginning of cycle, read instruction maybe
            if self.nextInstruction == self.cycles:
                line = lines.pop(0)
                value = self.executeInstruction(line)

            # Middle cycle, move sprite to X reg, move sprite, draw pixel, set signal
            self.moveSprite()
            self.draw()
            if subCycles == 0:
                self.setSignal()

            #End of cycle, add value to X reg if next cycle has new instruction
            if self.cycles + 1 == self.nextInstruction:
                self.x += value


    def moveSprite(self):
        self.sprite = [self.x-1,self.x,self.x+1]

    def draw(self):
        x = (self.cycles - 1) % 40
        y = self.cycles // 40
        if x in self.sprite:
            self.matrix.set(x, y, '#' )

    def executeInstruction(self, line):
        inst, value = self.parseLine(line)
        if inst == Op.NOOP:
            self.nextInstruction = self.cycles + 1
        else:
            self.nextInstruction = self.cycles + 2
        return value

    def parseLine(self, line):
        if line == 'noop':
            return (Op(line), 0)
        inst, value = line.split(' ')
        return (Op(inst), int(value))

    def setSignal(self):
        signalStrength = self.cycles * self.x
        self.signal[self.cycles] = signalStrength
        
    def getTotal(self):
        return sum(self.signal.values())

if __name__ == '__main__':
    input = fileReader.read('input.txt')
    cathode = Cathode(input)
    print(cathode.getTotal())
    print(print('\n'.join(cathode.matrix.listOfStrings())))