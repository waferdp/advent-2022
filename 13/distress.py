import fileReader
import collections.abc

class Distress:

    def __init__(self, input):
        self.pairs = self.findPairs(input)

    def findPairs(self, input):
        pairs = []
        pair = []
        for line in input:
            if not line:
                pairs.append((pair[0], pair[1]))
                pair = []
            else:
                pair.append(eval(line))
        pairs.append(pair)
        return pairs

    def goodPairs(self):
        indices = []
        for i in range(0, len(self.pairs)):
            pair = self.pairs[i]
            if self.isRightOrder(pair[0], pair[1]):
                indices.append(i)
        return sum(indices)
        
        comparisons = list(filter(lambda comp: comp < 0, map(lambda a,b: self.isRightOrder(a,b), self.pairs)))
        return len(comparisons)

    def isRightOrder(self, a, b):
        isArray = list((map(self.isArray, [a, b])))
        if not any(isArray):
            return self.compare(a,b)
        if all(isArray):
            return self.compareArrays(a, b)
        if self.isArray(a):
            return self.compareArrays(a, [b])
        else: 
            return self.compareArrays([a], b)

    def compareArrays(self, a , b):
        while True:
            ac = a.pop(0) if len(a) else None
            bc = b.pop(0) if len(b) else None
            if ac is None and bc is not None:
                return -1
            elif ac is not None and bc is None:
                return 1
            elif ac is None and bc is None:
                return 0
            comparison = self.isRightOrder(ac, bc)
            if comparison:
                return comparison

    def isArray(self, x):
        return isinstance(x, collections.abc.Sequence)

    def compare(self, a, b):
        return (a > b) - (a < b)