import readFile as file

class Rucksack:

    doubles = []
    groups = []

    def __init__(self, input):
        #self.doubles = self.parseLines(input)
        self.doubles = self.parseGroups(input)
        
    def parseGroups(self, input):
        groups = []
        for g in range(len(input)//3):
            i = g * 3
            groups.append([input[i], input[i+1], input[i+2]])
        return list(map(self.findCommonItem, groups))

    def parseLines(self, input):
        doubles = []
        for line in input:
            left = line[:len(line)//2]
            right = line[len(line)//2:]
            doubles.append(Rucksack.findDouble(left, right))
        return doubles

    def findCommonItem(self, group):
        for x in group[0]:
            if x in group[1] and x in group[2]:
                return x
        raise Exception(f'No common item found in group {group}')


    def getValues(self):
        values = 0
        for item in self.doubles:
            values += Rucksack.getSinglValue(item)
        return values

    def getSinglValue(item):
        assert(len(item) == 1)
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