import fileReader
import collections.abc
import json

class Distress:

    def __init__(self, input):
        self.pairs = self.findPairs(input)
        self.pairs.append(([[2]], [[6]]))

    def findPairs(self, input):
        pairs = []
        pair = []
        for line in input:
            if not line:
                pairs.append((pair[0], pair[1]))
                pair = []
            else:
                pair.append(json.loads(line))
        pairs.append(pair)
        return pairs

    def goodPairs(self):
        indices = []
        for i in range(0, len(self.pairs)):
            pair = self.pairs[i]
            if self.compareTo(pair[0], pair[1]) < 0:
                indices.append(i+1)
        return sum(indices)

    def getSorted(self):
        packets = []
        for pair in self.pairs:
            packets += pair
        #packets = self.shitSort(packets)
        packets = self.mergeSort(packets)
        return packets

    def findDividers(self):
        sorted = self.getSorted()
        div2 = sorted.index([[2]]) + 1
        div6 = sorted.index([[6]]) + 1
        return div2 * div6
        
    # Tried implementing more elegant sorting, but decided against it
    def shitSort(self, xs):
        sorted = []
        for x in xs:
            inserted = False
            for i in range(0, len(sorted)):
                if self.compareTo(x, sorted[i]) <= 0:
                    sorted.insert(i, x)
                    inserted = True
                    break
            if not inserted:
                sorted.append(x)
        return sorted

    def mergeSort(self, xs):
        mid = len(xs) // 2
        left = xs[:mid]
        right = xs[mid:]
        if len(left) > 1 and len(right) > 1:
            left = self.mergeSort(left)
            right = self.mergeSort(right)
        merged = self.merge(left, right)
        return merged 

    def merge(self, left, right):
        sorted = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if self.compareTo(left[i], right[j]) < 1:
                sorted.append(left[i])
                i += 1
            else:
                sorted.append(right[j])
                j += 1
        sorted = sorted + left[i:] + right[j:]
        return sorted

    def compareTo(self, a, b):
        isArray = list((map(self.isArray, [a, b])))
        if not any(isArray):
            return self.compareElems(a,b)
        if all(isArray):
            return self.compareArrays(a, b)
        if self.isArray(a):
            return self.compareArrays(a, [b])
        else: 
            return self.compareArrays([a], b)

    def compareArrays(self, a , b):
        for i in range(0, (max(len(a), len(b)))):
            ac = a[i] if len(a) > i else None
            bc = b[i] if len(b) > i else None
            if ac is None and bc is not None:
                return -1
            elif ac is not None and bc is None:
                return 1
            elif ac is None and bc is None:
                return 0
            comparison = self.compareTo(ac, bc)
            if comparison:
                return comparison

    def isArray(self, x):
        return isinstance(x, collections.abc.Sequence)

    def compareElems(self, a, b):
        return (a > b) - (a < b)

if __name__ == '__main__':
    input = fileReader.read('input.txt')
    distress = Distress(input)
    sum = distress.goodPairs()
    product = distress.findDividers()
    print(sum)
    print(product)
