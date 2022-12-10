
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
        if x < 0 or y < 0:
            return self.default
        if x >= self.width or y >= self.height:
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

    def listOfStrings(self):
        lines = []
        for y in range(0, self.height):
            line = ''
            for x in range(0, self.width):
                line += self.get(x,y)
            lines.append(line)
        return lines