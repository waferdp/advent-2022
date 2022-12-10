import fileReader
from enum import Enum

class Op(Enum):
    NOOP = 'noop'
    ADD = 'addx'

class Cathode:

    def __init__(self, input):
        self.x = 1
        self.signal = {}
        self.count = 0
        self.cycles = 0
        self.parseLines(input)

    def parseLines(self, lines):
        for line in lines:
            inst, value = self.parseLine(line)
            if inst == Op.NOOP:
                self.cycles += 1
            else:
                self.cycles += 2
            subCycles = (self.cycles - 20) % 40
            if subCycles <= 1:
                self.setSignal()
            # if 178 < self.cycles < 222:
            #     print (f'During {self.cycles}: {inst.name} {value if value != 0 else ""} - {self.x}')
            self.x += value

    def parseLine(self, line):
        if line == 'noop':
            return (Op(line), 0)
        inst, value = line.split(' ')
        return (Op(inst), int(value))

    def setSignal(self):
        cycles = self.cycles - ((self.cycles - 20) % 40)
        if cycles in self.signal:
            return
        signalStrength = cycles * self.x
        self.signal[cycles] = signalStrength
        
    def getTotal(self):
        return sum(self.signal.values())

if __name__ == '__main__':
    input = fileReader.read('input.txt')
    cathode = Cathode(input)
    print(cathode.getTotal())