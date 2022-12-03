import readFile as file

class Rucksack:

    doubles = []

    def __init__(self, input):
        self.doubles = self.parseLines(input)
        

    def parseLines(self, input):
        doubles = []
        for line in input:
            left = line[:len(line)//2]
            right = line[len(line)//2:]
            doubles.append(Rucksack.findDouble(left, right))
        return doubles

    def getValues(self):
        values = 0
        for item in self.doubles:
            values += Rucksack.getSinglValue(item)
        return values

    def getSinglValue(item):
        if item.isupper():
            return ord(item) - 64 + 26
        else:
            return ord(item) - 96

    def findDouble(left,right):
        for x in left:
            if x in right:
                return x
        raise Exception(f'No double found in compartments {left}  {right}')

lines = file.read('test_input.txt')
rucksack = Rucksack(lines)
print(rucksack.getValues())

lines = file.read('input.txt')
rucksack = Rucksack(lines)
print(rucksack.getValues())
