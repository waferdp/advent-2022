import readFile as file

class Cleanup:
    pairs = []


    def __init__(self, input):
        self.pairs = self.parsePairs(input)
        

    def parsePairs(self, lines):
        pairs = []
        for line in lines:
            leftText,rightText = line.split(',')
            leftL,leftH = list(map(int, leftText.split('-')))
            rightL,rightH = list(map(int, rightText.split('-')))
            pairs.append([(leftL, leftH), (rightL,rightH)])
        return pairs

    def isFullrOverLap(pair):
        (l1,l2),(r1,r2) = pair
        if l1 >= r1 and l2 <= r2:
            return True
        if r1 >= l1 and r2 <= l2:
            return True
        return False 

    def isPartialOverlap(pair):
        (l1,l2),(r1,r2) = pair
        if l2 < r1 or l1 > r2:
            return False
        if r2 < l1 or r1 > r2:
            return False
        return True

    def output(self):
        #return len(list(filter(Cleanup.isFullrOverLap, self.pairs)))
        return len(list(filter(Cleanup.isPartialOverlap, self.pairs)))


lines = file.read('test_input.txt')
cleanup = Cleanup(lines)
print(cleanup.output())

lines = file.read('input.txt')
cleanup = Cleanup(lines)
print(cleanup.output())