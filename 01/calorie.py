import readFile as file

class Calorie:
    lines = []
    elves = []

    def __init__(self,input) -> None:
        self.lines = input
        self.elves = Calorie.parseElves(self.lines)
        

    def parseElves(lines):
        elves = []
        elf = 0
        for line in lines:
            if line == '':
                elves.append(elf)
                elf = 0
            else:
                elf += int(line)
        if elf > 0:
            elves.append(elf)
        list.sort(elves)
        return elves

    def greatest(self):
        return self.elves[-1]

    def topThree(self):
        return self.elves[-1] + self.elves[-2] + self.elves[-3]

lines = file.read('input.txt')
calorie = Calorie(lines)
print(calorie.greatest())
print(calorie.topThree())