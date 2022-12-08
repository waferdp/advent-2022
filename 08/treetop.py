import fileReader
from matrix import Matrix2d

class Treetop:

    def __init__(self, input):
        self.trees = self.parseInput(input)


    def parseInput(self, input):
        width = len(input[0])
        height = len(input)
        matrix = Matrix2d(width= width, height= height, default=0)

        for y in range(0, height):
            for x in range(0, width):
             matrix.set(x, y, int(input[y][x]))

        return matrix

    def isVisible(self, x, y):
        treeHeight = self.trees.get(x, y)
        above = self.trees.getAbove(x, y)
        below = self.trees.getBelow(x, y)
        left = self.trees.getLeft(x, y)
        right = self.trees.getRight(x, y)

        above = len(above) == 0 or max(above) < treeHeight
        below = len(below) == 0 or max(below) < treeHeight
        left = len(left) == 0 or max(left) < treeHeight
        right = len(right) == 0 or max(right) < treeHeight

        return (above, below, left, right)

    def getVisibleTrees(self):
        visible = 0
        for y in range(0, self.trees.height):
            for x in range(0, self.trees.width):
                if any(self.isVisible(x,y)):
                    visible += 1
        return visible
    
    def getTreeScore(self, x, y):
        treeHeight = self.trees.get(x, y)
        above = self.countLower(self.trees.getAbove(x, y)[::-1], treeHeight)
        below = self.countLower(self.trees.getBelow(x, y), treeHeight)
        left = self.countLower(self.trees.getLeft(x, y)[::-1], treeHeight)
        right = self.countLower(self.trees.getRight(x, y), treeHeight)

        score = above * left * below * right
        return score

    def getTopScore(self):
        topScore = 0
        for y in range(0, self.trees.height):
            for x in range(0, self.trees.width):
                topScore = max(topScore, self.getTreeScore(x, y))
        return topScore

    def countLower(self, trees, treeHeight):
        count = 0
        for tree in trees:
            count +=1
            if tree >= treeHeight:
                return count
        return count

if __name__ == '__main__':
    input = fileReader.read('input.txt')
    treetop = Treetop(input)
    print(treetop.getVisibleTrees())
    print(treetop.getTopScore())