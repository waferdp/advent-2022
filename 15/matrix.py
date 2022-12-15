
class Matrix2d:
    matrix = None
    maxX = 0
    maxY = 0
    minX = 0
    minY = 0
    default = None

    def __init__(self, width, height, default = None):
        self.matrix = {}
        self.minX = 0
        self.minY = 0
        self.maxX = width - 1
        self.maxY = height - 1
        self.default = default

    def get(self, x, y):
        try:
            return self.matrix[y][x]
        except:
            return self.default
        
    def set(self, x, y, value):
        self.minX = min(self.minX, x)
        self.maxX = max(self.maxX, x)
        self.minY = min(self.minY, y)
        self.maxY = max(self.maxY, y)

        if y not in self.matrix:
            self.matrix[y] = {}
        
        self.matrix[y][x] = value

    def width(self):
        return self.maxX - self.minX + 1

    def height(self):
        return self.maxY - self.minY + 1

    def __repr__(self):
        return self.draw()

    def draw(self):
        lines = []
        return [self.drawLine(y) for y in range(self.minY, self.maxY+1)]
    
    def drawLine(self, y):
        return ''.join([self.get(x, y) for x in range(self.minX, self.maxX+1)])

    def find(self, value):
        for y in self.matrix:
            keys = list(filter(lambda k: self.minX <= k <= self.maxX, ([k for k in self.matrix[y]])))
            missing = self.missing_elements(keys)
            if len(missing) and missing[0] > 0:
                return missing[0], y
        return None

    def missing_elements(self, L):
        start, end = L[0], L[-1]
        return sorted(set(range(start, end + 1)).difference(L))

class FixMatrix2d(Matrix2d):
    
    def __init__(self, other: Matrix2d):
        super().__init__(width=1, height=1, default=other.default)
        self.minX = other.minX
        self.minY = other.minY
        self.maxX = other.maxX
        self.maxY = other.maxY
        self.default = other.default
        self.matrix = other.matrix

    def set(self, x ,y, value):
        if self.minY <= y <= self.maxY and self.minX <= x <= self.maxX:
            return super().set(x, y, value)
        else:
            return

    def min(self, num: int):
        self.minX = num
        self.minY = num

    def max(self, num: int):
        self.maxX = num
        self.maxY = num


