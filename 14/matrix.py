
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
        return self.maxX - self.minX + 1

    def __repr__(self):
        return self.draw()

    def draw(self):
        lines = []
        for y in range(self.minY, self.maxY+1):
            line = ''
            for x in range(self.minX, self.maxX+1):
                line += self.get(x,y)
            lines.append(line)
            line = ''
        return lines    

