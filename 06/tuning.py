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
            if len(lastX) >= self.diffLength:
                lastX = lastX[1:]
            lastX += c
            if len(lastX) == self.diffLength and Tuning.areAllDifferent(lastX):
                return count
        return len(input)
            
    def areAllDifferent(text):
        short = text
        for c in text:
            short = short[1:]
            if c in short:
                return False
        return True

if __name__ == '__main__':
    input = file.read('input.txt')[0]
    tuning = Tuning(input, 14)
    print(tuning.startOfStream)