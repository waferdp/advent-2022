
class Matrix2d:
    matrix = None
    width = 0
    height = 0
    default = None

    def __init__(self, width, height, default = None):
        self.matrix = {}
        self.width = width
        self.height = height
        self.default = default

    def get(self, x, y):
        if self.isOutOfBounds(x, y):
            return self.default
        try:
            return self.matrix[y][x]
        except:
            return self.default
        
    def set(self, x, y, value):
        if y >= self.height or x >= self.width:
            return
        if y not in self.matrix:
            self.matrix[y] = {}
        self.matrix[y][x] = value

    def isOutOfBounds(self, x,y):
        if x < 0 or y < 0:
            return True
        if x >= self.width or y >= self.height:
            return True

    def getRight(self, x, y):
        start = x
        values = []
        if self.isOutOfBounds(x, y):
            if x < 0 and 0 <= y < self.height:
                start = 0
            else:
                return values
        for x in range(start+1, self.width):
            values.append(self.get(x,y))
        return values

    def getLeft(self, x, y):
        end = x
        values = []
        if self.isOutOfBounds(x, y):
            if x >= 0 and 0 <= y < self.height:
                end = self.width
            return values
        for x in range(0, end):
            values.append(self.get(x,y))
        return values

    def getBelow(self, x, y):
        start = y
        values = []
        if self.isOutOfBounds(x, y):
            if y < 0 and 0 <= x < self.width:
                start = 0
            else:
                return values
        for y in range(start+1, self.height):
            values.append(self.get(x,y))
        return values

    def getAbove(self, x, y):
        end = y
        values = []
        if self.isOutOfBounds(x, y):
            if y >= self.height and 0 <= x < self.width:
                start = 0
            else:
                return values
        for y in range(0, end):
            values.append(self.get(x,y))
        return values