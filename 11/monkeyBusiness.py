import re
from monkey import Op
from monkey import Ref
from monkey import Monkey
from functools import reduce
import fileReader
import math

class MonkeyBusiness:

    def __init__(self, input, divideBy = 3):
        self.divideBy = divideBy
        monkeyTexts = self.findMonkeys(input)
        monkeys = map(self.parseMonkey, monkeyTexts)
        self.monkeys = dict()
        for monkey in monkeys:
            self.monkeys[monkey.number] = monkey
        if divideBy == 1:
            self.smallestCommon = self.findSmallestDenominator() 
        else:
            self.smallestCommon = None

    def findSmallestDenominator(self):
        divisors = [m.test[0] for m in list(self.monkeys.values())]
        return math.prod(divisors)  

    def findMonkeys(self, input):
        monkeys = []
        monkeyText = []
        for line in input:
            if line == '':
                monkeys.append(monkeyText)
                monkeyText = []
            else:
                monkeyText.append(line)
        monkeys.append(monkeyText)
        return monkeys

    def parseMonkey(self, text):
        name = text[0].replace(':', '')
        number = name[-1]
        items = list(map(int, re.findall('[0-9]+', text[1]))) 
        operation = self.parseOperation(text[2].split('=')[1].strip())
        test = self.parseTest(text[3:6])
        monkey = Monkey(name= name, number= number, items= items, operation= operation, test= test)
        monkey.items = items
        return monkey

    def parseOperation(self, opText):
        return opText.split(':')[-1].strip()

    def parseTest(self, testLines):
        divisibleBy = re.findall('[0-9]+', testLines[0])[0]
        ifTrue = re.findall('[0-9]+', testLines[1])[0]
        ifFalse = re.findall('[0-9]+', testLines[2])[0]
        return int(divisibleBy), ifTrue, ifFalse

    def round(self):
        for i in self.monkeys:
            monkey = self.monkeys[i]
            monkey.items = monkey.inspect(self.divideBy, self.smallestCommon)
            throws = monkey.runTest()
            monkey.items = []
            for dest, item in throws:
                self.monkeys[dest].items.append(item)
            
    def getMostActive(self):
        actives = [m.inspected for m in list(self.monkeys.values())]
        actives.sort()  
        return actives[-2:]

if __name__ == '__main__':            
    input = fileReader.read('input.txt')
    mb = MonkeyBusiness(input, divideBy= 1)
    for i in range(10000):
        if i % 10 == 0:
            print(f'{i}')
        mb.round()
    actives = mb.getMostActive()
    print(actives[0] * actives[1])