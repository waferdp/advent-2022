import readFile as file
import re

class Supply:

    def __init__(self, input, multiMove = False):
        self.stacksText, self.instructionText = self.getParts(input)
        self.stackLocations = self.getLinePart(self.stacksText)
        self.stacks = self.parseStacks(self.stacksText)
        self.instructions = self.parseInstructions(self.instructionText)
        self.multiMove = multiMove

    def getParts(self, input):
        stacksPart = self.getStacksPart(input)
        instructionsPart = input[len(stacksPart) + 1:]
        return stacksPart, instructionsPart

    def getStacksPart(self, input):
        stacks = []
        for line in input:
            if line == '':
                return stacks
            stacks.append(line)

    def getLinePart(self, stacksPart):
        numbers = list(stacksPart[-1].split(' '))
        locations = {}
        for number in numbers:
            if len(number):
                location = stacksPart[-1].index(number)
                locations[number] = location
        return locations

    def newStacks(self):
        stacks = {}
        for number in self.stackLocations:
            stacks[number] = []
        return stacks

    def parseStacks(self, stacksText):
        stacks = self.newStacks()
        stacksText.pop()
        while len(stacksText):
            row = stacksText[-1]
            for number in self.stackLocations:
                if self.stackLocations[number] >= len(row):
                    break
                crate = row[self.stackLocations[number]]
                if crate == ' ':
                    continue
                stacks[number].append(crate)
            stacksText.pop()
        return stacks

    def parseInstructions(self, lines):
        instructions = []
        for line in lines:
            numbers = re.findall('[0-9]+', line)
            instructions.append((int(numbers[0]), numbers[1], numbers[2]))
        return instructions
    
    def executeInstructions(self):
        for (amount, fro, to) in self.instructions:
            if not self.multiMove:
                for x in range(amount):
                    self.stacks[to].append(self.stacks[fro].pop())
            else:
                lift = self.stacks[fro][-amount:]
                self.stacks[fro] = self.stacks[fro][:-amount]
                self.stacks[to] += lift
        
    def topCrates(self):
        crates = ''
        for stack in self.stacks:
            crates += self.stacks[stack][-1]
        return crates

lines = file.read('input.txt')
supply = Supply(lines, True)
supply.executeInstructions()
print(supply.topCrates())
