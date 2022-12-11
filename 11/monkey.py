from enum import Enum
import re

class Op(Enum):
    Add = '+'
    Multiply = '*'

class Ref(Enum):
    Old = 'Old'
    Value = 'Val'

class Monkey:
    
    def __init__(self, name, number, items, operation, test):
        self.name = name
        self.number = number
        self.items = items,
        self.operation = operation
        self.test = test
        self.inspected = 0

    def inspect(self, divideBy, smallestCommon):
        items = []
        for item in self.items:
            newItemValue = self.operate(item)
            if smallestCommon is not None:
                divided = newItemValue % smallestCommon
            else:
                divided = newItemValue // divideBy

            items.append(divided)
            self.inspected += 1
        return items 

    def runTest(self):
        throws = []
        divisibleBy, ifTrue, ifFalse = self.test
        for item in self.items:
            if item % divisibleBy == 0:                    
                throws.append((ifTrue, item))
            else:
                throws.append((ifFalse, item))
        return throws

    def operate(self, item):
        old = item
        new = eval(self.operation)
        return new

    def parseOperation_old(opText):
        op = Op(re.findall('[+*]', opText)[0])
        numbers = re.findall('[0-9]+', opText)
        value = 1
        if len(numbers):
            ref = Ref.Value
            value = int(numbers[0])
        else:
            ref = Ref.Old
        return op, ref, 
        
    def __repr__(self):
        return f'{self.name}: {self.items}'

