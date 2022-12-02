import readFile as file

class RockPaperScissors:

    moves = []
    

    def __init__(self, input):
        self.moves = self.parseInput(input)
        self.mat = RockPaperScissors.pointsMatrix()

    def parseInput(self, input):
        moves = []
        for line in input:
            [a,b] = line.split(' ')
            moves.append([a,b])
        return moves

    def calcPoints(self):
        points = 0
        for move in self.moves:
            points += self.getPoints(move[0], move[1])
        return points
    
    def pointsMatrix():
        mat = {
            'A' : { 
                'X' : 3,
                'Y' : 4,
                'Z' : 8
            },

            'B': {
                'X' : 1,
                'Y' : 5,
                'Z' : 9
            },
            'C': {
                'X' : 2,
                'Y' : 6,
                'Z' : 7
            }

        }
        return mat

    def getPoints(self, a, b):
        return self.mat[a][b]

lines = file.read('test_input.txt')
rpy = RockPaperScissors(lines)
points = rpy.calcPoints()
print(points)

lines = file.read('input.txt')
rpy = RockPaperScissors(lines)
points = rpy.calcPoints()
print(points)