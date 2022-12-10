import fileReader
from enum import Enum

class Op(Enum):
    NOOP = 'noop'
    ADD = 'addx'

class Cathode:

    def __init__(self, input):
        self.x = 1
        self.nextInstruction = 1
        self.signal = {}
        self.cycles = 0
        self.cycleFor(240, input)

    def cycleFor(self, cycles, lines):
        value = 0
        for cycle in range(240):
            self.cycles = cycle
            subCycles = (self.cycles - 20) % 40
            if subCycles == 0:
                self.setSignal()
            if self.cycles + 1 == self.nextInstruction:
                self.x += value
            if self.nextInstruction == self.cycles:
                line = lines.pop(0)
                value = self.executeInstruction(line)


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