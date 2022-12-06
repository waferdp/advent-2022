import readFile as file

class Tuning:
    startOfStream = 0
    
    def __init__(self, input, diffLength = 4):
        self.diffLength = diffLength
        self.startOfStream = self.findStart(input)

    def findStart(self, input):
        lastX = ''
        count = 0
        for c in input:
            count += 1
            if c in lastX:
                lastX = lastX[lastX.index(c)+1:]
            lastX += c
            if len(lastX) == self.diffLength:
                return count
        return None

if __name__ == '__main__':
    input = file.read('input.txt')[0]
    tuning = Tuning(input, 14)
    print(tuning.startOfStream)